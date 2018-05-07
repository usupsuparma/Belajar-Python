#fungsi argument sederhana
def siswa(nama):
    print("nama siswa adalah: ",nama)

siswa("usup")

#fungsi argument 2 argument
def guru(nama,pelajaran):
    print("nama guru adalah: ",nama)
    print("mengajar pelajaran: ",pelajaran)
guru("uned", "matematika")

def pejagaSekolah(nama,usia=20,sifat='galak'):
    print("nama penjaga: ",nama)
    print("usia",usia)
    print("sifatnya: ",sifat)
pejagaSekolah("udin")