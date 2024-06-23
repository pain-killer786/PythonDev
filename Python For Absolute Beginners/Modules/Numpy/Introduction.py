#What is NumPy?
#NumPy is a Python library used for working with arrays.

#It also has functions for working in domain of linear algebra, fourier transform, and matrices.

#Why Use NumPy?
#In Python we have lists that serve the purpose of arrays, but they are slow to process.

#NumPy aims to provide an array object that is up to 50x faster than traditional Python lists.

#The array object in NumPy is called ndarray, it provides a lot of supporting functions that make working with ndarray very easy.

#Arrays are very frequently used in data science, where speed and resources are very important.

#Why is NumPy Faster Than Lists?

#NumPy arrays are stored at one continuous place in memory unlike lists, so processes can access and manipulate them very efficiently.

#This behavior is called locality of reference in computer science.

#This is the main reason why NumPy is faster than lists. Also it is optimized to work with latest CPU architectures.

#alias: In Python alias are an alternate name for referring to the same thing. Create an alias with the 'as' keyword while importing.

#Importing Numpy

import numpy as np  # 1-D array
arr=np.array([1,2,3,4,5]) 
print(arr)
print(np.__version__)


#Create a NumPy ndarray Object
#NumPy is used to work with arrays. The array object in NumPy is called ndarray.We can create a NumPy ndarray object by using the array() function.
arr=np.array([1,2,3,4,5]) 
print(arr)
print(type(arr))


# 0-D Arrays
# 0-D Arrays, or Scalars are the elements in an array. Each value in an array is a 0-D array.

arr=np.array([42]) 
print(arr)

# 2-D Arrays
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)

#3-D Arrays
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(arr)

#Checking number of dimenstions -> 'ndim' attribute returns an integer and tells us how many dimensions the array have
a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

#Higher Dimensional Arrays
#An array can have any number of dimensions.When the array is created, you can define the number of dimensions by using the ndmin argument.

arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print('number of dimensions :', arr.ndim)

# Accessing the elements in an 1-D Array
print(arr[0])

# Accessing the elements in an 2-D Array
print(arr[0,1])

# Accessing the elements in an 3-D Array
print(arr[0,2,3])

#Array Slicing -> Same as list

# Datatypes in Numpy
 #i-integer; b - boolean; u - unsigned integer; f - float; c - complex float; m - timedelta; M - datetime; O - object; S - string; U - unicode string; V - fixed chunk of memory for other type ( void )
 
#Checking Datatypes of an array -> use 'dtype' attribute
x = np.array(['apple','orange'])
print(x.dtype)

#Creating Arrays With a Defined Data Type
# We use the array() function to create arrays, this function can take an optional argument: 'dtype' that allows us to define the expected data type of the array elements:

import numpy as np

arr = np.array([1, 2, 3, 4], dtype='S4')

print(arr)
print(arr.dtype)

#Converting Data Type on Existing Arrays

#The astype() function creates a copy of the array, and allows you to specify the data type as a parameter.

#The data type can be specified using a string, like 'f' for float, 'i' for integer etc. or you can use the data type directly like float for float and int for integer.

import numpy as np

arr = np.array([1.1, 2.1, 3.1])

newarr = arr.astype('i')

print(newarr)
print(newarr.dtype)