import subprocess
cmd="bash --version"
#cmd=["bash", "version"]
sp=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True)
rc=sp.wait()
o,e=sp.communicate()

if rc==0:
    for each_lines in o.splitlines():
        if "version" in each_lines and "release" in each_lines:
            #print(each_lines)
            #print(each_lines.split())
            #print(each_lines.split()[3])
            #print(each_lines.split()[3].split('('))
            print(each_lines.split()[3].split('(')[0])
else:    
    #print("command was failed:",e)
    print("command was failed")


