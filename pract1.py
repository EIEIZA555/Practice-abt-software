#Find Odd or Even and then find prime number
def is_prime(n):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
x=0
y=[]
for i in range(5):
    x=int(input("Enter 5 number: "))
    y.append(x)
for i in range(5):
    if (y[i]%2==0):
        print(y[i],"is Odd")
    else :
        print(y[i],"is Even")
for i in range(5):
    if is_prime(y[i]):
        print(y[i], "is a Prime number")
    else:
        print(y[i], "is Not a Prime number")
print("Day 3")