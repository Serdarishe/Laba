import math

# 1
def rad(deg):
    return math.radians(deg)
print(rad(15))

# 2
def trap():
    hght = int(input("Height: "))
    fstv = int(input("Base, first value: "))
    scdv = int(input("Base, second value: "))
    return (f"Expected Output: {hght * (fstv + scdv)/2}")
print(trap())

# 3
def regul():
    numsid = int(input("Input number of sides: "))
    lensid = int(input("Input the length of a side: "))
    apoth = (lensid/(2*math.tan(math.pi/numsid)))
    return f"The area of the polygon is: {(numsid*lensid*apoth)/2}"
print (regul())

# 4
def parall():
    lb = int(input("Length of base: "))
    hp = int(input("Height of parallelogram: "))
    return f"Expected Output: {lb*hp}"
print(parall())