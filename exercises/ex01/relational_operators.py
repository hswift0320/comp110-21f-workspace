"""This is a program showing relational operators"""

__author__ = "730396987"

left: str = input("Left number")
right: str = input("Right Number")
lessthan: bool= int(left) < int(right) 
greaterorequalto: bool= int(left) >= int(right)
equalto: bool= int(left) == int(right)
notequal: bool= int(left) != int(right)
print("Left-hand side:" + str(left))
print("Right-hand side:" + str(right))

print(left + "<" + right + "is " + str(lessthan))
print(left + ">=" + right + "is " + str(greaterorequalto))
print(left + "==" + right + "is " + str(equalto)) 
print(left + "!=" + right + "is " + str(notequal))