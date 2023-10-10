import numpy
#1D array
arr=numpy.array([1,3,4,5])
print(arr)
#2D array
arr1=numpy.array([[1,2,3],[7,4,5]])
print(arr1)
print(arr1.ndim)
#3D array
arr2=numpy.array([[[1,2,3],[4,5,6]],[[7,8,9],[6,5,4]]])
print(arr2)
print(arr2.ndim)

#3D matrix
a = numpy.matrix('[1, 2, 3; 4, 5, 6; 7, 8, 9]')
print(a)
a_mean=a.mean()
print(a_mean)
#2D matrix
b=numpy.array('[1,2;5,6]')
print(b)
#reverse 1D array
#1 method
print("1D array:",arr)
res=arr[::-1]
print("reverse of 1D array:",res)
#2 mehod using reverse function
print("1D array:",arr)
res1=numpy.flip(arr)
print("reverse of 1D array:",res1)
#slicing in array
arr3=numpy.array([1,2,3,4,7,8,9])
print(arr3[:])
print(arr3[0:5])
print(arr3[:7])
print(arr3[-5:-2])
print(arr3[::2])
print(arr3[:6:3])