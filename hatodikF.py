# 6 feladat
print("Adj meg két egész számot:")
szam_1 = int(input("1.szám: "))
szam_2 = int(input("2.szám: "))

osszeg = szam_1 + szam_2
kulomb = szam_1 - szam_2
szor = szam_1 * szam_2
hanyad = szam_1 / szam_2
hatvany1 = szam_1 ** szam_2
hatvany2 = szam_2 ** szam_1

szam_1 = str(szam_1)
szam_2 = str(szam_2)

print(szam_1+"+"+szam_2+"="+str(osszeg))
print(szam_1+"-"+szam_2+"="+str(kulomb))
print(szam_1+"*"+szam_2+"="+str(szor))
print(szam_1+"/"+szam_2+"="+str(hanyad))
print(szam_1+"^"+szam_2+"="+str(hatvany1))
print(szam_2+"^"+szam_1+"="+str(hatvany2))