import random
n=int(input("Enter no.of students:"))
a=[]
b=["Truth","Dare"]
for i in range(0,n):
    a.insert(i,input("Enter name %d:"%(i+1)))
k=random.randrange(0,n)
r=random.randrange(0,2)
print(a[k])
print(b[r])
