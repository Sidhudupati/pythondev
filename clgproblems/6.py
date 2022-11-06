#Write a Python program to print the sum of the digits of a given number.  
#For example if the input is 123, the result should be 6 (1+2+3=6).
#Sample Input
#145
#Sample Output
#10

n = int(input())
s = 0
while n>0:
    s = s+n%10
    n=n//10
print(s)

