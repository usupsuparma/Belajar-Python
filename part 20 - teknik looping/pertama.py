# teknik looping

nama_band = ['Payung Teduh',
             'Fourtwnty',
             'Dialog Dini Hari',
             'Mr. Sonjaya',
             'Parahyena']
kumpulan_lagu = ['Akad',
                'Zona Nyaman',
                'Rumahku',
                'Sang Filsuf',
                'Sindoro']
# enumarate
for index , band in enumerate(nama_band):
    print(index,":",band)
print("="*100)

# zip
for band,lagu in zip(nama_band,kumpulan_lagu):
    print(band,'menyanyikan lagu:',lagu)
print("="*100)

# set
playlist = {"baby baby",'ada apa cinta', 'cenat-cenut','jaran goyang'}
for lagu in playlist:
    print(lagu)
    # file hasil looping tidak di urutkan
print('='*100)
for lagu in sorted(playlist):
    print(lagu)
print('='*100)
# dictionary
playlist2 = {'Payung Teduh':'akad',
             'Fourtwnty':'Zona Nyaman',
             'dialog dini hari':'Rumahku'}
for i in playlist2.keys():
    print(i)
    # menggunakan key
print('='*100)
for i in playlist2.values():
    print(i)
    # menggunakan values
print('='*100)
for i in playlist2.items():
    print(i)
    # menggunakan item
print('='*100)
for i , v in playlist2.items():
    print(i,"lagunya:",v)