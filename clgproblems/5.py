#Write a python program to find the greatest of three numbers.
#Sample input & output 1:
#12
#23
#56
#56 is greatest
#Sample input & output 2:
#45
#16
#32
#45 is greatest

n1=int(input())
n2=int(input())
n3=int(input())
if(n1>n2 and n1>n3):
    print(n1,"is greatest") 
elif(n2>n1 and n2>n3):
    print(n2,"is greatest")
else:
    print(n3,"is greatest")

