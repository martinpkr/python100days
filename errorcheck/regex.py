import subprocess
import re
def return_output(ifconfig):
    # Run the 'ifconfig' command and capture the output

    # Define the regex patterns for network configuration name, RX errors, and TX errors
    network_pattern = r'^([^\s:]+)'
    rx_errors_pattern = r'RX errors.*'
    tx_errors_pattern = r'TX errors.*'

    # Split the output into individual instances based on double newline
    instances = ifconfig.strip().split('\n\n')
    list = []
    # Process each instance
    for instance in instances:
        # Find the network configuration name
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


    joined_list = "\n".join(list)
    return list,network_name,rx_error_number,tx_error_number