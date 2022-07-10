# -*- coding: utf-8 -*-
"""
Задание 12.1

Создать функцию ping_ip_addresses, которая проверяет пингуются ли IP-адреса.

Функция ожидает как аргумент список IP-адресов.

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте команду ping (запуск ping через subprocess).
IP-адрес считается доступным, если выполнение команды ping отработало с кодом 0 (returncode).
Нюансы: на Windows returncode может быть равен 0 не только, когда ping был успешен,
но для задания нужно проверять именно код. Это сделано для упрощения тестов.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
import subprocess
#ip_list = ['8.8.8.8', '8.8.4.4', '192.168.1.1', '192.168.0.1']

def ping_ip_addresses(listip):
    avadd = []
    unavadd = []
    for addr in listip:
        reply = subprocess.run(['ping', '-c', '3', '-n', addr])
        if reply.returncode == 0:
            avadd.append(addr)
        else: unavadd.append(addr)
    return avadd, unavadd

if __name__ == "__main__":
    print(ping_ip_addresses(['8.8.8.8', '8.8.4.4', '192.168.1.1']))