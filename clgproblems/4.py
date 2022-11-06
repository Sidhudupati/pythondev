#sample input 1=
#60
#50
#70
#sample output 1=
#normal triangle
 
#sample input 2=
#90
#60
#30
#sample output 2=
#right triangle

#sample input 1=
#60
#60
#60
#sample output 2=
#equilateral triangle
a=int(input())
b=int(input())
c=int(input())
if(a+b+c==180):
    if(a==90 or b==90 or c==90):
        print('Right Triangle')
    elif(a==60 and b==60):
        print('Equilateral Triangle')
    else:
        print('Normal Triangle')
else:
    print('Triangle cannot be formed')


