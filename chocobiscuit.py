#What are we outputting?
    #Thickness of slice
    #Area of biscuit
    #Calories per slice
    #Number of whole slices the brother can eat
#We need to grab
    #length of baking tray in cm
    #width of baking tray in cm
    #How many slices the mixture should be divided into

#each squrare cm of biscuit contins 3 calories
#topping contains 950 calories total

float_tray_length = float(input("Please enter the width of the tray\n"))
float_tray_width = float(input("Please enter the width of the tray\n"))
int_amount_slices = int(input("How many slices should the mixture be divided into?\n"))


#ANSWER 1 - thickness of each slice
float_thickness_of_slice = float_tray_length / int_amount_slices
float_thickness_of_slice = float(float_thickness_of_slice)
print("Each slice is %fcm thick\n" % float_thickness_of_slice)

#ANSWER 2 - area of each slice
float_area_of_whole_cm2 = float(float_tray_length*float_tray_width)
float_area_of_slice_cm2 = float(float_area_of_whole_cm2/int_amount_slices)
print("The area of the whole biscuit is %fcm2\n" % float_area_of_whole_cm2)
print("The area of one slice is %fcm2\n" % float_area_of_slice_cm2)

#ANSWER 3 - number of calories in each slice
#Biscuit
float_calories_per_slice = float_area_of_slice_cm2 * 3
print("There are this many calories per slice %f\n" % float_calories_per_slice)
#Sauce
float_sauce_calories_per_cm2 = 950 / float_area_of_whole_cm2
print("There are %f calories per cm2\n" % float_sauce_calories_per_cm2)
float_sauce_calories_per_slice = float_sauce_calories_per_cm2 * float_area_of_slice_cm2
print("there are %f calories per slice\n" % float_sauce_calories_per_slice)
float_total_calories_per_slice = float_sauce_calories_per_slice + float_calories_per_slice
print("There is a total of %f calories per slice\n" % float_total_calories_per_slice)

#ANSWER 4 - maxmimum number of slices the brother can eat
maxcal = 1200
startcal = 0
i = 0
inc = 0
inc = int(inc-1)
#print(float_total_calories_per_slice)
while i < maxcal:
    inc = inc + 1
    i = i+float_total_calories_per_slice
    #print(float_total_calories_per_slice)
    #print(i)
    

print("He can have %i slices" % inc)
