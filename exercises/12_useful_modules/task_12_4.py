"""
Задание 12.4
Создать функцию find_n_ip.
Параметры функции:
* ip_from_range1 - IP-адрес из диапазона адресов range1
* range1 - диапазон IP-адресов вида "10.1.1.1-10.1.2.2"
* range2 - диапазон IP-адресов вида "10.2.2.100-10.2.3.101"
Функция должна определить каким адресом по счету является адрес ip_from_range1
в диапазоне range1. И найти такой же адрес по счету в диапазоне range2.
Функция должна возвращать найденный IP-адрес в виде строки "10.5.1.3"
Например, если передать функции find_n_ip такие аргументы:
new_ip = find_n_ip("10.1.1.17", "10.1.1.1-10.1.1.30", "50.1.1.1-50.1.1.20")
new_ip должен быть равен "50.1.1.17"
Если передать такие аргументы:
new_ip = find_n_ip("10.1.1.127", "10.1.1.100-10.1.2.200", "50.1.1.110-50.1.2.210")
new_ip должен быть равен "50.1.1.137"
"""


from ipaddress import ip_address

def find_n_ip(ip_from_range1, range1, range2):
    ip1 = ip_address(ip_from_range1)
    range_list = ('-').join([range1, range2]).split('-')
    start_ip1, end_ip1, start_ip2, end_ip2 = range_list
    start_ip1 = ip_address(start_ip1)
    end_ip1 = ip_address(end_ip1)
    ip = start_ip1
    i = 0
    while not ip1 == ip:
        ip = start_ip1 + i
        i = i + 1
    start_ip2 = ip_address(start_ip2)
    end_ip2 = ip_address(end_ip2)
    k = 0
    ip2 = start_ip2
    while not k == i:
        ip2 = start_ip2 + k
        k = k + 1
    return str(ip2)


if __name__ == '__main__':
    print(find_n_ip("10.1.1.17", "10.1.1.1-10.1.1.30", "50.1.1.1-50.1.1.20"))

