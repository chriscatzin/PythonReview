#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 09:27:20 2019

@author: christophercatzin
"""

# 1 

#Create a function to calculate the absolute value of a number without using the abs() function to calculate the absolute value for -9 and 7.2
def my_abs(value):
    """Returns absolute value without using abs function"""
    if value <= 0:
        return value * -1
    return value * 1

print(my_abs(-9))
print(my_abs(7.2))


# 2

# for the given data (20,30,40,50,100), create a function to calcuate the total/3 
#note that all the calcualtions have to be done within the function

def calc(*args):
    return sum(args) / 3

calc(20, 30, 40, 50, 100)

## 3
#create a function to work in range(43,60) such that if the number is <50, it prints out "LT_50" else it should print out (number+3)

def func(x):
    if x < 50:
        print("LT_50")
    else:
        print(x + 3)

func(23)
func(100)
#4

# create a functio which takes 2 inputs as num and x and do the following
#if num>=0 then calcuate num*x else num*x/2

def func(num, x):
    if(num >= 0):
        print(num * x)
    else:
        print(num * x / 2)

func(10, 2)
func(-3, 5)


#5 create a function to create a new list with only the nos which can be divided by 3 from the following list

def func():
    li = [5, 7, 21, 99, 51, 62, 77, 27, 73, 61] 
    newList = []
    for x in li:
        if (x % 3 == 0):
            newList.append(x)
            print(newList)

func()
# 6

#create a function using lambda function to overwrite the following list with all the elements squared


def func():
    li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61] 
    square = lambda x: x * x
    squared = list(map(square, li))
    print(squared)


func()