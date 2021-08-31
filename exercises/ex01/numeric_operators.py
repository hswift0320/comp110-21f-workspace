"""This is a program showing numerical operators"""

__author__ = "730396987"

left: str = input("Left number:")
right: str = input("Right Number:")
multiple: int= int(left) * int(right)
division: float= float(left) / float(right)
floor: int= int(left) // int(right)
modulus: int= int(left) % int(right)

print("Left-hand side:" + str(left))
print("Right-hand side:" + str(right))
print(left + "**" + right + "is " + str(multiple)) 
print(left + "/" + right + "is " + str(division))
print(left + "//" + right + "is " + str(floor))
print(left + "%" + right + "is " + str(modulus))
