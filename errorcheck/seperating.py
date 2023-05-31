from regex import return_output
import subprocess
def ready_data(ifconfig):

    seperate = return_output(ifconfig)

    seperated = seperate.split("\n")
    filtered = list(filter(None,seperated))

    result = {}
    network_config = ''
    rx_errors = 0
    tx_errors = 0

    for line in filtered:
        if line.startswith('Network configuration:'):
            network_config = line.split(': ')[1]
        elif line.startswith('RX errors:'):
            parts = line.split()
            if len(parts) >= 5:
                try:
                    rx_errors = int(parts[4])
                except ValueError:
                    print(f"Error parsing RX errors in line: {line}")
            else:
                print(f"Invalid format for RX errors in line: {line}")
        elif line.startswith('TX errors:'):
            parts = line.split()
            if len(parts) >= 5:
                try:
                    tx_errors = int(parts[4])
                except ValueError:
                    print(f"Error parsing TX errors in line: {line}")
            else:
                print(f"Invalid format for TX errors in line: {line}")

            result[network_config] = {
                'RX errors': rx_errors,
                'TX errors': tx_errors
            }


    return(result)
# print(seperated)