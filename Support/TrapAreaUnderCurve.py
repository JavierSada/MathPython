import sys

def integral():
    global eq     
    eq = raw_input("Enter equation in terms of x:  ")
    
    leftend = raw_input("Enter a value or the left end point:  ")
    rightend = raw_input("Enter b value or the right end point:  ")
    n = raw_input("Enter number of rectangles:  ")
    
    leftend = int(leftend)
    rightend = int(rightend)
    n = int(n)
    
    #Calculate area using width of each rectangle
    
    deltaX = (rightend - leftend)/float(n)
    
    #Print Results
    
    print 'Your width is ', deltaX
    print 'Leftend sum is ',LeftEndSum(n, leftend, deltaX)
    print 'Rightend sum is ',RightEndSum(n, leftend, deltaX)
    print 'Trap sum is (Avg of Left and Right Ends)',Trap(n, leftend, deltaX)
    
def LeftEndSum(num, le, dx):
    leftSum = 0.0
    for i in range(num):
        x = le + i * dx
        h = eval(eq)
        leftSum = leftSum + h*dx
        #print x,h,leftSum
    return leftSum

def RightEndSum(num, le, dx):
    rightSum = 0.0
    for i in range(num):
        x = le + (i + 1) * dx
        h = eval(eq)
        rightSum = rightSum + h*dx
        #print x,h,leftSum
    return rightSum 

# Trap area approximation        
def Trap(num, le, dx):
    tsum = .5*(RightEndSum(num, le, dx) + LeftEndSum(num, le, dx))
    return tsum
    
if __name__== '__main__':
    integral()
    