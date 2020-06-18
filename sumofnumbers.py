int_number_for_sum  = int(input("How many numbers do you want to enter?"))
list_sumadd = [""]
i = 0
for i in range(1,int_number_for_sum+1):
    x = input("Enter a number...")
    list_sumadd.append(x)
newint = 0
for y in range(1,len(list_sumadd)):
    newint = int(list_sumadd[y]) + int(newint)
print(newint)

#Alternate way
z = int(input("Enter the amount of numbers you want to enter.."))
list_sumadd = [""]
i = 0
while i < (int_number_for_sum+1):
    x = input()
    x = list_sumadd[i]
for y in range(1,len(list_sumadd)):
    newint = int(list_sumadd[y]) + int(newint)
print(newint)






