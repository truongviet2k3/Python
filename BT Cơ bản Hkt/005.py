"""Chuyen tu he co so 10 sang he co so 8(Co xu ly ngoai le dau vao)
    try:
        ...
    expect:
        ...
"""
def decimal_to_octal(num_10):
    octal_lst = []
    octal_str = ""
    while num_10 > 0:
        i = num_10 % 8
        octal_lst.append(i)
        num_10 = num_10 // 8
    octal_lst.reverse()
    for k in octal_lst:
        octal_str += str(k)
    return octal_str

value = input()
try:
    num_10 = int(value)
    num_8 = decimal_to_octal(num_10)
    print(f"He thap phan la {num_10} sang he co so 8:", num_8)
except:
    print("Invalid")
