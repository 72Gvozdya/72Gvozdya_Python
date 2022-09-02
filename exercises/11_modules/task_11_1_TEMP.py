from pprint import pprint
columns = []
result = {}
result_template = '''({}, {})'''
with open('sh_cdp_n_r3.txt') as f:
    command_output = f.read()
    lines = [stroke.strip() for stroke in command_output.split('\n')]
    for line in lines:
        columns = line.split()
        if '>' in line:
            hostname = line.split('>')[0]
        if len(columns) > 7 and columns[3].isdigit():
            device, loc_int_name, loc_int_num, *other, port_name, port_num = columns
            tuple1 = (hostname, loc_int_name + loc_int_num)
            tuple2 = (device, port_name + port_num )
            #result[tuple1] = tuple2
            result[hostname, loc_int_name + loc_int_num] = result_template.format(device, port_name + port_num)
    pprint(result)

#sh_cdp_n_r3.txt
#sh_cdp_n_sw1.txt