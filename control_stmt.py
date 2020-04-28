'''
import sys
print("before exit")
sys.exit()
print("after exit")
'''
'''
for each in [3,4,5]:
    print(each)
    break
print("After loop")
'''
'''
for each in [3,65,78,"surya",99]:
    print(each)
    if each==78:
        break
print("AFTER loop")
'''

'''
path=['/usr/bin','/usr/httpd','/usr/httpd/bin','/home/ec2-user']
for each_path in path:
    print("now working on each path is: ",each_path)
    if "httpd" in each_path:
        print(each_path)
        break

print("Outside of the loop")

'''
cnt=1
while True:
    print(cnt)
    if cnt==100:
        break
    cnt=cnt+1



