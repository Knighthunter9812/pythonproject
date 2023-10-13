import numpy
#1D array
arr=numpy.array([1,3,4,5,6,2,8,5])
print(arr)
print(arr.dtype)
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
#Mean of matrix
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
#frequency of non zero element in 1D array
count = numpy.count_nonzero(arr == 5)
print(count)
#method 2
count_arr = numpy.bincount(arr)
print(count_arr[5])
#reverse a column in 2D array
print(numpy.fliplr(arr1))
#reverse a row in 2D array
print(numpy.flipud(arr1))
#split the elements wih spaces
x = numpy.array(['I AM AYUSH JAKHAR'], dtype=numpy.str_)
print(x)
r = numpy.char.split(x)
print(r)
#join string by seperator
array1=numpy.array(['kurkure','chips'])
separray = numpy.array(['_'])
newarray= numpy.char.join(separray, array1)
print(newarray)
#extract elemnts from 1D array
condition=(arr%2==0)
print(numpy.extract(condition, arr))
#remove column that contain non-numeric values
n_arr = numpy.array([[10.5, 22.5, numpy.nan],[41, 52.5, numpy.nan]])
print(n_arr[:,~numpy.isnan(n_arr).any(axis=0)])
#stack two 3*3 array vertically
ar1 = numpy.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])

ar2 = numpy.array([[10, 11, 12],[13, 14, 15],[16, 17, 18]])

# Stack them vertically
stacked_array = numpy.vstack((ar1, ar2))
print(stacked_array)
#euclidean distance
p1 = numpy.array([1, 2, 3])
p2 = numpy.array([4, 5, 6])

# Calculate Euclidean distance
euclidean_distance = numpy.linalg.norm(p1 - p2)
print(euclidean_distance)