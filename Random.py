import random
n=int(input("Enter no.of Students:"))
a=[]
b=["Truth","Dare"]
for i in range(0,n):
    a.insert(i,input("Enter name %d:"%(i+1)))
x=random.randrange(0,n)
y=random.randrange(0,2)
print(a[x])
print(b[y])
