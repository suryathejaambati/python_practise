'''
num=eval(input("Enter your number: "))
if num==1:
    print("one")
if num==2:
    print("two")
if num==3:
    print("three")
if num==4:
    print("four")
if num==5:
    print("five")
if num==6:
    print("six")
if num==7:
    print("seven")
if num==8:
    print("eight")
if num==9:
    print("nine")
if num==10:
    print("ten")
'''
'''
num=eval(input("Enter your number: "))
if num==1:
    print("one")
elif num==2:
    print("two")
elif num==3:
    print("three")
elif num==4:
    print("four")
elif num==5:
    print("five")
elif num==6:
    print("six")
elif num==7:
    print("seven")
elif num==8:
    print("eight")
elif num==9:
    print("nine")
elif num==10:
    print("ten")

'''
'''
num=eval(input("Enter your number: "))
if num==1:
    print("one")
elif num==2:
    print("two")
elif num==3:
    print("three")
elif num==4:
    print("four")
elif num==5:
    print("five")
elif num==6:
    print("six")
elif num==7:
    print("seven")
elif num==8:
    print("eight")
elif num==9:
    print("nine")
elif num==10:
    print("ten")
else:
    print("The number is out of range please choose 1-10 range")
'''

num=eval(input("Enter your number: "))
num_word={1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten'}
if num in [1,2,3,4,5,6,7,8,9,10]:
    print(num_word.get(num))
else:
    print("The number is out of range please choose 1-10 range")

    
