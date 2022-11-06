#Sample Input-1:
#3 5 2 7 6
#Sample Output-1:
#5
#Sample Input-2:
#5 5 4 7 7
#Sample Output-2:
#4
sal = [int(i) for i in input().split()]
us = []
for s in sal:
    if s not in us:
        us.append(s)
        
us.sort()
print(us[-3])



