import re
import pprint
mac_address_table = open('CAM_table.txt').read()
#print(mac_address_table)
findalll = re.findall(r'(\d+) +(\S+) +\w+ +\S+', mac_address_table)