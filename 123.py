import re
import glob
filenames = ['sw1_dhcp_snooping.txt, sw2_dhcp_snooping.txt, sw3_dhcp_snooping.txt.']
for filename in filenames:
    sw = re.search(r'(\S+)_dhcp_snooping', filename).group(1)

filenames = glob.glob('*_dhcp_snooping*')