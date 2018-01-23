#TensorFlow.
import numpy as np
my_list = [1, 2, 3]
type(np.array(my_list))
arr = np.array(my_list)
np.arange(0, 11, 2) #goes up to 11, does not include 11.  Shows interval between range.
np.zeros((3, 5))
np.ones(3)
np.ones((3,5))
np.linspace(0, 11, 100) #shows number of points you want between range.
np.random.randint(0, 100, (3, 3))
np.random.normal
np.random.seed(101)
arr = np.random.randint(0, 100, 10)
arr.max()
arr.min()
arr.mean()
arr.argmax() #shows index location of max value.
arr.argmin() #shows index location of min value.
arr.reshape(2, 5)
mat = np.arange(0, 100).reshape(10, 10)
mat[0, 1] #zero-index based.
mat[:, 0]
mat[5, :] #"row, comma, column".  colons show everything.
mat[0:3, 0:3] #start counting at zero.  Up to, not including to last number.
my_filter = mat > 50
mat[my_filter]
mat[mat > 50]

#Dot Products.
a = np.array([1, 2])
b = np.array([2, 1])
dot = 0
for e, f in zip(a, b):
    dot += e*f #returns 4.
