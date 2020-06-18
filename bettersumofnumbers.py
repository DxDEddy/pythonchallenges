
maxint = int(input("What's the largest number?"))
i = 0
otherint = 0
for i in range(0,maxint):
    print("maxint = %i" % maxint)
    print("maxint - i = %i" % (maxint-i))
    print("i = %i" % i)
    otherint = maxint + (maxint - i)
    i = i + 1
print(maxint)