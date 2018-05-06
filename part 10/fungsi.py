def suaraAyam():
    print("kukuruyuk")
def hargaAyam():
    print("harga Ayam adalah Rp. 20.000.00")
    harga = 20000
    return harga
def belanja(kg):
    print("anda sedang belanja ayam sebanya ",kg,"kg")
    hargatotal = kg * hargaAyam()
    print("total belanja: ",hargatotal)
belanja(3.56)