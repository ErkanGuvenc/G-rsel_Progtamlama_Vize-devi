#soru 3 = Girilen bir string ifade de bulunduğundan bir önceki ve sonraki karakteri ekrana getirme

metin=input("Bir Cümle Giriniz...:")
ara=input("Aranacak Kelimeyi Giriniz...:")

ymetin = list(metin)

indis = metin.find(ara)
sonuc =""

if (indis-1) >= 0 :
	sonuc += ymetin[indis-1]
sonuc += ara
if (indis+len(ara)) <= len(ymetin) -1:
	sonuc += ymetin[indis+len(ara)]

print("Aradığınız kelimenin bir önceki ve bir sonraki değeri :", sonuc)