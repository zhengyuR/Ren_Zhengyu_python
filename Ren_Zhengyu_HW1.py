# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 19:47:57 2016

@author: ren
"""
#1
#Your marks are influenced by your format, please refer to the format that Professor G has shown during the lecture. The content
#we expect are the problem you are trying to solve, the input variables and the output you expect. Once you have corrected them,
#I am more than happy to give back your mark!
#Overall Comment: Very good assignment! You have covered all the possible situations. And you commented them well which shows
#you have a very good understanding of the calculation and code.
def max(a,b):
    """
    Define a function max()that takes two numbers as arguments and returns 
    the largest of them. Use the if-then-else construct available in Python.
    """
    if a > b:
        print(a,'is maximum')
        return a
    elif a==b:
        return('The numbers are equal')
    else:
        print(b,'is maximum')
        return b
max(3,4)

#2
def max_of_three(a,b,c):
    """
    Define a function max_of_three()that takes three numbers as arguments 
    and returns the largest of them. 
    """
    if a>=b:                   #set up a new parameter to compare
        t=a
    else: 
        t=b
    if t > c:
        print(t,'is maximum')
        return t
    else:
        print(c,'is maximum')
        return c
max_of_three(4,3,4)

#3
def length(string):
    """
    Define a function that computes the length of a given list or string.  
    """
    number=0#the length of the string starts from 0
    for num in string:#go over all the letter in the string
        number=number+1
    print('the length is',number)
length('apple')

#4
def character(x):
    """
    Write a function that takes a character (i.e. a string of length 1) and
    returns True if it is a vowel, False otherwise. 
    """
    if (x=="a"or x=="A"or x=="e"or x=="E"or x=="i"or x=="I"or x=="o"or x=="O"or x=="u"or x=="U"):
        return('True')
    else:
        return('False')
character('U')

#5
def translate(x):
    """
    Write a function translate()that will translate a text into "rövarspråket" 
    (Swedish for "robber's language"). That is, double every consonant and place
    an occurrence of "o"in between. For example, translate("this is fun") should 
    return the string"tothohisosisosfofunon".
    """
    string=""#set up a new string
    x=x.replace(" ","")#take care of spaces
    for i in range(0,len(x)):#go over all the letters in the text
        if (x=="a"or x=="A"or x=="e"or x=="E"or x=="i"or x=="I"or x=="o"or x=="O"or x=="u"or x=="U"):
        #check if the letter is a vowel          
           string = string+x[i]#if the letter is a vowel just add it to the new string 
        else:
            string = string+x[i]+"o"+x[i]
        #if the letter is consonant,double it and place the 'o' and add it to the new string
    return string
translate("this is fun")

#6
def sum(inputList):
    """
    Define a function sum()and a function multiply()that sums and multiplies all 
    the numbers in a list of numbers. 
    """
    sum=0#the sum of the list starts from 0
    for num in inputList:
        sum=sum+num#add all number in the list
    print("the sum is",sum)
sum([1,2,3,4])

def multiply(inputList):
    multiply=1#the multiplication of the list starts from 1
    for num in inputList:
        multiply= multiply*num#multiply all number in the list
    print("the multiply is",multiply)
multiply([1,2,3,4])
    
#7
def reverse(string):
    """
    Define a function reverse()that computes the reversal of a string. 
    """
    string=string.replace(" ","")#take care of spaces
    if len(string) <= 1:#if the length of the string is 1,hold
        return string
    else:
        return string[::-1]#reverse the string
reverse('I am testing')

#8
def is_palindrome(string):
    """
    Define a function is_palindrome()that recognizes palindromes. 
    """
    string = string.upper()
    if reverse(string) == string:
    #use function reverse() to check if the reverse of the string is same as the original string
            return True
    else:
            return False
is_palindrome('Radar')

#9
def is_member(x,a):
    """
    Write a function is_member()that takes a value x and a list of values a, 
    and returns True if xis a member of a,False otherwise. 
    """
    for i in range(0,len(a)):#go over all the number in the list
        if x == a[i]:#compare x to the number in the list to see if they are the same
            return True
        else:
            return False
is_member(3,[2,4,5])

#10
def overlapping(x,y):
    """
    Define a function overlapping()that takes two lists and returns True if they 
    have at least one member in common, False otherwise. 
    """
    for i in range(0,len(x)):
        for j in range(0,len(y)):
            if x[i] == y[j]:
                return True
            else:
                continue#reapet until finished all number in the list
    return False
overlapping([3,4,5],[6,7,3])

#11

def generate_n_chars(x,y):
    """
    Define a function generate_n_chars()that takes an integer nand a character 
    c and returns a string, ncharacters long.
    """
    s = "" #set up a new string
    for i in range(x):#number that character need to repeat
        s = s+y
    return s#returns a string
generate_n_chars(5,"x") 

#12
#Define a procedure histogram()that takes a list of integers and prints
#a histogram to the screen.
def histogram(list):
    for i in range(0,len(list)):#go over the number in the list
        print('*'*list[i]) 
histogram([4,9,7])

#13
def max_in_list(list):
    """
    Write a function max_in_list()that takes a list of numbers and returns the 
    largest one. 
    """
    x=list[0] #set x be the first number in the list
    for i in range(0,len(list)):#go over the number in the list
        if x<=list[i]: #if the second one is bigger than the first
            x=list[i] #assign x to the bigger one
        else:
            continue#repeat until find the max number
    return x
max_in_list([9,11,7,5])

#14
def length(word):
    """
    Write a program that maps a list of words into a list of integers representing
    the lengths of the correponding words. 
    """
    list=[]#set up a new list
    for i in range(0,len(word)):
       list.append(len(word[i]))#count the length of each word
    print(list)
length(['apple','book','cat','dog'])

#15
def find_longest_word(list):
    """
    Write a function find_longest_word()that takes a list of words and returns 
    the length of the longest one. 
    """
    x=len(list[0]) #set x be the first length of word in the list
    for i in range(0,len(list)):
        if x<=len(list[i]):#if the second one is longer than the first
           x=len(list[i])#assign x to the bigger one
        else:
             continue#repeat until find the max number
    return x
find_longest_word(['apple','books','cat','dog'])

#16
def filter_long_words(list,n):
    """
    Write a function filter_long_words()that takes a list of words and an integer 
    n and returns the list of words that are longer than n.
    """
    numberlist=[]#set up a new list
    for i in range(0,len(list)):
        if len(list[i]) > n:#pick up the word that is longer than n
           numberlist.append(list[i])#count the length of each word
        else:
            continue
    return numberlist
filter_long_words(['apple','books','cat','dog'],3)
