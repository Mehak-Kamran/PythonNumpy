#import numpy
import numpy as np
#creating one,two and three dim array
a=np.array([5,7],dtype=np.float64)
b=np.array([[1,2],[3,4],[5,6],[4,7]])
#1 layer
d=np.array([[[3,4],[5,7],[7,9]]])
#two layers
c=np.array([[[3,4],[5,7],[7,9]],[[5,3],[4,7],[3,3]]])
#finding dim of array
print(a.ndim,b.ndim,c.ndim)
#type of array
print(a.dtype,b.dtype)
#size of item
print(a.itemsize,b.itemsize)
#total no of elem in array
print(a.size,b.size,c.size)

print(a.shape,b.shape,c.shape,d.shape)