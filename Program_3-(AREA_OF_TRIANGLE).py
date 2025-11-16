# IN THIS PROGRAM WE WILL FIND THE AREA OF THE TRIANGLE
# !!! HERE WILL FIND THE AREA OF THE TRIANGLE IF WE HAVE ALL THE SIDES !!!

"""Semi perimeter (s) = (a + b + c) / 2

Area = square root of (s * (s - a) * (s - b) * (s - c))"""

a = int(input("Please enter the 1st side: "))
b = int(input("Please enter thr 2nd side: "))
c = int(input("Please enter the 3rd side: "))

s = (a + b + c) / 2
area = (s * (s - a) * (s - b) * (s - c)) ** 0.5 # "**" to find the power
print ("Area of the Triangle is", round(area, 4)) # round function is used to round the value, means 10.8 -> 10
