# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 14:37:59 2018

@author: Albert Prat
"""
import re

def SH(string, m=257, C=1024):
# m represents the estimated cardinality of the items set
# C represents a number that is larger that ord(c)
    hash=0
    for i in range(len(string)):
        hash = (hash * C + ord(string[i])) % m
    return hash


l = []
tags = []
for i in range(0,len(tweets_list)):
    tweet = tweets_list[i]
    l.append(tweet.split(sep=" "))
    
    
for i in range(0, len(l)):
    iterable_l = l[i]
    for j in range(0,len(iterable_l)):
        i_j = iterable_l[j]
        m = re.search(r"@\w+", i_j)
        if m!=None:
            tags.append(m.group())
        else:
            pass