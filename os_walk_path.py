import os
path="/home/ec2-user/sury"
'''
print(list(os.walk(path)))
#print(os.walk(path))
for each in os.walk(path):
    print(each)
'''

#for r,d,f in os.walk(path,topdown=False):
for r,d,f in os.walk(path):
    if len(f)!=0:
        print(r)
    for each_file in f:
        print(os.path.join(r,each_file))

