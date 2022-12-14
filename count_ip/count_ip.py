from collections import defaultdict
f=open('ip_address.txt')
count ={}
count = defaultdict(lambda : 0,count)
lines=f.readlines()
for line in lines:
    if(not line.startswith("#")):
        ip=line.split()[0]
        print(ip)
        count[ip]=count[ip]+1

print("Final =", count)
for k,v in count.items():
    print(k,"=",v)