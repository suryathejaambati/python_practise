#Working withe text files

'''
fo=open('newdemo.txt','w')
#print(fo.mode)
#print(fo.readable())
#print(fo.writable())
fo.close()
'''
'''
my_content=["This is data -1\n","This is data -2\n","This is data-3"]
fo=open('newdemo.txt','a')
fo.write("I am adding the new data\n")
fo.write("I am adding the first data\n")
#fo.writelines(my_content)
fo.close()
'''
'''
my_content=["This is data -1\n","This is data -2\n","This is data-3"]
fo=open('newdemo.txt','w')
for each_lines in my_content:
    fo.write(each_lines+"\n")
fo.close()	
'''
'''
fo=open('newdemo.txt','r')
data=fo.read()
fo.close()
print(data)
'''
'''
fo=open('newdemo.txt','r')
print(fo.readline())
print(fo.readline())
print(fo.readline())
fo.close()
'''
'''
fo=open('newdemo.txt','r')
data=fo.readlines()
fo.close()
print(data[-1])

'''
'''
fo=open('newdemo.txt','r')
data=fo.readlines()
for eachlines in range(3):
    print(data[eachlines])
fo.close()
'''

#sfile="newdemo.txt"
#dfile="random.txt"
sfile=input("Enter sfile:")
dfile=input("Enter dfile:")
sfo=open(sfile,'r')
content=sfo.read()
sfo.close()
dfo=open(dfile,'w')
dfo.write(content)
dfo.close()



















