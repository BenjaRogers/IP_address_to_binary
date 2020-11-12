
def main():
    binary_address = "11000110.10101000.00000010.00000001".split('.')
    decimal_address_list = convert_to_decimal(binary_address)
    print(turn_to_string(decimal_address_list))
    
def get_binary_address():
    binary_address = input("Enter the 32 bit binary number in the following"
                           " format(XXXXXXXX.XXXXXXXX.XXXXXXXX.XXXXXXXX): ").split('.')
    return binary_address

def convert_to_decimal(binary_address):
    decimal_address = []
    binary_address_list = [list(octet) for octet in binary_address]
    position_value = [128, 64, 32, 16, 8, 4, 2, 1]
    for i in binary_address_list:
        num = 0
        for j in range(len(i)):
            if i[j] == '1':
                num += position_value[j]
            if i[j] == '0':
                pass
        decimal_address.append(num)
    return decimal_address

def turn_to_string(decimal_adress):
    decimal_address_list = [str(num) for num in decimal_adress]
    for i in range(len(decimal_address_list) + 3):
        if i in [1, 3, 5]:
            decimal_address_list.insert(i, '.')
    decimal_address_string = ''
    decimal_address_string = decimal_address_string.join(decimal_address_list)
    return decimal_address_string

main()