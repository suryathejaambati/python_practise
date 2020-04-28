from datetime import datetime
import pytz
'''
ist=pytz.timezone('Asia/Kolkata')
print(datetime.datetime.now(ist))
print(type(ist))
print(datetime.datetime.now().month)
print(datetime.datetime.now().year)
print(datetime.datetime.now().day)
print(datetime.datetime.now().hour)
print(datetime.datetime.now().minute)
print(datetime.datetime.now().second)
print(datetime.datetime.now())
#print(datetime.datetime.now(ist).strftime("%y-%m-%d"))
#print(datetime.datetime.now(ist).strftime("%Y-%m-%d"))
#print(datetime.datetime.now(ist).strftime("%y-%-m-%-d"))
print(datetime.datetime.now(ist).strftime("%c"))
print(datetime.datetime.now(ist).strftime("%x"))
print(datetime.datetime.now(ist).strftime("%y-%m-%d"))
print(datetime.datetime.fromtimestamp(15555243))
#print(datetime.time.now())
'''

print(datetime.now())
req_timz=pytz.timezone(eastern)
print(datetime.now(req_timz))

