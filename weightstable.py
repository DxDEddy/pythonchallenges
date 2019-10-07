kilos = 10
pounds = 0
def weightstable(kilos, pounds):
    print("|KG: %f | Pnd: %f |" % (kilos, pounds))

while kilos<=100:
    pounds = kilos * 2.20462
    weightstable(kilos, pounds)
    kilos = kilos + 10
