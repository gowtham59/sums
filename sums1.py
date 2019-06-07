a=int(input())
b=int(input())
m=[]
for x in range(a):
    k=input()
    m.append(k)
c=0
for i in range (b):
    c=int(c)+int(m[i])
print (c)
