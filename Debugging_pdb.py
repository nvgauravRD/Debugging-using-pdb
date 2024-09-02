# Debugging in python

"""
De-bugging can be done using pdb package in python
"""

import pdb

# make use of set_trace() to add debug points and many more

def AddTwoNum(num1, num2):
    return num1 + num2


num1, num2 = 5, 6

pdb.set_trace()

print(AddTwoNum(num1,num2))

"""
Output:
(Pdb) num1
5
(Pdb) num2
6
(Pdb) 
6
(Pdb) num1 + num2
11
(Pdb) AddTwoNum(num1,num2)
11
(Pdb) exit
"""
