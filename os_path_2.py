import os
#path="/home/ec2-user/sury/test.py"

path=input("Enter the path: ")
print(os.path.basename(path))
print(os.path.dirname(path))

if os.path.exists(path):
    print(f"{path} is exists")
else:
    pritn(f"{path} is not exists")

if os.path.isfile(path):
    print(f"{path} is file")
else: 
    print(f"{path} is a dir")
'''
if os.path.isdir(path):
    print(f"{path} is file")
else
    print(f"{path} is not file")
'''
