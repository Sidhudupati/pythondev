#Write a Python program to find the given number is prime number or not
#Sample input & Output 1=
#13                                                                                                                      
#Prime number
#Sample input & output 2=
#32                                                                                                                      
#Not a prime number                                                                                               
n = int(input())
prime = True
for i in range(2,n):
    if n%i == 0:
        prime = False
        break
if prime:
    print("Prime number")
else:
    print("Not a prime number")

