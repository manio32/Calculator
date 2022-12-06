import time

num = input().split()

num1 = num[0]
value = num[1]
num2 = num[2]

if value == "+":
    print(int(num1) + int(num2))
    time.sleep(300)
elif value == "-":
    print(int(num1) - int(num2))
    time.sleep(300)
elif value == "*":
    print(int(num1) * int(num2))
    time.sleep(300)
elif value == "/":
    print(int(num1) / int(num2))
    time.sleep(300)