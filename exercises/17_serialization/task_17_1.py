# -*- coding: utf-8 -*-
"""
Задание 17.1

Создать функцию write_dhcp_snooping_to_csv, которая обрабатывает вывод
команды show dhcp snooping binding из разных файлов и записывает обработанные
данные в csv файл.

Аргументы функции:
* filenames - список с именами файлов с выводом show dhcp snooping binding
* output - имя файла в формате csv, в который будет записан результат

Функция ничего не возвращает.

Например, если как аргумент был передан список с одним файлом sw3_dhcp_snooping.txt:
MacAddress          IpAddress        Lease(sec)  Type           VLAN  Interface
------------------  ---------------  ----------  -------------  ----  --------------------
00:E9:BC:3F:A6:50   100.1.1.6        76260       dhcp-snooping   3    FastEthernet0/20
00:E9:22:11:A6:50   100.1.1.7        76260       dhcp-snooping   3    FastEthernet0/21
Total number of bindings: 2

В итоговом csv файле должно быть такое содержимое:
switch,mac,ip,vlan,interface
sw3,00:E9:BC:3F:A6:50,100.1.1.6,3,FastEthernet0/20
sw3,00:E9:22:11:A6:50,100.1.1.7,3,FastEthernet0/21

Первый столбец в csv файле имя коммутатора надо получить из имени файла,
остальные - из содержимого в файлах.

Проверить работу функции на содержимом файлов sw1_dhcp_snooping.txt,
sw2_dhcp_snooping.txt, sw3_dhcp_snooping.txt.

"""
import csv
import re
import glob

def write_dhcp_snooping_to_csv(filenames, output):
    regex = '(?P<mac>[\w:]+\d+) +(?P<ip>\S+) +\d+ +\D+ +(?P<vlan>\d+) +(?P<intf>FastEthernet\S+)'
    with open(output, 'w') as dest:
        writer = csv.writer(dest)
        writer.writerow(['switch', 'mac', 'ip', 'vlan', 'interface'])
        for filename in filenames:
            sw = re.search(r'(\S+)_dhcp_snooping', filename).group(1)
            with open(filename) as f:
                for line in f:
                    match = re.search(regex, line)
                    if match:
                        writer.writerow([sw] + list(match.groups()))

if __name__ == '__main__':
    files = glob.glob('*dhcp_snooping*')
    files.sort()
    write_dhcp_snooping_to_csv(files, 'task_17_1.csv')

with open('task_17_1.csv') as ff:
    print(ff.read())


'''
def write_dhcp_snooping_to_csv(filenames, output):
    filename = glob.glob(filenames)
    result = []
    #sw = [filenames[z].split('_')[0] for z in range(len(filenames))]
    #sw.sort()
    sw = filename[0].split('_')[0]
    regex = '(?P<mac>[\w:]+\d+) +(?P<ip>\S+) +\d+ +\D+ +(?P<vlan>\d+) +(?P<intf>FastEthernet\S+)'
    headers = ['switch', 'mac', 'ip', 'vlan', 'interface']
    with open(filenames) as f:
        match = re.finditer(regex, f.read())
        temp = [list(m.groups()) for m in match]
        for n in range(len(temp)):
            temp[n].insert(0, sw)
        result.append(headers)
        result = result + temp
    with open(output, 'w') as d:
        writer = csv.writer(d)
        for row in result:
            writer.writerow(row)

if __name__ == '__main__':
    write_dhcp_snooping_to_csv('sw1_dhcp_snooping.txt', 'task_17_1.csv')

with open('task_17_1.csv') as ff:
    print(ff.read())
'''