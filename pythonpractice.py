#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 21:55:15 2019

@author: christophercatzin
"""
a = 5
print(a, "is of type", type(a))
s=1
z= (a, "is of type", type(a))
a = 2.0
print(a, "is of type", type(a))
​
​
a = 1+2j
print(s, "is complex number?", isinstance(1+2j,complex))
​
a = "This is python training"
print(a, "is of type", type(a))
​
​
#error 
print('a
      b
      c')
​
#escape sequences
​
print('a\
      b\
      c')
#double backspace
​
print('python\\data-Science')
​
#including tab
​
#Tab in strings 
​
print('python\t data-Science')
​
​
​
#enter in strings
​
print('python\ndata-Science')
​
#Raw strings
​
print(r'python\"" data-Science')
​
#triple quotes
​
print(""" my sentence has "" and ' strings""")
​
#error
print('my 
      sentence 
      has ')
​
print(""" my sentence 
      has "" 
      and ' strings""")
​
#More string operations
​
​
​
statement = "my training is good"
print (statement[0])       # Prints first character of the string
print (statement[2:11])       # Prints characters starting from 3rd to 5th
print (statement + " and interesting")
​
​
#length of a string
print(len(statement))
​
#position of a char in a string
print(statement.index("y"))
​
#countof a char in a string
print(statement.count("o"))
​
#subsetting a string
st = (statement[3:11])
​
​
#Reversing a string
print(statement[::-1])
​
#uppercase  string
print(statement.upper())
​
#lower case string
print('STATEMENT'.lower())
​
​
#splitting a string
​
splitwords= statement.split(" ")
​
splitwords= "smoking is bad".split(" ")
​
