#sample input=
#enter x1 and y1
#2
#4
#enter x2 and y2
#10
#15
#sample output=
#hari's house is located at (6.00,9,50)

print("Enter x1 and y1:")
a=int(input())
b=int(input())
print("Enter X2 and y2:")
c=int(input())
d=int(input())
k=(a+c)/2
l=(b+d)/2
print("hari's home is located at ({:.2f} , {:.2f})".format(k,l))