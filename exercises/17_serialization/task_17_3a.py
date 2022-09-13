# -*- coding: utf-8 -*-
"""
Задание 17.3a

Создать функцию generate_topology_from_cdp, которая обрабатывает вывод
команды show cdp neighbor из нескольких файлов и записывает итоговую
топологию в один словарь.

Функция generate_topology_from_cdp должна быть создана с параметрами:
* list_of_files - список файлов из которых надо считать вывод команды sh cdp neighbor
* save_to_filename - имя файла в формате YAML, в который сохранится топология.
 * значение по умолчанию - None. По умолчанию, топология не сохраняется в файл
 * топология сохраняется только, если save_to_filename как аргумент указано имя файла

Функция должна возвращать словарь, который описывает соединения между устройствами,
независимо от того сохраняется ли топология в файл.

Структура словаря должна быть такой:
{'R4': {'Fa 0/1': {'R5': 'Fa 0/1'},
        'Fa 0/2': {'R6': 'Fa 0/0'}},
 'R5': {'Fa 0/1': {'R4': 'Fa 0/1'}},
 'R6': {'Fa 0/0': {'R4': 'Fa 0/2'}}}

Интерфейсы должны быть записаны с пробелом. То есть, так Fa 0/0, а не так Fa0/0.

Проверить работу функции generate_topology_from_cdp на списке файлов:
* sh_cdp_n_sw1.txt
* sh_cdp_n_r1.txt
* sh_cdp_n_r2.txt
* sh_cdp_n_r3.txt
* sh_cdp_n_r4.txt
* sh_cdp_n_r5.txt
* sh_cdp_n_r6.txt

Проверить работу параметра save_to_filename и записать итоговый словарь
в файл topology.yaml. Он понадобится в следующем задании.

"""
import re
import glob
import yaml
from pprint import pprint

def generate_topology_from_cdp(list_of_files, save_to_filename=None):
    regex = r'(?P<r_dev>\S+) +(?P<intf>Eth \S+) +\d+ +(\S )+.+?(?P<port>Eth \S+)'
    result = {}
    for file in list_of_files:
        l_dev = re.search(r'sh_cdp_n_(\S+)\.', file).group(1).upper()
        result[l_dev] = {}
        with open(file) as f:
            match = re.finditer(regex, f.read(), re.DOTALL)
            for m in match:
                r_dev, intf, port = m.group('r_dev', 'intf', 'port')
                result[l_dev][intf] = {r_dev: port}
    if save_to_filename:
        with open(save_to_filename, 'w') as dest:
            yaml.dump(result, dest)
    return(result)

if __name__ == '__main__':
    files = glob.glob('sh_cdp_n*')
    generate_topology_from_cdp(files, 'task_17_3.yaml')
   # print(generate_topology_from_cdp(files))
    with open('task_17_3.yaml') as ff:
        temp = yaml.safe_load(ff)
        pprint(temp)