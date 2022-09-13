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
import ipaddress
ips = ['8.8.8.8', '8.8.4.4', '192.168.1.1', '192.168.0.1']

def ping_ip_addresses(ip_list):
    acc_ip = []
    unacc_ip = []
    for ip in ip_list:
        #ip = ipaddress.ip_address(ip)
        reply = subprocess.run(['ping', '-c', '1', '-n', ip], stdout = subprocess.DEVNULL, stderr = subprocess.DEVNULL)
        if reply.returncode == 0:
            acc_ip.append(ip)
        else:
            unacc_ip.append(ip)

    return acc_ip, unacc_ip

if __name__ == '__main__':
    print(ping_ip_addresses(ips))

