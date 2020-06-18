# -*- coding: utf-8 -*-
from random import randrange
import linecache
f = open("wordlist.txt", "r")
output = ""
arr_mixup = ["!","*","-","1","2","3","4","5","6","7","8","9","0","!","*","-","1","2","3","4","5","6","7","8","9","0"]

while len(output) <= 16:
    random = randrange(1,8096)
    print("Random = %i" % random) 
    lines = linecache.getline("wordlist.txt", int(random))
    lines = lines.rstrip('\n')
    print("Fileword = %s" % lines)
    output = output + lines
    print("Output = %s" % output)

passlength = len(output)
arr_output = list(output)

for i in range(0,5):
    changechar = randrange(0, passlength)
    arr_output[changechar] = arr_output[changechar].upper()

for i in range(0,5):
    changechar = randrange(0, passlength)
    arr_output[changechar] = arr_mixup[randrange(0,len(arr_mixup)-1)]
    i = i + 1

finaloutput = "".join(arr_output)
print("Here's the final result: %s" % finaloutput)
print(len(output))