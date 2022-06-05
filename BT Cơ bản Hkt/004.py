"""
In ra dinh dang dau ra cua mot so nhu :
Binary(He nhi phan 0-1): 
Decimal(He thap phan(10)): %d 
Octal(He 8): %o
Hexadecimal(He 16): %x
print("%..." %(...))
"""


def decimal_to_binary(num):
    bin_lst = []
    bin_str = ""
    while num > 0:
        i = num % 2 #chia lay phan du
        bin_lst.append(i) #them phan tu vao list
        num = num // 2 #chia lay phan nguyen
    bin_lst.reverse() #dao nguoc list
    for k in bin_lst: 
        bin_str += str(i) #chuyen tu list sang xau
    #print(bin_lst)
    return bin_str
    

value1 = int(input())
print(decimal_to_binary(value1))
