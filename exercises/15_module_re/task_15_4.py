# -*- coding: utf-8 -*-
"""
Задание 15.4

Создать функцию get_ints_without_description, которая ожидает как аргумент
имя файла, в котором находится конфигурация устройства.

Функция должна обрабатывать конфигурацию и возвращать список имен интерфейсов,
на которых нет описания (команды description).

Пример итогового списка:
["Loopback0", "Tunnel0", "Ethernet0/1", "Ethernet0/3.100", "Ethernet1/0"]

Пример интерфейса с описанием:
interface Ethernet0/2
 description To P_r9 Ethernet0/2
 ip address 10.0.19.1 255.255.255.0
 mpls traffic-eng tunnels
 ip rsvp bandwidth

Интерфейс без описания:
interface Loopback0
 ip address 10.1.1.1 255.255.255.255

Проверить работу функции на примере файла config_r1.txt.
"""
import re
def get_ints_without_description(file):
    result = []
    regex = "!\ninterface (?P<intf>\S+)\n (?P<desc>description)?"
    with open(file) as f:
        match = re.finditer(regex, f.read())
        for m in match:
            if m.lastgroup == 'intf':
                result.append(m.group('intf'))

        #result = [m.group('intf') for m in match if m.lastgroup == 'intf']
        #match = re.finditer(regex, f.read())
        #result = [m.group('intf') for m in match if m.lastgroup == 'intf']
    return result

if __name__ == '__main__':
    print(get_ints_without_description('config_r1.txt'))