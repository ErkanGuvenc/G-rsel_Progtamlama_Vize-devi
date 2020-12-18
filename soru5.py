def kodTipi(g):
    if g == "receive":
        return 0
    elif g == "send":
        return 1
    else:
        return -1


def sinyalGuc(str):
    mesaj = ""
    sinyal = int(str)
    if sinyal > 0 and sinyal <= 50:
        mesaj = "Çok Zayıf Sinyal"
    elif sinyal > 50 and sinyal <= 100:
        mesaj = "Zayıf Sinyal"
    elif sinyal > 100 and sinyal <= 150:
        mesaj = "Orta Sinyal"
    elif sinyal > 150 and sinyal <= 200:
        mesaj = "Güclü Sinyal"
    elif sinyal > 200 and sinyal <= 255:
        mesaj = "Çok Güçlü Sinyal"
    return mesaj


def cihaz(chz):
    mesaj = ""
    c = int(chz)
    if c == 1:
        mesaj = "Televizyon"
    elif c == 2:
        mesaj = "Camaşır Makinesi"
    elif c == 3:
        mesaj = "Buzdolabı"
    elif c == 4:
        mesaj = "Fırın"
    return mesaj


# cihaz(6)

def cihazDurum(chzDrm):
    mesaj = ""
    cd = int(chzDrm)
    if cd == 0:
        mesaj = "Off"
    elif cd == 1:
        mesaj = "On"
    return mesaj


# cihazDurum(0)

def cevap(cvp):
    mesaj = ""
    cv = int(cvp)
    if cv == 0:
        mesaj = "Cevap İstenmiyor"
    elif cv == 1:
        mesaj = "Cevap İsteniyor"
    return mesaj


# ----------------------------------------------

giris = "send-250-1-1-1\nreceive-170-3-0\n"

# ----------------------------------------------

kodTipleri = ["receive", "send"]

komutlar = giris.rsplit("\n")
print("Giris : \n" + giris)
print("\n")
cikti = ""

for komut in komutlar:
    if (komut == ""):
        continue
    komutCikti = ""
    komutParcalari = komut.rsplit("-")
    kTip = kodTipi(komutParcalari[0])
    if (kTip < 0):
        komutCikti = "Error : Gecersiz Kod Tipi (" + komut + ")\n"
        cikti += komutCikti + "------" + "\n"
        continue
    komutCikti += "Kod Tipi : " + kodTipleri[kTip] + "\n"

    if (not ((kTip == 0 and len(komutParcalari) - 1 == 3) or (kTip == 1 and len(komutParcalari) - 1 == 4))):
        komutCikti = "Error : Gecersiz parametre sayisi (" + komut + ")\n"
        cikti += komutCikti + "------" + "\n"
        continue
    sinyalGucu = sinyalGuc(komutParcalari[1])
    if (sinyalGucu == ""):
        komutCikti = "Error : Birinci bolum hatali (" + komut + ")\n"
        cikti += komutCikti + "------" + "\n"
        continue
    komutCikti += "Sinyal Gucu : " + sinyalGucu + "\n"
    chz = cihaz(komutParcalari[2])
    if (chz == ""):
        komutCikti = "Error : Ikinci bolum hatali (" + komut + ")\n"
        cikti += komutCikti + "------" + "\n"
        continue
    komutCikti += "Cihaz : " + chz + "\n"
    cDurum = cihazDurum(komutParcalari[3])
    if (cDurum == ""):
        komutCikti = "Error : Ucuncu bolum hatali (" + komut + ")\n"
        cikti += komutCikti + "------" + "\n"
        continue
    komutCikti += "Durumu : " + cDurum + "\n"
    if (kTip == 1):
        cvp = cevap(komutParcalari[4])
        if (cvp == ""):
            komutCikti = "Error : Dorduncu bolum hatali (" + komut + ")\n"
            cikti += komutCikti + "------" + "\n"
            continue
        komutCikti += "Cevap : " + cvp + "\n"
    cikti += komutCikti + "------" + "\n"
print(cikti)