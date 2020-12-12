print ('\nSolving productivity by Gauss Jordan') 
import numpy as np
Data1 = np.array([[1300,8],[4200,12]]) 
Data2 = np.array([[60],[120]])
Result1= np.linalg.solve(Data1,Data2)
print 'The answer to equation system is:', Result1 
