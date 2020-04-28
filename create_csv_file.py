import csv
req_file="demo.csv"
'''
fo=open(req_file,'r')
csv_reader=csv.reader(fo,delimeter="|")
for each in csv_reader:
    print(each)
fo.close()
'''

fo=open(req_file,'w',newline="")
csv_writer=csv.writer(fo,delimiter='|')
csv_writer.writerow(['S_No','Name','Age'])
csv_writer.writerow([1,"suryatheja",28])
csv_writer.writerow([2,'Chandrsmitha',25])
fo.close()


