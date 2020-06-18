query = input()
string = query[0]
for i in range(0,len(query)):
    print("Checking %s" % query[i])
    if query[i] == "-":
        string = string + query[i+1]
    i = i + 1
print(string)