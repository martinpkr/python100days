import re
import json
from multiprocessing import Pool
from paramiko import SSHClient, AutoAddPolicy
from regex import return_output
from whichmachine import name_of_machine

velia_hosts = ['lx8', 'lx9', 'af14', 'app6', 'lx10', 'af15', 'app7', 'lx5-test', 'grafana', 'loki', 'shiva', 'zabbix5',
               'lx11', 'lx12', 'lx13', 'lx14', 'lx15', 'lx16', 'lx17', 'lx18', 'lx19']

network_pattern = re.compile(r'^([^\s:]+)')
rx_errors_pattern = re.compile(r'RX errors.*')
tx_errors_pattern = re.compile(r'TX errors.*')

def extract_data(host):
    data = []

    try:
        client = SSHClient()
        client.load_host_keys('/home/martin.kirilov/.ssh/known_hosts')
        client.set_missing_host_key_policy(AutoAddPolicy())
        client.load_system_host_keys()
        client.connect(host, port=22, username='martin.kirilov')

        stdin, stdout, stderr = client.exec_command('ifconfig')

        if stdout.channel.recv_exit_status() == 0:
            output_decoded = stdout.read().decode('utf8')
            result = return_output(output_decoded)

            for instance in result[0]:
                network_match = network_pattern.search(instance)
                network_name = network_match.group(1) if network_match else None

                rx_errors_match = rx_errors_pattern.search(instance)
                rx_errors_line = rx_errors_match.group() if rx_errors_match else None

                tx_errors_match = tx_errors_pattern.search(instance)
                tx_errors_line = tx_errors_match.group() if tx_errors_match else None

                rx_error_number = '0'
                tx_error_number = '0'

                if rx_errors_line is not None:
                    rx_error_line_split = rx_errors_line.split('  ')
                    tx_error_line_split = tx_errors_line.split('  ')
                    rx_error_counts = rx_error_line_split[0]
                    tx_error_counts = tx_error_line_split[0]

                    rx_error_number = rx_error_counts[-1]
                    tx_error_number = tx_error_counts[-1]

                machine_data = {
                    'name': name_of_machine(host),
                    'network_name': network_name,
                    'rx_error': rx_error_number,
                    'tx_error': tx_error_number
                }

                data.append(machine_data)

    finally:
        client.close()

    return data

# Use a multiprocessing Pool for concurrent execution
with Pool() as pool:
    results = pool.map(extract_data, velia_hosts)

# Flatten the results list
data = [item for sublist in results for item in sublist]
print(data)
# Save the data to JSON file
json_data = json.dumps(data, indent=4)

with open("data.json", "w") as file:
    file.write(json_data)
