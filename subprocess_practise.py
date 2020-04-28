'''
import os
out=print(os.system("dirsdf"))
print(out)

'''

import subprocess
#cmd="ls -lrt" # this is for Shell is true and added uninversal lines are true
#cmd=['ls', '-lart'] #this is for Shell is false
#cmd=ls -lrt
#cmd.split()
cmd="bash --version"
sp=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True)
rc=sp.wait()
o,e=sp.communicate()
print(o)
print(e)

print(rc)


# In windows you can use shell is true for all opearations

