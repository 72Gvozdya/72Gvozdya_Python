import re

groups = []
regex = (r"(?P<intf>^\S+) +(?P<ip>[\d.\w]+) +\S+ +\S+"
            r" +(?P<status>up|administratively down) +(?P<protocol>up|down)")
'''
with open('sh_ip_int_br.txt') as f:
    result = re.finditer(regex, f.read())
    for match in result:
        groups.append(match.groups())
'''
with open('sh_ip_int_br.txt') as f:
    for line in f:
        match = re.search(regex, line)
        if match:
            groups.append(match.groups())
