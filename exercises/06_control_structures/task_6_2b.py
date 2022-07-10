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
#correct_ip = False
while True:
    ip = input("Введите IP адрес в формате 10.0.1.1: ")
    octets = ip.split('.')
    correct_ip = True
    if len(octets) != 4:
        correct_ip = False
    else:
        for i in octets:
            if not (i.isdigit() and int(i) in range(256)):
                correct_ip = False
                break
    if not correct_ip:
        print('Неправильный IP-адрес')
    else:
        break

oct1 = int(ip.split('.')[0])
if 1 <= oct1 <= 223:
    print("unicast")
elif 223 < oct1 < 240:
    print("multicast")
elif ip == '255.255.255.255':
    print("local broadcast")
elif ip == '0.0.0.0':
    print("unassigned")
else:
    print("unused")