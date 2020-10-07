#!/usr/bin/env python

##OUTPUT in dg3392_DikshaGarg_Midterm1/src##
import sys 

count = int(sys.argv[1]) #setting the length of reservoir
print_queue = [] #making a priority queue for printing the output

for k in sys.stdin:
    (i,j) = k.split(' ',1) #separating the key value pairs
    print_queue.append((i,j))#appending the values in the queue
sorted(print_queue,key=lambda l:l[0], reverse=True) #sorting the list in reverse

for i,j in print_queue:  #printing the output of the queue
    print(j)
    count = count - 1
    if count == 0:
        break