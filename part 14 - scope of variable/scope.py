# scope variable global
namaKucing = "emmpus"
makananKucing = "tempe"
def rubahNamaKucing(namaKucingBaru):
    global namaKucing
    namaKucing = namaKucingBaru
    print(namaKucing)
def kasihMakanKucing(makan, nama):
    global namaKucing,makananKucing
    namaKucing = nama
    makananKucing = makan
    print("Nama kucing baru: ",namaKucing,"makannan kucing baru: ",makananKucing)
rubahNamaKucing("emmeong")
kasihMakanKucing("telor", "mudin")