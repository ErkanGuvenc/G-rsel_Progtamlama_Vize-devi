# soru 4= üç basamaklı birbirinden farklı kaç tane sayı oluştuğunu bullan ve ekrana yazdıran program:

liste=[]

for i in range(100,1000):
    if len(set(str(i)))==len(str(i)):
        liste.append(i)

for sayi in liste:
    print("Sayılar : ", sayi)

print("Toplam sayı", len(liste), "addetir.")