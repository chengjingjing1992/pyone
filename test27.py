##coding=utf-8
def is_ip(ip):
    num_list = ip.split(".")
    for num in num_list:
        if not num.isdigit() or not 0 <= int(num) <=255:
            return False
    return True

print(is_ip("101.1.0.201"))