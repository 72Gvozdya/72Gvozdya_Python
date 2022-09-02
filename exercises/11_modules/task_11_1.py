# -*- coding: utf-8 -*-
"""
Задание 11.1

Создать функцию parse_cdp_neighbors, которая обрабатывает
вывод команды show cdp neighbors.

У функции должен быть один параметр command_output, который ожидает как аргумент
вывод команды одной строкой (не имя файла). Для этого надо считать все содержимое
файла в строку, а затем передать строку как аргумент функции (как передать вывод
команды показано в коде ниже).

Функция должна возвращать словарь, который описывает соединения между устройствами.

Например, если как аргумент был передан такой вывод:
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0

Функция должна вернуть такой словарь:

    {("R4", "Fa0/1"): ("R5", "Fa0/1"),
     ("R4", "Fa0/2"): ("R6", "Fa0/0")}

В словаре интерфейсы должны быть записаны без пробела между типом и именем.
То есть так Fa0/0, а не так Fa 0/0.

Проверить работу функции на содержимом файла sh_cdp_n_sw1.txt. При этом функция должна
работать и на других файлах (тест проверяет работу функции на выводе
из sh_cdp_n_sw1.txt и sh_cdp_n_r3.txt).

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
from pprint import pprint
def parse_cdp_neighbors(command_output):
    """
    Тут мы передаем вывод команды одной строкой потому что именно в таком виде будет
    получен вывод команды с оборудования. Принимая как аргумент вывод команды,
    вместо имени файла, мы делаем функцию более универсальной: она может работать
    и с файлами и с выводом с оборудования.
    Плюс учимся работать с таким выводом.
    """
    result = {}
   # result_template = '''({}, {})'''
    lines = [stroke.strip() for stroke in command_output.split('\n')]
    #result = {rec: [] for rec in paramlist}
    for line in lines:
        columns = line.split()
        if '>' in line:
            hostname = line.split('>')[0]
        if len(columns) > 7 and columns[3].isdigit():
            device, loc_int_name, loc_int_num, *other, port_name, port_num = columns
            tuple1 = (hostname, loc_int_name + loc_int_num)
            tuple2 = (device, port_name + port_num)
            result[tuple1] = tuple2
            #result[hostname, loc_int_name + loc_int_num] = result_template.format(device, port_name + port_num)
    return result

if __name__ == "__main__":
    with open("sh_cdp_n_r3.txt") as f:
        pprint(parse_cdp_neighbors(f.read()))

#sh_cdp_n_r3.txt
#sh_cdp_n_sw1.txt