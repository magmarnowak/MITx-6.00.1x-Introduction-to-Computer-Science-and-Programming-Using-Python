# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 16:18:00 2017

@author: MN
"""
#%% Problem set 1.1
#Assume s is a string of lower case characters.
#Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print:
#Number of vowels: 5

s= 'azcbobobegghakl'#added for testing
y = 0
for x in s:
    if x in "aeiou":
        y+=1
print ("Number of vowels: " + str(y))

#%% Problem set 1.2
#Assume s is a string of lower case characters.
#Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print
#Number of times bob occurs is: 2

s = 'azcbobobegghaklbob'#added for testing
start_index = 0
end_index = 3
count = 0
while end_index < (len(s)+1):
    if s[start_index:end_index] == 'bob':
        count+=1
        start_index +=1
        end_index+=1
    else:
        start_index +=1
        end_index+=1
print('Number of times bob occurs is: ' + str(count))
#%% Problem set 1.3
#Assume s is a string of lower case characters.
#Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print
#Longest substring in alphabetical order is: beggh
#In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print
#Longest substring in alphabetical order is: abc
#Note: This problem may be challenging. We encourage you to work smart. If you've spent more than a few hours on this problem, we suggest that you move on to a different part of the course. If you have time, come back to this problem after you've had a break and cleared your head.

s = 'pvsryaozbbljuggizpi'#added for testing
current=s[0]
result=s[0]
for x in s[1:]:
    if x>=current[-1]:
        current+=x
        if len(current) > len(result):
            result = current
        elif len(current) == len(result):
            result = result
    else:
        current = x
print ('Longest substring in alphabetical order is: '+ result) 
#%% Problem set 1.3 as a function
def longest_substring(s):
    current=s[0]
    result=s[0]
    for x in s[1:]:
        if x>=current[-1]:
            current+=x
            if len(current) > len(result):
                result = current
            elif len(current) == len(result):
                result = result
        else:
            current = x
    return print ('Longest substring in alphabetical order is: '+ result)
    
longest_substring(s)

