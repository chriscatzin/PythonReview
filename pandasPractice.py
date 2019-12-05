#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 11:37:13 2019

@author: christophercatzin
"""

import numpy as np
import pandas as pd
import csv
import os

os.chdir('/Users/christophercatzin/Data')

os.getcwd()


f = open("/Users/christophercatzin/Data/car_prices.csv",'r')
f.readlines()

newdata = pd.read_csv('Sample_csv_File_V1.csv')
newdata.dtypes

#checking the data
#What is the number of observations in the dataset?
newdata.shape[1]
newdata.shape[0] #will give you only the observations/rows number
newdata.shape
newdata.info()
newdata.dtypes

t = newdata.dtypes

#gives stats about numerical variables

checkingdata = newdata.describe()
checkingdata = newdata.describe().transpose()

#allows us to view first / last X observations
t=newdata.head(12)
t=newdata.tail()

#allows us to view a sample of observations
t=newdata.sample(n=370)
t=newdata.sample(frac = 0.2)

#getting frequency table of a single variable
t=newdata['TRFRID'].value_counts()
car = pd.read_csv('car_prices.csv')

t=car.car.value_counts(dropna=False)

t=newdata.TRFRID.value_counts(dropna=False)

t=newdata.TRFRID.value_counts(dropna=False)

print(newdata.columns) # prints the column names

# reading a csv file with options
newdata1 = pd.read_csv('Sample_csv_File_V2.csv')
newdata1 = pd.read_csv('Sample_csv_File_V2.csv',dtype=str, delimiter='|')
newdata1.dtypes
newdata1.info()
newdata1['DateofEvaluation']=(pd.to_datetime(newdata1['DateofEvaluation']))

#Changing the data type of a variable after reading a file
#var= '123.234'

newdata1['Revenue'] = newdata1['Revenue'].astype(float)
newdata1.Revenue = newdata1.Revenue.astype(float)

# newdata1.Revenue = newdata1.float(['Revenue'])

newdata1.dtypes
t = newdata1.dtypes
newdata1.PROGRAMEID.unique() # calulating the unique rows
t = newdata1.describe()

#getting frequency table of a single variable
newdata['PROGRAMEID'].value_counts()
newdata.PROGRAMEID.value_counts()
t=newdata1.Revenue.value_counts()

#Group by
newdata1.agg({'Revenue':'mean'})
print(newdata1['Revenue'].mean())
print(newdata1.Revenue.min())
print(newdata1['Revenue'].median())
print(newdata1['PROGRAMEID'].mode())
print(newdata1['Revenue'].std())
print(newdata1['PROGRAMEID'].count())
abcd = np.percentile(newdata1['Revenue'], [10,20,30,40,80,90,95,99,99.5], axis =0)

#Part 2 =========================   DATA HANDLING ================================================
age = pd.read_csv('Sample_Age.csv',dtype=str, delimiter=',')

#Changing the data type of a variable after reading a file
age.Age = age.Age.astype(float)

#Merging files
newdata2 = pd.merge(newdata1,age[['PERSONID','Age']], how='left', on='PERSONID')

# An example where the names are not the same in both the files
# newdata2 = pd.merge(newdata1,age, how='left', left_on = 'PersonID' ,right_on = 'Person_id')
#Data Exploration
#Imputing Data
newdata2['Age'] = newdata2['Age'].fillna(newdata2['Age'].mean())
t = newdata2.describe()

#Selecting a few columns from a dataframe
t=newdata2[['PERSONID', 'Revenue', 'Age']]

#Creating a new variable
newdata2['rev2'] = newdata2['Revenue']*2
newdata2.rev2 = newdata2.Revenue*2
newdata2['rev3'] = newdata2['Revenue'] + newdata2['rev2']
newdata2.shape

#filtering data
t= newdata2[newdata2.Revenue < 110]
t= newdata2.Revenue < 110

# Creating a flag variable
newdata2['Rev_flag'] = np.where(newdata2['Revenue'] > 120, 'GT_120',
        np.where(newdata2['Revenue'] > 110, 'GT_110',
        np.where(newdata2['Revenue'] > 105, 'GT_105','<=120')))
        
newdata2['Rev_flag'].unique()

newdata2['age_grp'] = newdata2['Age'].apply(lambda x :
    'GRP_LE_35' if x <= 35
    else 'GRP_LE_50' if x > 35 and x <= 50
    else 'GRP_GT_50_70' if x > 50 and x <= 70
    else 'GRP_GT_70' if x > 70
    else 'MISS')
    
newdata2['age_grp'].unique()
newdata2['age_grp'].value_counts()

# Dropping a column

t = newdata2.drop(['rev3','rev2'], axis = 1)

del newdata1

# excluding rows based on a condition

t = newdata2[newdata2['PROGRAMEID'] != 'CM-DP']

t = newdata2.drop([5,7])

t = newdata2.tail(1000)

list1 = [1,2,3]

newdata2.tail(1000).to_csv("File.csv")

pd.DataFrame(list1).to_csv("File.csv")

# Applying functions on dataframes
# 1

def USD(x):
    return float(x / 1.34)

newdata2['Revenue_USD'] = newdata2['Revenue'].apply(USD)


# use .apply

def rev_age(row):
    return row['Revenue']/row['Age']

newdata2['rev_age'] = newdata2.apply(rev_age, axis = 1)

def rev_age(row):
    return row['Revenue'] * row['Age']

newdata2['rev_age'] = newdata2.apply(rev_age, axis = 1)



# newdata2['rev_age'] = newdata2['Age'] * newdata2['Revenue']


# Renaming a column
newdata2.rename(columns={'CUSTID_y':'CUST_ID_yuiys'}, inplace= True)

# sorting a dataset
newdata2 = newdata2.sort_values(['Age', 'Revenue'], ascending = True)

newdata2 = newdata2.Revenue.sort_values()


# Missing value treatment

# newdata2['Age'].fillna(47, inplace = True)

#groupby

Age_mean = newdata2.groupby(['TRFRNAME']).Revenue.mean()

Age_mean = newdata2.groupby(['TRFRNAME', 'PROGRAMID']).Age.mean().reset_index()

# Using SQL in python

from pandasql import *

pysqldf = lambda r : sqldf(r, globals())

r = """
    Select PROGRAMEID,
    (sum(Revenue))/1000 as rev_sum00,
    avg(Age) as mean_age
    from newdata2
    group by PROGRAMEID
    """
df_test = pysqldf(r)

r = """
    Select *,
    CASE when "Revenue" > 150 THEN ">150"
    WHEN "Revenue" > 110 THEN ">110"
    ELSE "<=110"
    END
    as "REVBand"
    from newdata2
    """
df_test = pysqldf(r)




newdata3 = pd.read_csv('Practice_data.csv')
newdata3.dtypes

chicken = newdata3[['item_name','item_price']]
mod = chicken[chicken['item_name'] != 'Chicken']
mod['Chicken'] = mod['item_name']
mod['Burito'] = mod['item_name']
mod['Chips'] = mod['item_name']
mod['Other'] = mod['item_name']

x = mod.drop(['item_name'], axis = 1)









def func(x):
    d = {}
    d['count_cust'] = x['PERSONID'].count()
    d['total_age'] = x['Age'].sum()/1000
    return pd.Series(d)

t = newdata2.groupby(['PROGRAMEID','TRFRID']).apply(func).reset_index()


# GRAPHS AND DIAGRAMS

from matplotlib import pyplot as plt

olsdata = pd.read_csv('OLS_dataset_new.csv')

t = olsdata.describe()

# SIMPLE LINE GRAPH

plt.scatter(olsdata['CRIM'], olsdata['MEDV'])
plt.xlabel("CRIM")
plt.ylabel("median price")

plt.scatter(olsdata['MEDV'], olsdata['CRIM'])
plt.xlabel("MEDV")
plt.ylabel("CRIM")

plt.barh(olsdata['CRIM'], olsdata['MEDV'])
plt.xlabel("CRIM")
plt.ylabel("MEDV")

plt.bar(olsdata['CRIM'], olsdata['MEDV'])
plt.xlabel("CRIM")
plt.ylabel("MEDV")

plt.plot(olsdata['CRIM'], olsdata['MEDV'])
plt.xlabel("CRIM")
plt.ylabel("MEDV")

plt.plot(df_test['PROGRAMEID'], df_test['mean_age'])
plt.xlabel("PROGRAMEID")
plt.ylabel("mean_age")














