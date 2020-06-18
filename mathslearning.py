#Integer Division
#Integer division will perform a normal division as long as it returns an integer. In this case, it would normally output a floating point number, it will output an integer number and assign it the int type.
15 /  4 #= 3.75
15 // 4 #= 3

#Modulo = %
#modulo will print whatever is left of a division. In this case we divide 11 by 4 and we get 3 output.
11 % 4 = 3
10 % 4 = 2
5  % 3 = 2

#Here we can see an example of an optimised fizzbuzz solution using modulo 

int_endnum = 100
for i in range(1,int_endnum):
    if(i%3 == 0 and i%5 != 0):
        print("fizz @ %i" % i)
    elif(i%5 == 0 and i%3 != 0):
        print("buzz @ %i" % i)
    if(i%3 == 0 and i%5 == 0):
        print("fizzbuzz @ %i" % i)
    i = i + 1

#Round()
#Whereas converting a float to an int truncates, this will round correctly to either 0 or a defined number of decimal places.
#sytax:
#round(val, decimal places, default = 0)

round(3.8) = 4
round(6.2) = 6
round(5.325123, 2) = 5.33

#Using the Math module

### ceil() function
#Returns the smallest integer that is greater than or equal to x
#Examples:

math.ceil(-45.17) : -45
math.ceil(100.12) : 101
math.ceil(100.72) : 101
math.ceil(math.pi) : 4


# floor() function
#Returns the smallest integer that is less than or equal to x
#Examples:

math.floor(-45.17) :  -46
math.floor(100.12) :  100
math.floor(100.72) :  100
math.floor(math.pi) :  3

#factorial()
#returns the factorial of x
#Example:
n = input("Enter a number: ")
factorial = 1
if int(n) >= 1:
for i in range(1,int(n)+1):
   factorial = factorial * i
print("Factorial of ",n , " is : ",factorial)

#This gets us this as output:

Enter a number: 5
Factorial of 5 is : 120

#fmod(x,y)
#Returns the remainder when x is divided by y
#Examples
print(math.fmod(25,5))
print(math.fmod(20,3))
print(math.fmod(-20,12))
print(math.fmod(-13,6))

#This gets us this as an output:

0.0
2.0
-8.0
-1.0

#log()
#This returns the logarithm of x, optionally with a base as the second parameter.
print (math.log(14))
print (math.log(14,5))

#This gets us this as an output:

2.6390573296152584
1.6397385131955606

#pow()
#This returns x raised to the power y, this is the same as using "x ** y"
print(pow(4,5)) = 1024
print(4 ** 5)   = 1024

#sqrt()
#returns the square root of the parameter
print(sqrt(x))

#This will result in out output being:

1.41421356237

#Sine, Cosine and Tangent
#We can use functions to return x with all of these operations applied to it.
print(cos(5))
print(sin(5))
print(tan(5))

#That will get us this as an output:

0.28366218546
-0.95892427466
-3.38051500625

#Mathematical Constants
print(math.pi) #Returns the value of pi
print(math.e) # Returns the mathematical constant e

#After inputting that we will get this back

3.14159265359 #pi
2.71828182846 #e
