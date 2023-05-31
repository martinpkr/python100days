from paramiko import SSHClient , AutoAddPolicy

def name_of_machine(host):
    client = SSHClient()
    # LOAD HOST KEYS
    client.load_host_keys('/home/martin.kirilov/.ssh/known_hosts')
    client.set_missing_host_key_policy(AutoAddPolicy())
    client.load_system_host_keys()
    client.connect(host, port=22, username='martin.kirilov')
    stdin, stdout, stderr = client.exec_command('hostname')

    print(stdout.read().decode('utf-8'))