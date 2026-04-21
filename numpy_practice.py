import numpy as np

def section1():
    a = np.array([10,12,14,16])
    print(a)
    zeros_matrix = np.zeros((2,3))
    print(zeros_matrix)
    ones_matrix = np.ones((3,2))
    print(ones_matrix)

    range_arr = np.arange(0,10,2)
    print(range_arr)

def section2():
    arr = np.array([[1,2,3], [4,5,6]])
    arr_float = arr.astype(float)

    print(arr)
    print(arr.dtype)
    print(arr_float.dtype)
    print(arr.size)
    print(arr.ndim)
    print(arr.shape)

def section3():
    # indexing, slicing 
    arr_1d = np.array([10,20,30,40,50])    
    arr_2d = np.array([[1,2,3], [4,5,6], [7,8,9]])

    # print(arr_1d[2])
    # print(arr_1d[1:4])

    print(arr_2d)
    print(arr_2d[1,2])
    print(arr_2d[0:2, 1:3])
    print(arr_2d[:,1])

def section4():
    # aggregation 
    arr = np.array([[1,2,3], [4,5,6]])
    print(arr.sum())
    print(arr.mean())
    print(arr.max())
    print(np.round(arr.std(),4))



if __name__ == "__main__":
    #section1()
    #section2()
    #section3()
    section4()