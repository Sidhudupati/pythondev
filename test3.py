a=int(input("Enter first number: "))
b=int(input("Enter second number:"))
c=int(input("Enter third number: "))
if a==b and a==c:
    print("All are equal")
elif a>b and a>c:
    print(a,"is greatest")  
elif b>c and b>a:
    print(b,"is greatest")
else:
    print(c,"is greatest")          