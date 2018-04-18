
# list sebagai iterable
gorengan= ['bakwan','cireng','tahu','sorabi','tempe goreng']
sayuran= ['kangkung','wortel','tomat','kentang']
buah = ['semangka','jeruk','wortel']

daftar_belanjag = [gorengan,sayuran,buah]

for subBelanja in daftar_belanjag:
    print(subBelanja)
    for komponen in subBelanja:
        print(komponen)
        print(len(komponen))
        for karakter in komponen:
            print(karakter)