n=int(input())
k=0
c=0
while n!=0:
    n1,n2,n3,n4=input().split()
    if n4=="True":
        k+=1
    if n4=="False":
        c+=1
    n=n-1
print(k,c)