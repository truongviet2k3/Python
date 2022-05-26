n = int(input())

def sumOfAll(n):
    s = 0
    for i in range (1,n):
        if n % i == 0:
            s += i
    return s
print(sumOfAll(n))