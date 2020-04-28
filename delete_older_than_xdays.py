import os
import sys
import datetime
req_path=input("Enter the path:")
age=0
if not os.path.exists(req_path):
        print("please provide valid path")
        sys.exit(1)
if os.path.isfile(req_path):
    print(" Please provide valid directroy path")
    sys.exit(2)
today=datetime.datetime.now()
#print(os.listdir(req_path))
for each_file in os.listdir(req_path):
    each_file_path=os.path.join(req_path,each_file)
    #print(each_file_path)
    if os.path.isfile(each_file_path):
        file_cre_date=datetime.datetime.fromtimestamp(os.path.getctime(each_file_path))
        #print(dir(file_cre_date))
        #print(file_cre_date)
        dif_days=(today-file_cre_date).days
        #print(dif_days)
        if dif_days >= age:
            #rm_f=print(each_file_path,dif_days)
            print(each_file_path)
            print(os.remove(each_file_path))


