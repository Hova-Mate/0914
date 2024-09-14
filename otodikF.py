# 5 feladat
print("Adj meg két egész számot:")
szam_1 = int(input("1.szám: "))
szam_2 = int(input("2.szám: "))

osszeg = szam_1 + szam_2
kulomb = szam_1 - szam_2
szor = szam_1 * szam_2
hanyad = szam_1 / szam_2
hatvany1 = szam_1 ** szam_2
hatvany2 = szam_2 ** szam_1

print("Összegük: "+str(osszeg))
print("Külömbségük: "+str(kulomb))
print("Szorzat: "+str(szor))
print("Hányadosuk: "+str(hanyad))
print("Hatványuk: "+str(hatvany1))
print("Hatványuk: "+str(hatvany2))