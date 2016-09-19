# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 19:29:16 2016

@author: ren
"""

#4
def correct(string):
   """
   Define a simple "spelling correction" function correct()that takes a
   string and sees to it that 1) two or more occurrences of the space 
   character is compressed into one, and 2) inserts an extra space
   after a period if the period is directly followed by a letter.
   """  
   import re#import Regular expression operations
   correction = re.sub(' +',' ',string)# compressed the extra space
   finalcorrection = re.sub('\.','. ',correction)#insert a space after period
   print(finalcorrection)
correct("This  is    very funny and cool.Indeed!")

#6
def make_ing_form(verb):
   """
   Define a function
   make_ing_form()which given a verb in infinitive form returns its
   present participle form.
   """  
   if verb.endswith('e'):
       presentverb = verb[:-1]+'ing'
       #returns all elements in the string except the last one 'e
       #then add 'ing'
   elif verb.endswith('ie'):
       presentverb = verb.rstrip('ie')+'ying'
       #use rstrip to strip characters from the end of the string
       #then add 'ying'
   elif verb[-2] in 'aeiou':#if the word consist of consonant-vowel-consonant
       presentverb = verb+verb[-1]+'ing'
       #double(add) the last letter in the string using[-1]
       #add 'ing'
   else:
       presentverb = verb+'ing'
   return presentverb
make_ing_form('do')
