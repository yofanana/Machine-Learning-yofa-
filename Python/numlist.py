
import random
import numpy as np
#1.1
n=10
numLits=list(range(1,n+1))

print("list: ",numLits)
print("{}{}".format("the 3rd: ", numLits[2]))
print("{}{}".format("the 5th: ", numLits[4]))
numLits.insert(3,25)
print("{}{}".format("add 25: ", numLits))
numLits.pop()
print("{}{}".format("delete the last item : ", numLits))
print("{}{}".format("list size : ",len(numLits)))
print("{}{}".format("list average : ",np.mean(numLits)))
print("{}{}".format("list max : ",max(numLits)))
numLits.sort()
print("{}{}".format("sort list : ",numLits))
