import math
#diameter of jar = 10cm
#height of jar = 16cm
#circumference = 2πr
#area of circle = πr²

pi = math.pi
jar_diameter = 10
jar_radius = 5
jar_height = 16
jar_base_area = pi*(jar_radius ** 2)
jar_volume_cm = jar_base_area * jar_height
print(jar_volume_cm)

cookie_diameter = 6
cookie_radius = 3
cookie_height = 2
cookie_base_area = pi*(cookie_radius ** 2)
cookie_volume_cm = cookie_base_area * cookie_height
print(cookie_volume_cm)

increment = int(0)

cookiefit = True

while cookiefit == True:
    print(increment)
    if cookie_volume_cm > jar_volume_cm:
        cookiefit = False
    else:
        jar_volume_cm = jar_volume_cm - cookie_volume_cm
        increment = increment + 1

print("finished")
#MATHS
#
#math.pi
#math.sqrt(2)
#math.sqrt(-1)
#math.sin(0)
#math.sin(math.pi / 2)
#math.log(1)
#math.log(math.e)
#
#
#
#
#
#


