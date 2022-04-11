from factorOperations import *
from bayesNet import *

domainDict = {"x" : [0,1], "y" : [0,1], "z" : ["yeee", "not yee"], "w" : ["asd", 3]}

a = Factor(["x", "z"], ["y", "w"], domainDict)

print(a)

print(eliminate(a, "z"))



"""
 factor = x,y

x y
x' y
x y'
x' y'
 
 newFactor = x

x	(y, y')
x'




"""