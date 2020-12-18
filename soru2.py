
#Soru 2 :Girilen bir string ifadenin URL adresi olup olmadığını doğrulayan komutun string metodlarını kullanmadan yazılımı:

adres=input("Bir URL adresi giriniz... : ")

site=list(adres)

print("------------------------------")
ara=list("www.") # Url www. adresi başlayacağı için bu sorgulanmıştır.

if site[0:4]==ara[0:4]:
    print(adres, "/Bu bir URL adresidir.")

else: print(adres, "/Bu bir URL adresi değildir.")

print("------------------------------")