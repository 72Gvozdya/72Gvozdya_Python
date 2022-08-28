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

"""
with open('ospf.txt', 'r') as f:
    for line in f:
        line = line.strip().split()
        print(f'{"Prefix":<22}' + f'{line[1]}')
        print(f'{"AD/Metric":<22}' + f'{line[2].strip("[]")}')
        print(f'{"Next-Hop":<22}' + f'{line[4].rstrip(",")}')
        print(f'{"Last update":<22}'  + f'{line[5].rstrip(",")}')
        print(f'{"Outbound Interface":<22}' + f'{line[6]}' + '\n')
