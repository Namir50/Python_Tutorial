'''ABC is a right triangle, 90 degree  at .
Therefore, ABC is 90 degree
Point M  is the midpoint of hypotenuse AC
You are given the lengths  AB and AC
Your task is to find MBC   in degrees.
Input Format
The first line contains the length of side AB 
The second line contains the length of side BC'''

import math

def find_angle_MBC(AB, BC):
    angle_MBC_deg = round(math.degrees(math.atan(AB / BC)))
    return f'{angle_MBC_deg}\u00b0'

# Input lengths of sides AB and BC from the user
AB = float(input("Enter the length of side AB: "))
BC = float(input("Enter the length of side BC: "))

# Find and print the angle MBC
print(find_angle_MBC(AB, BC))
