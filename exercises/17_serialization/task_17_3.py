# -*- coding: utf-8 -*-
"""
Задание 17.3

Создать функцию parse_sh_cdp_neighbors, которая обрабатывает
вывод команды show cdp neighbors.

Функция ожидает, как аргумент, вывод команды одной строкой (не имя файла).
Функция должна возвращать словарь, который описывает соединения между устройствами.

Например, если как аргумент был передан такой вывод:
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0

Функция должна вернуть такой словарь:
{'R4': {'Fa 0/1': {'R5': 'Fa 0/1'},
        'Fa 0/2': {'R6': 'Fa 0/0'}}}

Интерфейсы должны быть записаны с пробелом. То есть, так Fa 0/0, а не так Fa0/0.
{'SW1': {'Eth 0/1': {'R1': 'Eth 0/0'},
         'Eth 0/2': {'R2': 'Eth 0/0'},
         'Eth 0/3': {'R3': 'Eth 0/0'},
         'Eth 0/4': {'R4': 'Eth 0/0'}}}

Проверить работу функции на содержимом файла sh_cdp_n_sw1.txt
"""
import csv
import re

def parse_sh_cdp_neighbors(command):
    result = {}
    temp = {}
    sw = re.search(r'(\S+)>', command).group(1)
    regex = (r'(?P<dev>\S\d) +(?P<intf>Eth \S+) +\d+ +\S \S \S +\d+ +(?P<port>Eth \S+)')
    match = re.finditer(regex, command, re.DOTALL)
    for m in match:
        temp.update({m.group('intf'): {m.group('dev'): m.group('port')}})
        result[str(sw)] = temp
    return(result)

if __name__ == '__main__':
    with open('sh_cdp_n_sw1.txt') as f:
        stroke = f.read()
    print(parse_sh_cdp_neighbors(stroke))

'''
  connect_dict = {}
    l_dev = re.search(r"(\S+)[>#]", command_output).group(1)
    connect_dict[l_dev] = {}
    for match in regex.finditer(command_output):
        r_dev, l_intf, r_intf = match.group("r_dev", "l_intf", "r_intf")
        connect_dict[l_dev][l_intf] = {r_dev: r_intf}
    return connect_dict
'''