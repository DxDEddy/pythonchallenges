int_endnum = int(input("Enter what you want to end at...\n"))
for i in range(1,int_endnum+1):
    if(i%3 == 0 and i%5 != 0):
        print("fizz @ %i" % i)
    elif(i%5 == 0 and i%3 != 0):
        print("buzz @ %i" % i)
    if(i%3 == 0 and i%5 == 0):
        print("fizzbuzz @ %i" % i)
    i = i + 1