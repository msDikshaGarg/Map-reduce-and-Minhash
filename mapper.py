#!/usr/bin/env python

##OUTPUT in dg3392_DikshaGarg_Midterm1/src##
import sys 
import random
from heapq import *

#random sort reference: https://en.wikipedia.org/wiki/Reservoir_sampling#With_random_sort
recipe_queue=[] #creating the queue
count = int(sys.argv[1]) #setting the length of reservoir
for i in sys.stdin:
    i = i.rstrip()
    if i == '':
        continue
    id_recipe = random.random() #making random ids for words in the recipes
    if len(recipe_queue) < count: #if length is less than the length of reservoir
        heappush(recipe_queue,(id_recipe,i)) # push the word and the id as (key,value) in the queue
    else:
        if id_recipe > recipe_queue[0][0]:  #if random number is greater than the min element
            heapreplace(recipe_queue,(id_recipe,i)) #we replace it with the new element 

#sending output to reducer
for i, j in recipe_queue:
    print('%f %s' %(i, j))