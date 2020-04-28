import os
t_w=os.get_terminal_size().columns

given_str=input(" Enter your string: ")
print(given_str)
print(given_str.center(t_w))
print(given_str.ljust(t_w))
print(given_str.rjust(t_w))

