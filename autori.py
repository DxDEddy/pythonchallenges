query = input()
ref = query.split("-")
numb = len(ref)
test = ""
for i in range(0,numb):
    test = test + ref[i][0]

print(test)
