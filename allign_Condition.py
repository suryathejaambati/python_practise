
'''
import os
t_w=os.get_terminal_size().columns

given_str=input(" Enter your string: ")
print(given_str)
print(given_str.center(t_w))
print(given_str.ljust(t_w))
print(given_str.rjust(t_w))

'''
'''
import os
t_w=os.get_terminal_size().columns

given_str=input("Enter your string: ")
print(given_str)

if True:
    print(given_str.center(t_w))
if False:
    print(given_str.rjust(t_w))

'''
import os
t_w=os.get_terminal_size().columns
given_str=input("Enter your string: ")
print(given_str)
usr_conf=input("Do you want to allighn text: say yes or no ? ")
if usr_conf=="yes":
    print(given_str.center(t_w))
    print(given_str.ljust(t_w))
    print(given_str.rjust(t_w))



