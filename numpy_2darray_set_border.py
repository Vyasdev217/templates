import numpy as np
arr=np.zeros((5,5))
def numpy_2darray_border(arr,val):
    for i in range(len(arr)):
        arr[i][0]=val
        arr[0][i]=val
        arr[i][len(arr)-1]=val
        arr[len(arr)-1][i]=val
    #print(arr)
    return arr
print(numpy_2darray_border(arr,-1))
