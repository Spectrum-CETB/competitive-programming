#!/usr/bin/env python2	
# https://www.hackerrank.com/challenges/python-quest-1	
for i in range(1,input()):	
    print reduce(lambda x, _: x * 10 + i, range(i), 0)

#Pyramid program in python
a = int(input())
for i in range(1,a):
    print(str(i)*i)
    
