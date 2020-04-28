'''
import os
cmd="date"
os.system(cmd)
'''

import os
cmd="pwd"
st=os.system(cmd)
if st==0:
    print("return status is success")
else:
    print("return status is failure")
