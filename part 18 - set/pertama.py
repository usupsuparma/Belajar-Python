# set adalah himpunan
# cara membuat set ada dua cara
# bisa langsung deklarasi dengan {

superhero = {"wiro sableng","saras 008", "gundala"}

print(superhero)

# cara deklarasi set ke dua
superHeroKedua = set()

superHeroKedua.add("spiderman")
superHeroKedua.add("hulk")
superHeroKedua.add("iron man")
superHeroKedua.add("Batman")

print(superHeroKedua)


ganjil = {1,3,5,7,9}
genap = {2,4,6,8,}
prima = {2,3,5,7}

#gabungan union
print(ganjil.union(genap))

# irisan
print(ganjil.intersection(prima))