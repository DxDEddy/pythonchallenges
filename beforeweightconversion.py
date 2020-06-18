#Stone to g conversion
conversiontype = input("Do you want to convert Kilos to pounds or vice versa? Enter 's2k' or 'k2s\n")
conversiontype = str(conversiontype)

if conversiontype == "s2k":
    print("s2k")
    quaninput = input("Enter the amount of stone you want to convert: \n")
    quaninput = float(quaninput)
    #starting conversion process
    finalresult = quaninput * 6.35029
    print("%f stone has been converted to %f kilos" % (quaninput, finalresult))
elif conversiontype == "k2s":
    print("k2s")
    quaninput = input("Enter the amount of kilos you want to convert: \n")
    quaninput = float(quaninput)
    # starting conversion process
    finalresult = quaninput * 0.15747304441777
    print("%f kilos has been converted to %f stone" % (quaninput, finalresult))
else:
    print("Something went wrong")



#0.15747304441777