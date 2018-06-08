import sys

data_list = [1,2,3,4,5,6,7,8]
data_tuple = (1,2,3,4,5,6,7,8)

besarList = sys.getsizeof(data_list)
besarTuple = sys.getsizeof(data_tuple)

print(besarList)
print(besarTuple)