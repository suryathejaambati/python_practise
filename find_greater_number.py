'''
a=eval(input("Enter your first number: "))
b=eval(input("Enter your second number: "))
if a>b:
    print(f"{a} is greater than {b}")
else:
    print(f"{b} is greater than {a}")
'''

a=eval(input("Enter your first number: "))
b=eval(input("Enter your second number: "))
if a>b:
    print(f"{a} is greater than {b}")
elif a<b:
    print(f"{a} is less than {b}")
else:
    print(f"{a} and {b} are equal")


