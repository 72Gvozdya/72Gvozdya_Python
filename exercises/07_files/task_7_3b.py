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
word2 = []
with open('CAM_table.txt', 'r') as f:
    for line in f:
        word = line.split()
        if word and word[0].isdigit():
            vlan, mac, _, interf = word
            word2.append([int(vlan), mac, interf])
            #print(word)
    vlan2 = int(input('Введите № влан: '))
    for vlan, mac, interf in sorted(word2):
        if vlan == vlan2:
            print(f'{vlan:<9}{mac:20}{interf}')