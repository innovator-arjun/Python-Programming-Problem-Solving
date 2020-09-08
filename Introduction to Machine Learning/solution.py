import numpy as np


def make_array_from_list(some_list):
    res=np.array(some_list)
    return res



def make_array_from_number(num):
    result = np.array((num,),int)
    return result



class NumpyBasics:
    def add_arrays(self, a, b):
        res=np.add(a,b)
        return res

    def add_array_number(self, a, num):
        return a+num

    def multiply_elementwise_arrays(self, a, b):
        return a*b

    def dot_product_arrays(self, a, b):
        res=np.dot(a,b)
        return res

    def dot_1d_array_2d_array(self, a, m):
        # consider the 2d array to be like a matrix
        res=a.dot(m)
        return res
