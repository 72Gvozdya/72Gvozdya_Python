# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт: Если адрес был введен неправильно, запросить адрес снова.

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'
Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""


while True:
    ip = input("Введите IP-адрес: ")
    octs = ip.split('.')
    valid_ip = True

    if len(octs) == 4:
        for x in octs:
            if not x.isdigit() or not 0 <= int(x) <= 255:
                valid_ip = False
                break
    else:
        valid_ip = False
    if valid_ip:
        break
    print("Неправильный IP-адрес")


if 1<= int(octs[0]) <=223:
    print('unicast')
elif 224 <= int(octs[0]) <= 239:
    print('multicast')
elif ip == '255.255.255.255':
    print('local broadcast')
elif ip == '0.0.0.0':
    print('unassigned')
else:
    print('unused')

