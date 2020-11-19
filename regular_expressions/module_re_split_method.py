import re

output = 'Interface IP-Address Method Status,Protocol     FastEthernet0/2 10.5.34.129 mac 1e01.345a.ee41'

def output_converter(original_string):
    regex = (r'[ ,]+')
    return re.split(regex, original_string)

print(output_converter(output))