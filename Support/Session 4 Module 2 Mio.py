print ("\nSession 4 Module 2 --- Bayesian Probability")
U=range(1,27,1)
A=U[0:13]
B=U[13:]
C=U[7:20]

A=set(A)
B=set(B)
C=set(C)
U=set(U)
print ('The set A is = %s ') %A
print ('The set B is = %s ') %B
print ('The set C is = %s ') %C
print ('The universe U is = %s ') %U
P=(len(A) + len(C) -len(A&C))
T=float(len(U)) 

print ("\nApply Bayes' Theorem to calculate the conditional probability of A given C")
P=round(len(A&C)/float(len(C)),3)
print ('Conditional probability of A given C is %r') %P
Q=len(C)/T
print ('Probability of C is %r') %round(Q,3)
Qc=1.0-Q
print ('Probability of C complement is %r') %round(Qc,3)
R=round(len(A&(U-C))/float(len(U-C)),3)
print ('Conditional probabilty of A given C complement is %r') %R
Bayes_Result= Q*P/(Q*P+R*Qc)
print ('Bayes Result for Probability of C given A %r') %(Bayes_Result)