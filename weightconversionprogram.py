#--------------------------------------------------------
# A kilograms to pounds conversion program
# Edward Gray
# up939720
# Autumn Teaching Block 2019
#--------------------------------------------------------

#pounds to kg conversion
conversiontype = input("Do you want to convert Kilos to pounds or vice versa? Enter 'p2k' or 'k2p'\n")
conversiontype = str(conversiontype)

def conversionroutine(conversionval, endresult):
    quaninput = input("Enter the amount of pounds you want to convert: \n")
    quaninput = float(quaninput)
    finalresult = quaninput * conversionval
    print("Your value has been converted, the result is %f %s" % (finalresult, endresult))

if conversiontype == "p2k":
    endresult = "kilos"
    conversionval = 0.453592
    conversionroutine(conversionval, endresult)
elif conversiontype == "k2p":
    endresult = "pounds"
    conversionval = 2.20462
    conversionroutine(conversionval, endresult)
else:
    print("An exception has occured")

