a=int(input("Enter number a:"))
b=int(input("Enter number b:"))
for n in range(a,b+1):
    prime=True
    for i in range(2,n):
        if n%i==0:
            prime=False
            break
    if prime==True:
        print(n,end=' ')    