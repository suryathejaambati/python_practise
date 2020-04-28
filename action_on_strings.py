
'''
usr_str=input("Enter the string: ")
usr_conf=input("Enter action on your string (valid actions are: lower/upper/title) : ")
'''
'''
import sys
print(f"The no of commad line arguments: ",len(sys.argv))
if len(sys.argv) != 3
sys.exit()
usr_str=sys.argv[1]
usr_conf=sys.argv[2]
if usr_conf=="lower":
    print(usr_str.lower())
elif usr_conf=="upper":
    print(usr_str.upper())
elif usr_conf=="title":
    print(usr_str.title())
else:
   print("your entered string is invalid")

'''

import sys
print(f"The no of commad line arguments: ",len(sys.argv))
if len(sys.argv) != 3:
    print("Usage : ")
    print(f" {sys.argv[0]} <your_require_string> <lower|upper|title> ")
    sys.exit()
usr_str=sys.argv[1]
usr_conf=sys.argv[2]
if usr_conf=="lower":
    print(usr_str.lower())
elif usr_conf=="upper":
    print(usr_str.upper())
elif usr_conf=="title":
    print(usr_str.title())
else:
   print("your entered string is invalid")


