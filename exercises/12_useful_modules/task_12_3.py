# -*- coding: utf-8 -*-
"""
Задание 12.3

Создать функцию print_ip_table, которая отображает таблицу доступных
и недоступных IP-адресов.

Функция ожидает как аргументы два списка:
* список доступных IP-адресов
* список недоступных IP-адресов

Результат работы функции - вывод на стандартный поток вывода таблицы вида:

Reachable    Unreachable
-----------  -------------
10.1.1.1     10.1.1.7
10.1.1.2     10.1.1.8
             10.1.1.9

"""
#import subprocess
from tabulate import tabulate
'''
def print_ip_table(listip):
    table = {}
    reachadd = []
    unreachadd = []
    for addr in listip:
        reply = subprocess.run(['ping', '-c', '3', '-n', addr])
        if reply.returncode == 0:
            reachadd.append(addr)
            table['Reachable'] = reachadd
        else:
            unreachadd.append(addr)
            table['Unreachable'] = unreachadd
    return table
'''
def print_ip_table(reach_ip, unreach_ip):
    table = {'Reachable': reach_ip, 'Unreachable': unreach_ip}
    print(tabulate(table, headers = 'keys'))



if __name__ == "__main__":
    reach_ip = ['10.1.1.1', '10.1.1.2']
    unreach_ip = ['10.1.1.7', '10.1.1.8', '10.1.1.9']
    print_ip_table(reach_ip, unreach_ip)
#    columns = ['Reachable', 'Unreachable']
    #print(tabulate(print_ip_table(['8.8.8.8', '8.8.4.4', '192.168.1.1']), headers = 'keys'))
    #print(print_ip_table(['8.8.8.8', '8.8.4.4', '192.168.1.1']))