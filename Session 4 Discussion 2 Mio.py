print ("\nModule 4 Discussion 2: Bayesian model")
import pandas as pd 
train= pd.read_csv("C:\\Users\jjsad\\Documents\\Javier\\MSc Predictive Analytics\\Math for modelers\\Python\\Session 4\\train.csv", sep=',')
x = pd.DataFrame(train[['Survived', 'Sex']])

TP = x.shape[0]
TS = x[x.Survived == 1].shape[0]
TF = x[x.Sex == 'female'].shape[0]
FS = x[(x.Survived == 1) & (x.Sex == 'female')].shape[0]
TM= x[x.Sex == 'male'].shape[0]
MS = x[(x.Survived == 1) & (x.Sex == 'male')].shape[0]
TPS = float((TS/TP)*100)

print ('\nBasic Data')
print "Total passanger in the ship = %r" % TP
print "Total passanger survive = %r" % TS
TV = TP - TS
print "Total victims = %r" % TV
print "Total female passangers = %r" % TF
print "Total female survive = %r" % FS
FV = TF - FS
print "Total female victims = %r" % FV
print "Total male passangers = %r" % TM
print "Total male survive = %r" % MS
MV = TM - MS
print "Total male victims = %r" % TS

print ('\nBasic Probabilities')
P9 = float (TM)/TP
P9 = P9*100
print ('Probability being male in the ship population is %r') %round(P9,1), "%"
P10 = float (TF)/TP
P10 = P10*100
print ('Probability being female in the ship population is %r') %round(P10,1), "%"
P1 = float(TS)/TP
P1= P1*100
print ('Probability of Surviving is %r') %round(P1,1), "%"
P2 = 100 - P1
print ('Probability of beign a victim is %r') %round(P2,1), "%"
P3 = float(FS)/TF
P3 = P3*100
print ('Probability among females to survive is %r') %round(P3,1), "%"
P5 = 100 - P3
print ('Probability of female population not surviving is %r') %round(P5,1), "%"
P4 = float(MS)/TM
P4 = P4*100
print ('Probability among males to survive is %r') %round(P4,1), "%"
P6 = 100 - P4
print ('Probability of male population not surviving is %r') %round(P6,1), "%"

print ('\nConditional Probabilities')
P7 = float(MS)/TS
P7 = P7*100
print ('Probability of survive being a male passanger %r') %round(P7,1), "%"
P8 = float(FS)/TS
P8 = P8*100
print ('Probability of survive being a female passanger %r') %round(P8,1), "%"