#belajar for else 
number = 1
for i in range(0,11):
    print(i)
    if i is number:
        print('angka ditemukan: ',i)
        break
else:
    print('angka tidak ditemukan')
print('bukan bagian dari loop')