# -*- coding: utf-8 -*-
"""
Задание 7.1

Обработать строки из файла ospf.txt и вывести информацию по каждой строке в таком
виде на стандартный поток вывода:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

print('{:22}'.format('Prefix') + '{:<15}'.format(line[1]))
        print('{:22}'.format('AD/Metric') + '{:<15}'.format(line[2]))
        print('{:22}'.format('Next-Hop') + '{:<15}'.format(line[4]))
        print('{:22}'.format('Last update') + '{:<15}'.format(line[5]))
        print('{:22}'.format('Outbound Interface') + '{:15}'.format(line[6]))

"""
result = {}
with open('ospf.txt', 'r') as f:
    for line in f:
        line = line.replace(',', '')
        line = line.replace(']', '')
        line = line.replace('[', '')
        line = line.split()
        print('{:22}'.format('Prefix') + '{:<15}'.format(line[1]))
        print('{:22}'.format('AD/Metric') + '{:<15}'.format(line[2]))
        print('{:22}'.format('Next-Hop') + '{:<15}'.format(line[4]))
        print('{:22}'.format('Last update') + '{:<15}'.format(line[5]))
        print('{:22}'.format('Outbound Interface') + '{:15}'.format(line[6]))

