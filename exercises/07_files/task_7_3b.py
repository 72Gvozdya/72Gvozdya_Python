# -*- coding: utf-8 -*-
"""
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Переделать скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Пример работы скрипта:

Enter VLAN number: 10
10       0a1b.1c80.7000      Gi0/4
10       01ab.c5d0.70d0      Gi0/8

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
template = "{:<9} {:<20} {}"
vlanlst = []
inputvlan = input( "Введите номер Vlan: ")
with open('CAM_table.txt', 'r') as f:
    for line in f:
        line = line.split()
        if line and line[0].isdigit() and line[0] == inputvlan:
            line[0] = int(line[0])
            vlan, mac, _, ports = line
            vlanlst.append([vlan, mac, ports])
            #print(template.format(str[0], str[1], str[3]))
            #vlan, mac, _, ports = str
            #print(f'{vlan:9}{mac:20}{ports}')
    vlanlst = sorted(vlanlst)
    for vlan, mac, ports in vlanlst:
        print(template.format(vlan, mac, ports))