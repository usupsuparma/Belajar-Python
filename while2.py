angka = 0
cari = int(input("masukan angka"))
while angka < cari:
    if angka is cari:
        print("angka di temukan", angka)
        print(cari)
        angka += 1
        break

    print("angka adalah ",angka)
    angka +=1
else:
    print("angka terakhir dari loop: ",angka)

print("ini diluar looping")