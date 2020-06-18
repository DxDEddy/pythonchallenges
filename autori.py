query = input()
ref = query.split("-")
test = ""
numb = len(ref)
for i in range(0,numb):
    test = test + ref[i][0]
print(test)