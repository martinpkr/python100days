import subprocess
import re
PATTERN_FOR_PARTS = r'^(.*?:)\s+(RX errors.*?)(TX errors.*)$'
class Check:
    def __init__(self):
        self.output = subprocess.check_output('ifconfig', text=True)

        self.configurations = re.split(r"\n(?=\w+:)", self.output.strip())
        self.split_parts = []
        print(self.output)
        for config in self.configurations:
            self.split_parts.append(config.strip().replace('\n', '').replace('\t', ''))

        for part in self.split_parts:
            matches = re.match(PATTERN_FOR_PARTS, part)
            network_name = matches.group(1).strip()
            rx_errors = matches.group(2).strip().replace('  ',' ')
            tx_errors = matches.group(3).strip().replace('  ',' ')

            print(network_name)
            print(rx_errors)
            print(tx_errors)