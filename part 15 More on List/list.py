barang = ["mouse","keyboard","gelas"]
print(barang)

#manambahakan item ke dalam list dengan urutan terakhir dari list
barang.append("kabel")
print(barang)

# manambahkan item ke dalam list sesuai posisi yang dinginkan
barang.insert(2,"hp")
print(barang)

# gunakan extend untuk string extreble
barang.extend("aku")
print(barang)

# metode untuk menghitung anggota yang ada di list
hitung = barang.count("gelas")
print("jumlah: ",hitung)

# meremove data dalam list
barang.remove("a")
print(barang)

print("=="*50)
# untuk menukan posisi dari list yang tadinya di ujung jadi di depan
barang.reverse()
print(barang)

print("="*100)
# ini di gunakan untuk mencopy list agar tidak merubah list yang di copy
print(barang)
jenis = barang.copy()
jenis.append("jam tangan")
print(jenis)
print(barang)
