print ('\nSession 2 Discussion 2 --- Code') 
#Import modules
import csv
import sys
#SN

train_labels = open("C:\\Users\jjsad\\Documents\\Javier\\MSc Predictive Analytics\\Math for modelers\\Python\Session 2\\trainLabels.csv","rb")
csv_tl = csv.reader(train_labels)
data_tl = list(csv.reader(train_labels))
sum_tl = len(data_tl)
print "Total rows in trainLabels list =", (sum_tl)

train = open("C:\\Users\jjsad\\Documents\\Javier\\MSc Predictive Analytics\\Math for modelers\\Python\Session 2\\train.csv","rb")
csv_t = csv.reader(train)
data_t = list(csv.reader(train))
sum_t = len(data_t)
print "Total rows in train list =", (sum_t)

combined = open("C:\\Users\jjsad\\Documents\\Javier\\MSc Predictive Analytics\\Math for modelers\\Python\Session 2\\merge.csv","w")
writer = csv.writer(combined)
for row in xrange(sum_t):
    writer.writerow(data_tl[row] + data_t[row])
print 'New file created'
combined.close() 
train_labels.close()
train.close()