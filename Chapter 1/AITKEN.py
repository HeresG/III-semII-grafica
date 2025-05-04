import math
def f(x):
    return(1-0.5*x*x)
flag=0
x0=float(input("Enter the initial value of x:"))
err=float(input("\nEnter the error:"))
n=int(input("\nEnter the number of itterations:"))
for i in range (1,n):
    x1=f(x0)
    x2=f(x1)
    d=(x2-x1)-(x1-x0)
    x3=x2-(math.pow((x2-x1),2))/d
    print(x3)
    if(math.fabs(x3-x2)<err):
        print("\nThe fixed point is:",x3)
        flag=1
        break
    x0=x3
        
        
    