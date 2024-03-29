# -*- coding: utf-8 -*-
"""
Задание 9.3

Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный
файл коммутатора и возвращает кортеж из двух словарей:
* словарь портов в режиме access, где ключи номера портов,
  а значения access VLAN (числа):
{'FastEthernet0/12': 10,
 'FastEthernet0/14': 11,
 'FastEthernet0/16': 17}

* словарь портов в режиме trunk, где ключи номера портов,
  а значения список разрешенных VLAN (список чисел):
{'FastEthernet0/1': [10, 20],
 'FastEthernet0/2': [11, 30],
 'FastEthernet0/4': [17]}

У функции должен быть один параметр config_filename, который ожидает как аргумент
имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
#from sys import argv
#config_filename
def get_int_vlan_map(config_filename):
    access_dic = {}
    trunk_dic = {}
    with open (config_filename) as f:
        for line in f:
            if line.startswith('interface'):
                intf = line.split(' ')[-1].strip()
            elif 'access vlan' in line:
                vlan = line.split(' ')[-1].strip()
                access_dic[intf] = int(vlan)
            elif 'allowed vlan' in line:
                vlans = line.split(' ')[-1].strip().split(',')
                intvlans = [int(x) for x in vlans]
                trunk_dic[intf] = intvlans
    return(access_dic, trunk_dic)

#get_int_vlan_map('config_sw1.txt')