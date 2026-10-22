###
# Calculates the area of a triangle based on the lengths
# of the triangle's sides

import math


def triangle_area(a,b,c):
    semi = (a+b+c)/2
    area = math.sqrt(semi*(semi-a)*(semi-b)*(semi-c))

    return area

num1 = triangle_area(3,4,5)
num2 = triangle_area(5,12,13)
num3 = triangle_area(7,24,25)

print(f'The area of ​​a triangle with sides 3 4 5  is {num1}')
print(f'The area of ​​a triangle with sides 5 12 13  is {num2}')
print(f'The area of ​​a triangle with sides 7 24 25 is {num3}')
