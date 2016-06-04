# -*- coding: utf-8 -*-
'''
SIMULATION OF MARKOV-STYLE PROCESS FOR PROCESS MINING TOOLS
This software simulate process traces for process mining techniques
when actual process data is not available
    Copyright (C) 2015  Gerald Gendron
    gerald.gendron@gmail.com

    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License, version 2.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    
This General Public License does not permit incorporating your program into
proprietary programs.  If your program is a subroutine library, you may
consider it more useful to permit linking proprietary applications with the
library.  If this is what you want to do, use the GNU Lesser General
Public License instead of this License.
'''

"""
Created on Thu Oct  8 21:23:14 2015
@author: Jay Gendron
"""

'''
Here are some elements researched and used in this psuedocode

for a list l

import collections : this is an aggregation function
collections.Counter(l)

import random : provides functions for random numbers
random.seed(anInteger)
int(random.uniform(min,max,step))

l.append('itemToAdd')
','.join(l)   collapses list into a string
'''


'''PSEUDOCODE FOR SIMULATION
Create an empty list <traces>

Load key:value dictionary of allowed <paths> from footprint

Set <start> to string of first path activity

Set <end> to string of terminating path activity

Set <event> = <start>
    
For Loop: range is number of simulated traces desired

    Set list <trace> as <start>

    WHILE <event> != <end>
    set <max> to (length + 1) of values from <paths> associated with <event>
    pull random element from values and assign to <event>
    append <event> to <trace>
    

    When WHILE ends
    ->join <trace>
    ->append <trace> to <traces>
    -><event> = <start>
    
When For ends
    count frequency of traces
    write to file   
'''

##Start of code
import collections
import pandas as pd
import numpy as np

'''Test footprint

paths = {'a':['b','c'],'b':['c','d','p'],'c':'p','d':'e','e':'p'}

prb = {'a':[.5, .5],
        'b':[.34, .33, .33],
        'c':[1.0],
        'd':[1.0],
        'e':[1.0]}

answer: dict_keys(['a,b,d,e,p', 'a,c,p', 'a,b,c,p', 'a,b,p'])
'''
# More Complicated Path - nominal data
paths = {'a':['b','f','g','i'],'b':['c','d','f','g','i','m'],
         'c':['d','e','f','g','i'],'d':['e','f','g','i'],
         'e':['f','g','i'],'f':['c','d','e','g','h','i','m'],
         'g':['c','d','e','h','i','m'],'h':['i','m'],
         'i':['b','j','k','m','n'],'j':['k','l','m','n'],
         'k':['l','m','n'],'l':['m','n'],
         'm':['j','k','l','n','p','m'],'n':['j','k','l','p','m'],
         'o':'p'} 
         
prb = {'a':[.7,.01,.2,.09],
        'b':[.5,.1,.25,.05,.05,.05],
        'c':[.12,.03,.3,.3,.25],
        'd':[.05,.5,.4,.05],
        'e':[0.3, 0.4,0.3],
        'f':[0.09,0.09,0.02,0.02,0.13,0.64,0.01],
        'g':[0.09,0.09,0.02,0.15,0.64,0.01],
        'h':[0.6,0.4],
        'i':[0.1,0.5,0.250,0.075,0.075],
        'j':[0.25,0.25,0.25,0.250],
        'k':[0.450,0.150,0.400],
        'l':[0.500,0.500],
        'm':[0.2,0.2,0.02,0.02,0.01,0.55],
        'n':[0.09,0.09,0.02,0.7,0.1],
        'o':[1.0]}
         
#initial conditions
start = 'a'
end = 'p'
event = start

curve = [] #list for diagnostics tally
repli = [100,300,1000,3000,10000,30000,100000,300000]#,1000000,3000000]
count = [] #collect unique traces for plot

for e in repli:
    traces = []
    for i in range (0,e):
        trace = [start]

        while (event != end):
            max = len(paths[event])
            plook = prb[event]
            idx = int(np.random.choice(range(max),1,p=plook))
            newEvent = paths[event][idx]
            trace.append(newEvent)
            event = newEvent
           
        traces.append(','.join(trace))
        event = start

    counter = collections.Counter(traces)
    count.append(len(counter.keys()))
    print(counter)

##    write to file

df = pd.DataFrame.from_dict(counter, orient='index')
sorted = df.sort()

filenm = ("Sorted Markov Traces.txt")
f = open(filenm, "w")
f.write("25 Most Common Traces\n\n")
d = counter.most_common(25)
f.write(str(d))
f.write("\n\n")
f.write("All traces ordered by activity")
with pd.option_context('display.max_rows', len(counter.keys())+1):
    f.write(str(sorted))

# Diagnostics
print("Replications: ", repli)
print("Unique Traces: ", count)

remove =[]
for k in counter.keys():
    if counter[k] == 1:
        remove.append(k)
        
for r in range (0,len(remove)):
    del counter[remove.pop()]
        
print("Last Replication: ", repli[-1])
print("Unique Traces > 1: ", len(counter.keys()))
print("Removed",(count[-1] - len(counter.keys())),"singletons.")        
  
df = pd.DataFrame.from_dict(counter, orient='index')
sorted = df.sort()
  
f.write("\n\n")
f.write("Remaining traces ordered by activity")
with pd.option_context('display.max_rows', len(counter.keys())+1):
    f.write(str(sorted))
f.close()
