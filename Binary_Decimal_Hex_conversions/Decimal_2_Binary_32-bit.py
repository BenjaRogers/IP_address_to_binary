def main():
    ip_address = get_ip_address()
    ip_address = ip_address.split('.')
    binary_address = decimal_to_binary(ip_address)
    print(turn_to_string(binary_address))

def turn_to_string(binary_address):
    binary_address_list = [str(bit) for bit in binary_address]
    for i in range(len(binary_address_list)):
        if i in [8, 17, 26]:
            binary_address_list.insert(i, '.')
    binary_address_string = ''
    binary_address_string = binary_address_string.join(binary_address_list)
    return binary_address_string

def get_ip_address():
    ip_address = input("Enter IP Address (format XXX.XXX.XXX.XXX): ")
    return ip_address

def decimal_to_binary(ip_address):
    binary_address = []
    position_value = [128, 64, 32, 16, 8, 4, 2, 1]
    for section in ip_address:
        section = int(section)
        for value in position_value:
            if section - value >= 0:
                section -= value
                binary_address.append(1)
            else:
                binary_address.append(0)
    return binary_address

main()
