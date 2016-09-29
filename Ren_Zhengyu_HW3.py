# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 19:22:41 2016

@author: ren
"""
import pandas as pd#import pandas package
data=pd.read_table('/Users/ren/Documents/学校/Github/iris.data.txt',header=0,sep=',')
#the column name had already been edited in the text editor
#import the data we download，use ’header()‘ for the first row and use sep() to
#divide columns
#define  the data we download as 'data'
print(data)#display the data
print(data.head(10))#display the	first	ten rows of the data.
print(data.tail(10))#display the last	ten rows of	 the data.
print(data.describe().transpose())#use method describe() to get statistic summary
                                  #we could get Count,	Mean,	STD,	Min,	25%,	50%,	75%,	MAX
print(data.hist())#plot a histogram for each	of the numeric columns,no special instruction in'()'
print(data.classnf.value_counts().plot(kind='bar'))#plot a bar chart for the nominal column
                                                   #'classnf' is the name of the column we are plotting
                                                   #value_counts is counting how many data we are having for different class