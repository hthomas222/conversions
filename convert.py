def binary_conversion(conversion_1, num):
    if conversion_1 == "decimal":
        bnum = bin(int(num))
        print(bnum)
    elif conversion_1 == "octal":
        bnum = bin(int(str(num), 8))
        print(bnum)
    elif conversion_1 == "hexadecimal":
        int_val = int(num, 16)
        bnum = bin(int_val)[2:]
        print(bnum)





# main:
conversion_1 = input("What is the type your current number is using: ")
num = input("Please enter a number: ")
conversion_2 = input("Please enter the type you want to convert to: ")
if conversion_2 == "binary":
    binary_conversion(conversion_1, num)
# elif conversion_2 == "hexadecimal":
#     hexadecimal_conversion(num)
# elif conversion_2 == "octal":
#     octal_conversion()
# else:
#     decimal_conversion()


