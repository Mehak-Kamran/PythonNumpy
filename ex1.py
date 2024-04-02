#import numpy
import numpy as np
#creating one,two and three dim array
a=np.array([5,7],dtype=np.float64)
b=np.array([[1,2],[3,4],[5,6],[4,7]])
c=np.array([[[3,4],[5,7],[7,9]]])
print(a.ndim,b.ndim,c.ndim)
#type of array
print(a.dtype)
print(b.dtype)
