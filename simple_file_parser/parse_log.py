from collections import defaultdict
f=open('log.txt')

lines=f.readlines()
d={}
d=defaultdict(lambda:0,d)
data={}
fdate=lines[0].split(',')[0]
curr_date=fdate

for line in lines:
    curr_date=line.split(',')[0]
    code=line.split()[2].split(',')[0]
    if(fdate!=curr_date):
        data[fdate]=d

        fdate=curr_date
        d={}
        d = defaultdict(lambda: 0, d)
    else:
        d[code]=int(d[code])+1
if(fdate==curr_date):
    data[fdate] = d



for key, Value in data.items():
    print(key)
    for v,r in Value.items():
        print(v,"=",r)
#print("final data =",data)