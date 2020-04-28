'''
for each in [2,3,4,5]:
    print ("hello", each)

import os
path="/home/ec2-user/sury"
List_of_files=os.listdir(path)
#print(List_of_files)
for each_files_of_dir in List_of_files:
  #  print(each_files_of_dir)
    f.d.p=os.path.join(path,each_files_of_dir)
print(f.d.p)

'''


import os
import sys
path=input(" Enter the path: ")
if os.path.exists(path):
    df_l=os.listdir(path)
else:
    print(" Provide valid path")

list_of_files_dir=os.listdir(path)
print(" all files and dirs: ",list_of_files_dir)
for each_file_or_dir in list_of_files_dir:
    f_d_p=os.path.join(path,each_file_or_dir)
    if os.path.isfile(f_d_p):
        print(f"{f_d_p} is file")
    else:
        print(f"{f_d_p} is dir")

    
