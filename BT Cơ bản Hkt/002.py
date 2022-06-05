#Ting tong hai so nguyen(Co xu ly ngoai le dau vao)

value1 = input() #Nhap gia tri thu nhat
value2 = input() #Nhap gia tri thu hai
try: #Khoi lenh co the phat sinh loi
    num1=int(value1) #Ep kieu sang so nguyen
    num2=int(value2) #Ep kieu sang so nguyen
    sum = num1 + num2 #Tinh tong
    print("The sum of two numbers:", sum) #in ra man hinh
except: #Khoi lenh duoc thuc thi khi loi xay ra
    print("Invalid")