#given the total no. of students who have attended the event for
#  the 3 days. Write a python code to find the no. of students 
# who have attended the event on day 1,2 and 3.

#Enter total no. of students:10500
#sample output=
#day1: 3000
#day2: 6000
#day3: 1500

m=int(input("Enter total no. of students:"))
k=2/7*m
l=4/7*m
m=1/7*m
a=int(k)
b=int(l)
c=int(m)
print("day1:",a)
print("day2:",b)
print("day3:",c)
