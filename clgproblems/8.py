#Write a Python program that prints the numbers from 1 to 'N'. But for multiples of 
#three print "Zing" instead of the number and for the multiples of five print "Bing".
#For numbers which are multiples of both three and five print "ZingBing".
#Sample Input:1
#15
#Sample Output:1
#1
#2
#Zing
#4
#Bing
#Zing
#7
#8
#Zing
#Bing
#11
#Zing
#13
#14
#ZingBing

a=int(input())
for i in range(1,a+1):
    if i%3==0 and i%5==0:
        print("ZingBing")
    elif i%3==0:
        print("Zing")
    elif i%5==0:
        print("Bing")
    else:
        print(i)            