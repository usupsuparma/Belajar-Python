from collections import deque

antrian = deque([1,2,3,4,5])
print("Data Sekarang: ",antrian)

# menambahakan data pada antrian
antrian.append(6)
print("data masuk: ",6)
print("Data Sekarang: ",antrian)
jumlah = input("masukan jumlah data")
j = int(jumlah)
n = int(input("mauskan nilai n: "))
for i in  range(n,j) :
    antrian.append(i)
    print("data yang dimasukan: ",i)
    print("data Sekarang: ",antrian)


# mengurangi antrian
print("====="*100)
out = antrian.popleft()
print("data keluar: ",out)
print("data sekarang: ",antrian)