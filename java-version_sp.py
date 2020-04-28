import subprocess
cmd="java -version"
sp=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True)
rc=sp.wait()
o,e=sp.communicate()
#print(f" out: ", {o})
#print(f" err: ", {e})
#print(bool(o))

if rc==0:
    if bool(o)==False and bool(e)==True:
            #print(e.splitlines())
            #print(e.splitlines()[0])
            #print(e.splitlines()[0].split())
            #print(e.splitlines()[0].split()[2])
            print(e.splitlines()[0].split()[2].strip("\""))
else:
    print(e)

