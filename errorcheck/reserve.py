import re
from paramiko import SSHClient, AutoAddPolicy
from regex import return_output
from whichmachine import name_of_machine
import json
from base import insert_network_stats
from conditions import Check

velia_hosts = ['lx8', 'lx9', 'af14', 'app6', 'lx10', 'af15', 'app7', 'lx5-test', 'grafana', 'loki', 'shiva', 'zabbix5',
               'lx11', 'lx12', 'lx13', 'lx14', 'lx15', 'lx16', 'lx17', 'lx18', 'lx19']
data = []
network_pattern = r'^([^\s:]+)'
rx_errors_pattern = r'RX errors.*'
tx_errors_pattern = r'TX errors.*'

for host in velia_hosts:
    # HERE WE CONNECT WITH OPENSSH WITH PARAMIKO TO ALL VELIE MACHINES THAT HAVE NET-TOOLS INSTALLED
    client = SSHClient()
    # LOAD HOST KEYS
    client.load_host_keys('/home/martin.kirilov/.ssh/known_hosts')
    client.set_missing_host_key_policy(AutoAddPolicy())
    client.load_system_host_keys()
    client.connect(host, port=22, username='martin.kirilov')
    # TAKING THE OUTPUT
    stdin, stdout, stderr = client.exec_command('ifconfig')
    # IN THAT LIST WE APPEND ALL THE NETWORK NAMES AND ERRORS FOR EVERY INSTANCE IN THE FORM OF A STRING
    list = []

    if stdout.channel.recv_exit_status() == 0:
        # DECODING THE OUTPUT
        output_decoded = stdout.read().decode('utf8')
        result = return_output(output_decoded)

        for instance in result[0]:
            network_match = re.search(network_pattern, instance, re.MULTILINE)
            network_name = network_match.group(1) if network_match else None

            # Find the line with RX errors
            rx_errors_match = re.search(rx_errors_pattern, instance, re.MULTILINE)
            rx_errors_line = rx_errors_match.group() if rx_errors_match else None

            # Find the line with TX errors
            tx_errors_match = re.search(tx_errors_pattern, instance, re.MULTILINE)
            tx_errors_line = tx_errors_match.group() if tx_errors_match else None

            # Print the extracted information for the current instance
            list.append(f"{network_name}\n"
                        f"{rx_errors_line}\n"
                        f"{tx_errors_line}\n")
            if rx_errors_line is not None:
                rx_error_line_split = rx_errors_line.split('  ')
                tx_error_line_split = tx_errors_line.split('  ')
                rx_error_counts = rx_error_line_split[0]
                tx_error_counts = tx_error_line_split[0]

                rx_error_number = rx_error_counts[-1]
                tx_error_number = tx_error_counts[-1]

            machine_data = {}
            machine_data['name'] = name_of_machine(host)
            machine_data['network_name'] = network_name
            machine_data['rx_error'] = rx_error_number
            machine_data['tx_error'] = tx_error_number
            data.append(machine_data)
            print(machine_data)
        # IF WE WANT TO PRINT ALL THE ERRORS ON VELIA MACHINES
        # dictionaries = ready_data(output_decoded)

json_data = json.dumps(data, indent=4)

with open("data.json", "w") as file:
    file.write(json_data)