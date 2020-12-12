print ('\nFinal Exam Problem 3')
t1= 0
t2= 1
t3= 2
t4= 3
t5= 4
t6= 5
t7= 6
t8= 7
fd1 = float(6.412*t1**3 - 69.774*t1**2 + 124.24*t1 + 6.992)
fd2 = float(6.412*t2**3 - 69.774*t2**2 + 124.24*t2 + 6.992)
fd3 = float(6.412*t3**3 - 69.774*t3**2 + 124.24*t3 + 6.992)
fd4 = float(6.412*t4**3 - 69.774*t4**2 + 124.24*t4 + 6.992)
fd5 = float(6.412*t5**3 - 69.774*t5**2 + 124.24*t5 + 6.992)
fd6 = float(6.412*t6**3 - 69.774*t6**2 + 124.24*t6 + 6.992)
fd7 = float(6.412*t7**3 - 69.774*t7**2 + 124.24*t7 + 6.992)
fd8 = float(6.412*t8**3 - 69.774*t8**2 + 124.24*t8 + 6.992)
print ('\n The increase for 1998 is = %r')% fd1
print ('\n The increase for 1999 is = %r')% fd2
print ('\n The increase for 2000 is = %r')% fd3
print ('\n The increase for 2001 is = %r')% fd4
print ('\n The increase for 2002 is = %r')% fd5
print ('\n The increase for 2003 is = %r')% fd6
print ('\n The increase for 2004 is = %r')% fd7
print ('\n The increase for 2005 is = %r')% fd8
alist=[fd1,fd2,fd3,fd4,fd5,fd6,fd7,fd8]
largest=alist[0]
for large in alist:
    if large > largest:
        largest=large
print(largest)
print ('\nTherefore the year during which rents were increasing most rapidly is 1999 with an increase of $ %r')% fd2