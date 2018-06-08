import timeit

data_list = timeit.timeit(stmt="[1,2,3,4,5]", number=10000)
data_tuple = timeit.timeit(stmt="(1,2,3,4,5)", number=10000)

print("waktu list: ",data_list)
print("waktu tuple: ", data_tuple)