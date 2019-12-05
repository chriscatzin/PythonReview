#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 09:26:49 2019

@author: christophercatzin
"""

#For loop exercises :

#1 - Calculate age-----------------------------------------------------


def getAge():
    years_of_birth = [1990, 1991, 1990, 1990, 1992, 1991]
    for i in years_of_birth:
        print(2019 - i)
        
getAge()


#2------------------------------------------------------------------

#Write a  program to find those numbers which are divisible by 7 and multiple of 6, between 1600 and 2900 (both included)

nl=[]
for x in range(1600, 2900):
    if (x%7==0) and (x%6==0):
        nl.append(str(x))
print (','.join(nl))


#3----------------------------------------------------------

#Write a Python program that takes a word from the user and reverse it.

def reverse(string): 
    string = string[::-1] 
    return string 

word = input("Enter a word you desire: ")
reverse(word)

#4-----------------------------------------------------------------

#Write a Python program to count the number of even and odd numbers from the following

numbers = (7,9,2,4,5,19,34,99,102,3,75)

count_odd = 0
count_even = 0
for x in numbers:
        if not x % 2:
    	     count_even+=1
        else:
    	     count_odd+=1
print("Number of even numbers :",count_even)
print("Number of odd numbers :",count_odd)

#5--------------------------------------------------------------

#Write a Python program to get the Fibonacci series between 0 to 50.
#
#Note : The Fibonacci Sequence is the series of numbers :
#0, 1, 1, 2, 3, 5, 8, 13, 21, .... 

#Every next number is found by adding up the two numbers before it.

nterms = int(input("How many terms? "))
# first two terms
n1, n2 = 0, 1
count = 0
# check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1


#6 -----------------------------------------------------------------

# Write a Python program which iterates the integers from 1 to 50. 
# For multiples of three print "Three" instead of the number and for 
# the multiples of five print "Five". For numbers which are multiples of 
# both three and five print "ThreeFive".

for x in range(50):
    if x % 3 == 0 and x % 5 == 0:
        print("ThreeFive")
        continue
    elif x % 3 == 0:
        print("Three")
        continue
    elif x % 5 == 0:
        print("Five")
        continue
    print(x)


