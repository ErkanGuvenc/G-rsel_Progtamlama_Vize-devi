
#Soru 1 :Girilen bir string ifadenin email adresi olup olmadığını doğrulayan komutun string metodlarını kullanmadan yazılımı:

email= input(str("Lütfen bir email adresi giriniz...: "))

print("------------------------------")

for i in email:
    if i=="@":
        print("Bu bir email adresidir.")
        break
else:
    print("Bu bir email adresi değildir")

print("------------------------------")