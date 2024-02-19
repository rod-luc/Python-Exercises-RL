
"""this is the summary
  
  """

def array123(nums):
  rta = False
  for i in range(len(nums)):
    if i+2 <= len(nums):
      if nums[i]==1 and nums[i+1]==2 and nums[i+2]==3:
        rta = True
  return rta    

print(array123([1, 2, 3]))
print(array123([1,1, 2, 3]))
print(array123([1, 2, 2]))

import numpy as np
 
# Creating a vector from a list
vector = np.array([1, 2, 3])
print("Vector:", vector)
 
# Vector addition
vector2 = np.array([4, 5, 6])
sum_vector = vector + vector2
print("Vector addition:", sum_vector)
 
# Scalar multiplication
scalar = 2
scaled_vector = vector * scalar
print("Scalar multiplication:", scaled_vector)

print("Vector multiplication: ", vector * vector2 )
