# -*- coding: utf-8 -*-
"""
Задание 5.3a

Дополнить скрипт из задания 5.3 таким образом, чтобы, в зависимости
от выбранного режима, задавались разные вопросы в запросе о номере
VLANа или списка VLANов:
* для access: 'Введите номер VLAN:'
* для trunk: 'Введите разрешенные VLANы:'

Ограничение: Все задания надо выполнять используя только пройденные темы.
То есть эту задачу можно решить без использования условия if и циклов for/while.
"""

access_template = [
    "switchport mode access",
    "switchport access vlan {}",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

trunk_template = [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan {}",
]

template = {"access": access_template, "trunk": trunk_template}
templvlan = {"access": "Введите номер VLAN: ", "trunk": "Введите разрешенные VLANы: "}
#{"access": "Введите номер VLAN: ", "trunk": "Введите разрешенные VLANы: "}
intmode = input("Введите режим интефейса (access/trunk): ")
intnum = input("Введите номер интерфейса (тип и номер, вида Gi0/3): ")
vlans = input(templvlan[intmode])
print('\ninterface {0}'.format(intnum))
print(('\n').join(template[intmode]).format(vlans))
