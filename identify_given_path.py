import os
import sys
path=input(" Enter the path: ")
if os.path.exists(path):
    df_l=os.listdir(path)
else:
    print(" Please provide valid path")
    sys.exit()

print(df_l)
p1=os.path.join(path,df_l[0])
p2=os.path.join(path,df_l[1])

if os.path.isfile(p1):
    print(f"{p1} is file")
else:
    print(f"{p1} is directory")

if os.path.isfile(p2):
    print(f"{p2} is file")
else:
    print(f"{p2} is directory")


    
