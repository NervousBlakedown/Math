#Broadcasting/Indexing.
import numpy as np
arr = np.arange[0,11]
arr[0:5] = 100
arr #first five elements are now 100.
arr.copy[] #use copy to make second one while keeping original.
#mat[row, column] #row first, column second!
#conditional selection.


#Exercise Answers.
#import numpy as np
import numpy as np
#create array of ten zeros
np.zeros(10)
#create array of ten ones
np.ones(10)
#create array of ten fives
np.ones(10) * 5
#create array of integers from ten to fifty
np.arange(10, 51)
#create array of even integers from 10 to 50
np.arange(10, 51, 2)
#create 3x3 matrix with values from 0 to 8
np.arange(9).reshape(3, 3)
#create 3x3 identity matrix
np.eye(3)
#use numpy to generate random number between 0 and 1
np.random.rand(1)
#use numpy to generate array of 25 random numbers sampled from a standard normal distribution
np.random.randn(25)
#make matrix from 0 to 1, double brackets
np.arange(0, 101).reshape(10, 10) / 100
#create array of 20 linearly spaced points between 0 and 1
np.linspace(0, 1, 20)
#matrix stuff.
mat[:3, 1:2]
mat[3:,:]
#sum of all values in mat
mat.sum()
mat.std()
mat.sum(axis = 0) #axis 0 = sum of rows, axis 1 = sum of columns, no axis = total matrix sum
#use 'seed' to make sure random number generated is same each time
np.random.seed(101)
np.random.rand(1)


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
np.sum(a*b) #gives expected result.
(a*b).sum()
np.dot(a, b) #best way to get expected result.
a.dot(b)
b.dot(a)
amag = np.sqrt((a*a).sum())
amag = np.linalg.norm(a)
cosangle = a.dot(b) / (np.linalg.norm(a) * np.linalg.norm(b))
angle = np.arccos(cosangle)

#dot faster than 'for' loop.
import numpy as np
from datetime import datetime

a = np.randn(100)
b = np.randn(100)
T = 100000

def slow_dot_product(a, b):
    result = 0
    for e, f in zip(a, b)
        result += e*f
    return result

t0 = datetime.now()
for t in xrange(T):
    slow_dot_product(a, b)
dt1 = datetime.now() - t0

t0 = datetime.now()
for t in xrange(T):
    a.dot(b)
dt2 = datetime.now() - t0

print "dt1 / dt2:", dt1.total_seconds() / dt2.total_seconds()

#Matrices.
Z = np.zeros(10) #makes one row of ten zeros.
Z = np.zeros((10, 10)) #makes 10 x 10 array of zeros.
Y = np.ones((10, 10)) #makes 10 x 10 array of ones.
R = np.random.random((10, 10)) #makes 10 x 10 array of random numbers.
G = np.random.randn(10, 10) #single set of parentheses on purpose.
G.mean()
G.var()

#More Matrix Operations.
A = np.array([[1, 2], [3, 4]])
Ainv = np.linalg.inv(A)
Ainv.dot(A) #makes sure inverse is calculated correctly.
A.dot(Ainv) #makes sure inverse is calculated correctly.
np.linalg.det(A) #matrix determinent.
np.diag(A) #prints 'array([1, 4])'.
np.diag([1, 2]) #prints 'array([[1, 0], [0,2]])'
a = np.array([1, 2])
b = np.array([3, 4])
np.outer(a, b) #prints 'array([[3, 4], [6, 8]])'
np.inner(a, b) #prints '11'
a.dot(b) #prints '11'
np.diag(A).sum() #prints '5'
np.trace(A) #prints '5'
X = np.random.randn(100, 3)
cov = np.cov(X) #wrong. Transpose cov first.
cov.shape #prints '(100, 100)'
cov = np.cov(X.T) #correct.
np.linalg.eigh(cov)
np.linalg.eig(cov)

#Solving Linear Systems.
A = np.array([[1, 2], [3, 4]])
b = np.array([1, 2])
x = np.linalg.inv(A).dot(b) #bad solution.
x = np.linalg.solve(A, b) #always use this solution.

#Word Problem.
A = np.array([[1, 1], [1.5, 4]])
b = np.array([2200, 5050])
np.linalg.solve(A, b) #answer: 1500 children, 700 adults.  output = array([1500, 700])

#Organize Data.
X = []
import numpy as np
for line in open("url_goes_here.csv"):
    row = line.split(',')
    sample = map(float, row)
    X.append(sample)
X = np.array(X)
X.shape #output = (100, 3)
