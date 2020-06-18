import sys
initial_val = float(input("Enter whatever you want to check"))
checker = True

subtract_val_array = [20,10,5,2,1,0.5,0.2,0.1,0.05,0.02,0.01]
increment = 0
increment = int(increment)
print("Position %i of array is equal to: %i" % (increment, subtract_val_array[increment]))

while checker == True:
    while initial_val >= subtract_val_array[increment]:
        initial_val = initial_val - subtract_val_array[increment]
        print("Intial Value is now %f " % initial_val)
        while initial_val < subtract_val_array[increment]:
            print("Incrementing the array by one. Array index is now %i, value being checked for is: %f" % (increment,subtract_val_array[increment]))
            print("Current money is %f" % initial_val)
            if increment < 10:
                increment = increment + 1
            elif initial_val == 0:
                #test
                print("Stop")
            else:
                print("increment is already at 8")
            
    if initial_val == 0:
        print("Finished with intial_val = %f" % initial_val)
        exit()