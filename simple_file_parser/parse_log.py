from collections import defaultdict
f=open('log.txt')

lines=f.readlines()
d={}
d=defaultdict(lambda:0,d)
data={}
fdate=lines[0].split(',')[0]
curr_date=fdate
print("fdate=",fdate)

for line in lines:
    curr_date=line.split(',')[0]
    code=line.split()[2].split(',')[0]
    if(fdate!=curr_date):
        print("Fdate is not curr date",fdate,curr_date)
        data[fdate]=d
        print(data)
        fdate=curr_date
        d = defaultdict(lambda: 0, d)
    else:
        d[code]=int(d[code])+1
if(fdate==curr_date):
    data[fdate] = d
    
print("final data =",data)