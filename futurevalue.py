years = input("How many years do you want to calculate for?\n")
money = input("Enter the amount of money you're investing:\n")
years = int(years) + 1
money = float(money)
currentyear = 1
def futureValue(years, money):
    for i in range(1, years):
        money = money*1.055
        print("Money is equal to %f" % (money))
futureValue(years, money)