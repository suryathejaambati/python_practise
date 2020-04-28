'''
import getpass
db_pass=getpass.getpass()
#print("Entered password:{db_pass}")
print(f"entered your password: {db_pass}")


'''

import getpass
db_user=getpass.getuser()
db_pass=getpass.getpass(prompt="Enter your dbpasswd: ")
print(f"user is: {db_user}")
print(f"Entered your db password is : {db_pass}")

