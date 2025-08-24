
print("Choose a task: \n \t1. Binary to Decimal \n \t2. Decimal to Binary \n")
task = input('Enter your choice (1/2): ')

def dec_to_bn(num):
    return "Binary: {}".format(bin(int(num))[2:])

def bn_to_dec(num):
    new_chr = []
    rev_num = num[::-1]
    i=0
    for char in rev_num:
        if char == '1':
            new_chr.append(2**i)
            #print(new_chr)
        else:
            pass
        i+=1
    #return "Decimal: {}".format(bin(num)[2:])
    return f"Decimal: {sum(new_chr)}"

if task == '1':
    num = input("Enter the binary number: ")
    print(bn_to_dec(num))
else:
    num = input("Enter the decimal number: ")
    print(dec_to_bn(num))
