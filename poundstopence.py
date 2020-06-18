initial_val = float(input("Enter whatever you want to check"))
checker = True


#check 20
#check 10
#check 5
#check 2
#check 1
#check 50p
#check 20p
#check 10p
#check 5p
#check 2p
#check 1p

while checker == True:
    while initial_val > 20:
        initial_val = initial_val - 20
        print("Divided by 20, intial_val is now %f" % initial_val)
    while initial_val > 10:
        initial_val = initial_val - 10
        print("Divided by 10, intial_val is now %f" % initial_val)
    while initial_val > 5:
        initial_val = initial_val - 5
        print("Divided by 5, intial_val is now %f" % initial_val)
    while initial_val > 2:
        initial_val = initial_val - 2
        print("Divided by 2, intial_val is now %f" % initial_val)
    while initial_val > 1:
        initial_val = initial_val - 1
        print("Divided by 1, intial_val is now %f" % initial_val)
    while initial_val > 0.5:
        initial_val = initial_val - 0.5
        print("Divided by 0.5, intial_val is now %f" % initial_val)
    while initial_val > 0.2:
        initial_val = initial_val - 0.2
        print("Divided by 0.2, intial_val is now %f" % initial_val)
    while initial_val > 0.1:
        initial_val = initial_val - 0.1
        print("Divided by 0.1, intial_val is now %f" % initial_val)
    while initial_val > 0.05:
        initial_val = initial_val - 0.05
        print("Divided by 0.05, intial_val is now %f" % initial_val)
    while initial_val > 0.02:
        initial_val = initial_val - 0.02
        print("Divided by 0.02, intial_val is now %f" % initial_val)
    while initial_val > 0.01:
        initial_val = initial_val - 0.01
        print("Divided by 0.01, intial_val is now %f" % initial_val)

print(initial_val)