# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 14:14:34 2023

@author: amuly
"""

#LISTS
Y1=[20,30,40,50,60]
Y1[3]

Y1[4]
Y2=['yellow',2,3,4,90]
Y2[0]=1
Y2

Y3=['GREEN',90,80,70]
Y3[0]=100
len(Y1) # TO CALCULATE THE LENGTH OF THE DATA TYPES

sum(Y1)# TO CALICULATE THE SUM OF THE DATA TYPES 

Z1=sum(Y1)/len(Y1) # AVERAGE
Z1
#POP
Z2=['blue',60,70,80,90]
Z2.pop(0) # IT WILL REMOVE THE DATA TYPE AS PER THE POSITION 
Z2
#INSERT
Z2.insert(0,50)
Z2

Y1.insert(3,80)
Y1

Y1.insert(4,90) # IT WILL ADD THE DATA TYPES(POSITION,VALUE)
Y1

Y1.pop()
Y1
#APPEND
Y1.append(34) # BY DEFAULT IT WILL ADD THE NUMBER IN THE END
Y1

Y2.append(100)
Y2
#EXTEND
Y2.extend([4,32])
Y2

Z2.extend([3,56])
Z2

#practice of all gthe commands 
Z3=[20,80,90,[34,44,56],56]
Z3[3]
Z3[3][0]
Z3[3][1]
Z3[3][2]


Z3.pop(3)
Z3

Z3.insert(3,100)
Z3

Z3.pop()
Z3

Z3.append(120)
Z3

len(Z3)
sum(Z3)

Z4=sum(Z3)/len(Z3)
round(Z4)

X1=[100,200,300,800,900]
X1[3]=400
X1
len(X1)
sum(X1)

X2=sum(X1)/len(X1)
X2

round(X2)

X1.pop(3)
X1
X1.insert(4,400)
X1
X1.pop(3)
X1
X1.append(500)
X1

X1=[100,200,300,400,500,[70,80,90],600]
X1.pop(5)
X1[5][0]
X1[5][1]
X1[5][2]

X1.pop(5)

X1.remove([70,80,90])
X1


X3=[10,20,30,[1,2,3],40]
X3[3].index(3)
