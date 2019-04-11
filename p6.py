c=[1,2,3,4,5]
for i,d,in enumerate(c):
    c[i]=d+5
    print(c[i])
c_5=[d+5 for d in c]
print(c_5)
table=[]
for m,n in zip(c,c_5):
    table.append([m,n])
import pprint
s=[15.8,[0.2,1.7]]
pprint.pprint(s)
m=pprint.pformat(s)
print(m)
