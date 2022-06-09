#Converting decimal number into Binary Numbers

def decimal_to_binary(n):
    return bin(n).replace("0b", "")

decimal_number = int (input("Enter Decimal number : "))
binary_number = decimal_to_binary(decimal_number)
print(binary_number)
