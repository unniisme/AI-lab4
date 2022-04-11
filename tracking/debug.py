from factorOperations import *
from bayesNet import *

a = Factor(["x"], ["y"], {"x": [0,1], "y": [0,1]})
b = Factor(["y"], [],{"x": [0,1], "y": [0,1]})

print(joinFactors([a,b]))