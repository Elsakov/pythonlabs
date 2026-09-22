n=int(input("in_1:"))
k=0
c=0
for i in range(n):
    n1,n2,n3,n4=input("in_"+ str((i+2))+':').split()
    if n4=="True":
        k+=1
    if n4=="False":
        c+=1
    n=n-1
print("out:", k,c)