# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 19:29:16 2016

@author: ren
"""
#Overall Comment: Very good exercise, the assignment is in good format, your logic and code work effectively and efficienty.
#1
"""
use it to translate your Christmas cards from English into Swedish
"""
def lexicon_dic(inputWord):#define the dictionary that we will use later
   """
   Define a function working as a dictionary
   Parameters:
   inputWord-a string we input
   Returns:
   the translation of the string we input by this dictionary
   """ 
    lexicon_dic={"merry":"god", "christmas":"jul", "and":"och", 
                 "happy":"gott", "new":"nytt", "year":"ar"}
                 #import the dictionary for translation
    if inputWord in lexicon_dic:#if the word is in the dictionary, translate it
             return lexicon_dic.get(inputWord)
    else:
             return inputWord
             # if word is not in the dictionary, keep the word
def translate(string):
   """
   Define a function translate your Christmas cards from English into Swedish
   Parameters:
   string-a string we input
   Returns:
   the translation in Swedish
   """ 
    words = string.split( );
    translation = ""#create a new string
    for i in words:
        translation = translation + lexicon_dic(i) + " "
        #use the function we defined early to translate the part that need to 
        #be translated
    return translation
translate("merry christmas and happy new year")

#2
def char_freq(string):
   """
   Write a function char_freq()that takes a string and builds a
   frequency listing of the characters contained in it. 
   Parameters:
   string-a string we input
   Returns:
   show how many times the each character appears in the string we input
   """
   dictionary = {} #create a new dictionary
   for i in string:#go through all letters in the string
       dictionary[i] = dictionary.get(i,0)+1
       #use method 'get()' to returns a value for the given key.
       #dictionary.get(i,0) is looking for the key'[i]',if no [i] was found 
       #there, returns to 0, if [i] was found, +1 to the value
   return dictionary
char_freq("abbabcbdbabdbdbabababcbcbab")

    
#3
def rot_13(string):
   """
   implement an encoder/decoder of ROT-13. Then read the following secret 
   message: Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!
   Parameters:
   string-a string we input
   Returns:
   the decoded string
   """  
   key = {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u', 
       'i':'v', 'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a', 'o':'b', 'p':'c', 
       'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k',
       'y':'l', 'z':'m', 'A':'N', 'B':'O', 'C':'P', 'D':'Q', 'E':'R', 'F':'S', 
       'G':'T', 'H':'U', 'I':'V', 'J':'W', 'K':'X', 'L':'Y', 'M':'Z', 'N':'A', 
       'O':'B', 'P':'C', 'Q':'D', 'R':'E', 'S':'F', 'T':'G', 'U':'H', 'V':'I', 
       'W':'J', 'X':'K', 'Y':'L', 'Z':'M'}#import the key that used to decode 
   message=''#create a new string
   for char in string:#go through the whole string
       if char in key:#check the letter which need to be decoded
            message = message+key[char]
       else:
            message = message+char#take care of the punctuation
   return message
rot_13('Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!')      

#4
def correct(string):
   """
   Define a simple "spelling correction" function correct()that takes a
   string and sees to it that 1) two or more occurrences of the space 
   character is compressed into one, and 2) inserts an extra space
   after a period if the period is directly followed by a letter.
   Parameters:
   string-a string we input
   Returns:
   the correction of the string
   """  
   import re#import Regular expression operations
   correction = re.sub(' +',' ',string)# compressed the extra space
   finalcorrection = re.sub('\.','. ',correction)#insert a space after period
   print(finalcorrection)
correct("This  is    very funny and cool.Indeed!")

#5
def make_3sg_form(word):
   """
   define a function make_3sg_form()which given a verb in infinitive
   form returns its third person singular form. 
   Parameters:
   word-a word(verb) we input
   Returns:
   the 3rd perston singular form of the verb
   """
   newWord = ''#creat a new string
   #use method 'endswith() to judge different situation'
   if word.endswith('y'): # if the verb ends in y
        newWord = word[:-1]+'ies' # remove last letter and add ies
   elif word.endswith('o'): # if the verb ends in o
        newWord = word + 'es' # add es
   elif word.endswith('ch'): # if the verb ends in ch
        newWord = word + 'es' # add es
   elif word.endswith('s'): # if the verb ends in s
        newWord = word + 'es' # add es
   elif word.endswith('sh'): # if the verb ends in sh
        newWord = word + 'es' # add es
   elif word.endswith('x'): # if the verb ends in x
        newWord = word + 'es' # add es
   elif word.endswith('z'): # if the verb ends in z
        newWord = word + 'es' # add es
   else:
        newWord = word + 's' # add s
   return newWord 
make_3sg_form('try')
   
#6
def make_ing_form(verb):
   """
   Define a function
   make_ing_form()which given a verb in infinitive form returns its
   present participle form.
   Parameters:
   verb-a word(verb) we input
   Returns:
   the present participle form of the verb
   """  
   if verb.endswith('e'):
       presentverb = verb[:-1]+'ing'
       #returns all elements in the string except the last one 'e
       #then add 'ing'
   elif verb.endswith('ie'):
       presentverb = verb.rstrip('ie')+'ying'
       #use rstrip to strip characters from the end of the string
       #then add 'ying'
   elif (verb[-2] in 'aeiou')and(verb[-3] not in 'aeiou')and(verb[-1] not in 'aeiou'):
       #if the word consist of consonant-vowel-consonant
       presentverb = verb+verb[-1]+'ing'
       #double(add) the last letter in the string using[-1]
       #add 'ing'
   else:
       presentverb = verb+'ing'
   return presentverb
make_ing_form('hug')

#7
def max_in_list(list):
   """
   Using the higher order function reduce(), write a function max_in_list()that
   takes a list of numbers and returns the largest one.
   Parameters:
   list-a list of number we input
   Returns:
   the largest number in the list
   """  
   import functools #import functools for higher order function 'reduce()'
   #so that we can return to 'reduce'
   return functools.reduce(max, list) #forward-compatible with function
max_in_list([6,9,1,5])

#8
"""
Write a program that maps a list of words into a list of integers
representing the lengths of the correponding words. Write it in
three different ways: 1) using a for-loop, 2) using the higher order
function map(), and 3) using list comprehensions. 
Parameters:
word-a list of word we input
Returns:
a list of number which count the length of word in the list we input
"""
#using a for-loop
def map_list(words):
    lengths = [] #create a new list
    for i in words:
        lengths.append(len(i))#go over all letters in the word
        #use method 'append()' to record the length of the word
    return lengths
map_list(['hello','word'])

#using the higher order function map()
def map_Highorder(words):
    return list(map(len, words))
    #use method 'map(function, iterable...)to deal with the length of all words
    #and return a list of results
map_Highorder(["Hello", "word"])

#using list comprehensions
def list_comprehension(words):
    return [len(i) for i in words]
    #use list comprehensions  to create lists that each element is the result 
    #of the operations 'len()' applied to each member of the string we input
list_comprehension(["Hello", "word"])

#9
def find_longest_word(string):
   """
   Write a function find_longest_word()that takes a list of words
   and returns the length of the longest one. Use only higher order
   functions. 
   Parameters:
   string-a string we input
   Returns:
   the longest word in the list
   """ 
   return max(list(map(len,string)))
   #use method 'map(function, iterable...)to deal with the length of all words
   #in the string and use list（）to create a list of length of words
   #find the greatest number in the list
find_longest_word(['math', 'statistics', 'world'])

#10
def filter_long_words(list,n):
    """
    Write a function filter_long_words()that takes a list of words and an integer 
    n and returns the list of words that are longer than n.
    arameters:
    list-a list of word we input
    n-a number we input
    Returns:
    a new list that filtered the word in the list we input longer than 'n'
    """
    numberlist=[]#set up a new list
    for i in range(0,len(list)):
        if len(list[i]) > n:#pick up the word that is longer than n
           numberlist.append(list[i])#count the length of each word
        else:
            continue
    return numberlist
filter_long_words(['apple','books','cat','dog'],3)

#11
def translate(inputWords):
   """
   Use the higher order function map()to write
   a function translate() that takes a list of English words and
   returns a list of Swedish words. 
   Parameters:
   inputWords-a list of word we input
   Returns:
   the Swedish translation of the list 
   """ 
   lex_dic = {"merry":"god", "christmas":"jul", "and":"och", "happy":"gott",
           "new":"nytt", "year":"år"}#import the dictionary to translate
   return list(map(lambda x: lex_dic[x.lower()], inputWords))
translate(["merry", "christmas", "and", "happy", "new","year"])

#12
"""
Implement the higher order functions map(), filter()and reduce(). 
"""
def newmap(function,list):
    """
    Defining a function work as map function 
    Parameters: 
    function-a function we defined
    list-a list of number we input
    Return: apply the function to the list we input
    """
    newlist=[]#create a new list
    for i in list:#go over all numbers in the list
        newlist.append(function(i))
        #use method 'append()' to add function (i) to the list(work as map)
    return newlist 
newmap(lambda x: 1 + x,[1,2,3,4,5]) #use 'lambda' to crate an anonymous function 


def newfilter(function,list):
    """
    Defining a function work as filter function 
    Parameters: 
    function-a function we defined
    list-a list of number we input
    Return: filter the number in the list which do not satisfy the function we defined
    """    
    newlist = []#create a new list
    for i in list:#go over all numbers in the list
        if function(i) == True: #check if the number satisfy the function
            newlist.append(i)#if the number satisfied, add it to the new list
    return newlist
    
newfilter(lambda x: x > 3, [1, 2, 3, 4, 5]) #use 'lambda' to crate an anonymous function


def newreduce(function,list):
    """
    Defining a function work as reduce function 
    Parameters: 
    function-a function we defined
    list-a list of number we input
    Return: reduce the number in the list that satisfy the function we defined
    """
    reduction = list[0]#pick up the first number in the list
                       #suppose this number would be our final answer
    for i in range(0,len(list)):#go over all number in the list
        reduction = function(reduction,list[i])
        #apply function to the number we picked up previously compare it to the
        #new one
    return reduction
newreduce(max,[2,3,9,5,6])
