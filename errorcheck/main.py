
from paramiko import SSHClient, AutoAddPolicy
from regex import return_output
from whichmachine import name_of_machine
from seperating import ready_data
from base import insert_network_stats
from conditions import Check
velia_hosts = ['lx8', 'lx9', 'af14', 'app6', 'lx10', 'af15', 'app7', 'lx5-test', 'grafana', 'loki', 'shiva', 'zabbix5',
               'lx11', 'lx12', 'lx13', 'lx14', 'lx15', 'lx16', 'lx17', 'lx18', 'lx19']

for host in velia_hosts:
    client = SSHClient()
    #LOAD HOST KEYS
    client.load_host_keys('/home/martin.kirilov/.ssh/known_hosts')
    client.set_missing_host_key_policy(AutoAddPolicy())
    client.load_system_host_keys()
    client.connect(host,port=22,username='martin.kirilov')
    stdin, stdout, stderr = client.exec_command('ifconfig')

    if stdout.channel.recv_exit_status() == 0:
        name_of_machine(host)
        output_decoded = stdout.read().decode('utf8')
        print(return_output(output_decoded))  #IF WE WANT TO PRINT ALL THE ERRORS ON VELIA MACHINES
        dictionaries = ready_data(output_decoded)





