print ('\nExample 6 Section 7.1 Lial', 'r')
set()
U = set([0, 1, 2, 3 , 4, 5, 6, 7, 8, 9, 10])
A = set([3, 6, 9])
B = set([2, 4, 6, 8])
print ('\nThe Universe U = %r') %U
print ('\nSub set A = %r') %A
print ('\nSub set B = %r') %B
print ('\nInformation given Find A union B')
Uab=A & B
print ('\nUnion of A and B = %r \n') %Uab
Bc= U - B
Uabc= A & Bc
print ('\nInformation given Find A intersection Bc')
print ('\nThe intersection of A and Bc is %r \n') %Uabc

print ('\nExample 7 Section 7.1 Lial')
U = set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
A = set([1, 3, 5, 7, 9, 11])
B = set([3, 6, 9, 12])
C = set([1, 2, 3, 4, 5])
print ('\nThe Universe U = %r') %U
print ('\nSub set A = %r') %A
print ('\nSub set B = %r') %B
print ('\nSub set C = %r') %C
print ('\nInformation given Find A union B')
Uab=A | B
print ('\nUnion of A and B is %r \n') %Uab
print ('\nInformation given Find where A union B intersects Cc')
Cc = U - C
ICcab = Uab & Cc
print ('\nUnion of A union B intersects Cc %r \n') %ICcab