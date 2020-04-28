'''
my_content=["My name is suryatheja\n", " I want to b devops architect \n"," I am living in Bangalore \n"]
fo=open("new2.txt","w")
fo.writelines(my_content)
fo.close()
'''

'''
my_content=["My name is suryatheja", " I want to b devops architect"," I am living in Bangalore"]
fo=open("new1.txt","a")
for each_lines in my_content:
    fo.write(each_lines +"\n")
fo.close()
'''
'''
fo=open("new3.txt","r")
data=fo.read()
fo.close()
print(data)
'''

'''
fo=open("new3.txt","r")
#print(fo.readline())
#print(fo.readline())
fo.close()

'''

fo=open("new3.txt","r")
data=fo.readlines()
fo.close()
#print(data[-1])
for each in range(3):
    print(each)
    print(data[each])




