# BURS OTOMASYONU
ogrenci = dict()
id = 100
print("<-> BURS OTOMASYONUNA HOSGELDİNİZ! <->")


def ogrenci_bilgi():
    global ogrenci
    print(" -->Önceden burs almaya devam eden  ogrenci bilgilerini giriniz:")
    for i in range(2):
        bilgi = dict()
        ad_soyad = input("{}.ogrenci ad-soyad giriniz:".format(i + 1))
        bilgi["AdSoyad"] = ad_soyad
        kaz_uni = input("{}.ogrenci kazandigi üniversite ve bolum giriniz".format(i + 1))
        bilgi["kaz_Uni"] = kaz_uni
        ogr_ort = float(input("ogrencinin donem sonu ortalamasi:"))
        bilgi["Ogr_ort"] = ogr_ort
        ogr_durum = int(input("{}.ogrenci kacinci sinif:".format(i + 1)))
        bilgi["Ogr_Durum"] = ogr_durum
        ogrenci[i + id] = bilgi
    print("\n")


def ogrenci_guncelle():
    print("---ogrenci bilgilerini listele---")
    for ogr_id in ogrenci.keys():
        print("{} ID li ogrencinin".format(ogr_id), end="->")
        for j in ogrenci[ogr_id].keys():
            print(" {} = {}".format(j, ogrenci[ogr_id][j]), end=" , ")
        print()
    print("\n")


def ogrenci_sil(k):
    global ogrenci
    syc = 0
    liste1 = []
    if k == 3:
        print("Seneye burs alamayan ogrencileri siler , son sinif ve ortalamasi dusuk olan ogrencileri.")
        for ogr_id in ogrenci.keys():
            if ogrenci[ogr_id]["Ogr_Durum"] < 4 and ogrenci[ogr_id]["Ogr_ort"] >= 2.5:
                ogrenci[ogr_id] = ogrenci[ogr_id]
            else:
                syc += 1
                liste1.append(ogr_id)
                ogrenci[ogr_id].clear()
        print(liste1)
        print("---ogrenci silindikten donraki durum---")
        for ogr_id in ogrenci.keys():
            print("{} ID li ogrencinin".format(ogr_id), end="->")
            for j in ogrenci[ogr_id].keys():
                print(" {} = {}".format(j, ogrenci[ogr_id][j]), end=" , ")
            print()
        print("\n")

    def ogrenci_ekle():
        nonlocal syc
        if syc > 0:
            for i in range(syc):
                for p in liste1:
                    bilgi = dict()
                    ad_soyad = input("{}.ogrenci ad-soyad giriniz:".format(p))
                    bilgi["AdSoyad"] = ad_soyad
                    kaz_uni = input("{}.ogrenci kazandigi üniversite ve bolum giriniz".format(p))
                    bilgi["kaz_Uni"] = kaz_uni
                    ogr_gel = int(input("{}.ogrenci ailesinin aylik geliri:".format(p)))
                    bilgi["Ogr_gel"] = ogr_gel
                    ogr_Kar = int(input("{}.ogrenci kardes sayisi".format(p)))
                    bilgi["Ogr_Kar"] = ogr_Kar
                    ogrenci[p] = bilgi
        else:
            for i in range(2):
                bilgi = dict()
                ad_soyad = input("{}.ogrenci ad-soyad giriniz:".format(i + 1))
                bilgi["AdSoyad"] = ad_soyad
                kaz_uni = input("{}.ogrenci kazandigi  bolum giriniz".format(i + 1))
                bilgi["kaz_Uni"] = kaz_uni
                ogr_gel = int(input("{}.ogrenci ailesinin aylik geliri:".format(i + 1)))
                bilgi["Ogr_gel"] = ogr_gel
                ogr_Kar = int(input("{}.ogrenci kardes sayisi".format(i + 1)))
                bilgi["Ogr_Kar"] = ogr_Kar
                ogrenci[i + 102] = bilgi
            print("---ogrenci eklendikten sonraki durum---")
            for ogr_id in ogrenci.keys():
                print("{} ID li ogrencinin".format(ogr_id), end="->")
                for j in ogrenci[ogr_id].keys():
                    print(" {} = {}".format(j, ogrenci[ogr_id][j]), end=" , ")
                print()
            print("\n")

    if k == 4:
        ogrenci_ekle()


def ogrenci_bul():
    global ogrenci
    ara_ogrId = int(input("Aranacak ogrenci ID giriniz:"))
    b = ogrenci.get(ara_ogrId, "boyle bir ogrenci bulunmamaktadir.")
    print(b)


def cikis():
    print("Programdan ciktiniz!")
    return 0;


def ana_menu():
    while True:
        a = int(input(
            "-ogrenci bilgi fonksiyonu icin 1\n-ogrenci guncelle fonksiyonu icin 2\n-ogrenci sil fonksiyonu icin 3\n-ogrenci ekle"
            "fonksiyonu icin 4\n-ogrenci bul fonksiyonu icin 5 \n-programdan cikis icin 6\nbasiniz:"))
        if a == 1:
            ogrenci_bilgi()
        elif a == 2:
            ogrenci_guncelle()
        elif a == 3:
            ogrenci_sil(a)
        elif a == 4:
            ogrenci_sil(a)
        elif a == 5:
            ogrenci_bul()
        else:
            cikis()
            break;


ana_menu()

# BURS OTOMASYONU
ogrenci = dict()
id = 100
print("<-> BURS OTOMASYONUNA HOSGELDİNİZ! <->")


def ogrenci_bilgi():
    global ogrenci
    print(" -->Önceden burs almaya devam eden  ogrenci bilgilerini giriniz:")
    for i in range(2):
        bilgi = dict()
        ad_soyad = input("{}.ogrenci ad-soyad giriniz:".format(i + 1))
        bilgi["AdSoyad"] = ad_soyad
        kaz_uni = input("{}.ogrenci kazandigi üniversite ve bolum giriniz".format(i + 1))
        bilgi["kaz_Uni"] = kaz_uni
        ogr_ort = float(input("ogrencinin donem sonu ortalamasi:"))
        bilgi["Ogr_ort"] = ogr_ort
        ogr_durum = int(input("{}.ogrenci kacinci sinif:".format(i + 1)))
        bilgi["Ogr_Durum"] = ogr_durum
        ogrenci[i + id] = bilgi
    print("\n")


def ogrenci_guncelle():
    print("---ogrenci bilgilerini listele---")
    for ogr_id in ogrenci.keys():
        print("{} ID li ogrencinin".format(ogr_id), end="->")
        for j in ogrenci[ogr_id].keys():
            print(" {} = {}".format(j, ogrenci[ogr_id][j]), end=" , ")
        print()
    print("\n")


def ogrenci_sil(k):
    global ogrenci
    syc = 0
    liste1 = []
    if k == 3:
        print("Seneye burs alamayan ogrencileri siler , son sinif ve ortalamasi dusuk olan ogrencileri.")
        for ogr_id in ogrenci.keys():
            if ogrenci[ogr_id]["Ogr_Durum"] < 4 and ogrenci[ogr_id]["Ogr_ort"] >= 2.5:
                ogrenci[ogr_id] = ogrenci[ogr_id]
            else:
                syc += 1
                liste1.append(ogr_id)
                ogrenci[ogr_id].clear()
        print(liste1)
        print("---ogrenci silindikten donraki durum---")
        for ogr_id in ogrenci.keys():
            print("{} ID li ogrencinin".format(ogr_id), end="->")
            for j in ogrenci[ogr_id].keys():
                print(" {} = {}".format(j, ogrenci[ogr_id][j]), end=" , ")
            print()
        print("\n")

    def ogrenci_ekle():
        nonlocal syc
        if syc > 0:
            for i in range(syc):
                for p in liste1:
                    bilgi = dict()
                    ad_soyad = input("{}.ogrenci ad-soyad giriniz:".format(p))
                    bilgi["AdSoyad"] = ad_soyad
                    kaz_uni = input("{}.ogrenci kazandigi üniversite ve bolum giriniz".format(p))
                    bilgi["kaz_Uni"] = kaz_uni
                    ogr_gel = int(input("{}.ogrenci ailesinin aylik geliri:".format(p)))
                    bilgi["Ogr_gel"] = ogr_gel
                    ogr_Kar = int(input("{}.ogrenci kardes sayisi".format(p)))
                    bilgi["Ogr_Kar"] = ogr_Kar
                    ogrenci[p] = bilgi
        else:
            for i in range(2):
                bilgi = dict()
                ad_soyad = input("{}.ogrenci ad-soyad giriniz:".format(i + 1))
                bilgi["AdSoyad"] = ad_soyad
                kaz_uni = input("{}.ogrenci kazandigi  bolum giriniz".format(i + 1))
                bilgi["kaz_Uni"] = kaz_uni
                ogr_gel = int(input("{}.ogrenci ailesinin aylik geliri:".format(i + 1)))
                bilgi["Ogr_gel"] = ogr_gel
                ogr_Kar = int(input("{}.ogrenci kardes sayisi".format(i + 1)))
                bilgi["Ogr_Kar"] = ogr_Kar
                ogrenci[i + 102] = bilgi
            print("---ogrenci eklendikten sonraki durum---")
            for ogr_id in ogrenci.keys():
                print("{} ID li ogrencinin".format(ogr_id), end="->")
                for j in ogrenci[ogr_id].keys():
                    print(" {} = {}".format(j, ogrenci[ogr_id][j]), end=" , ")
                print()
            print("\n")

    if k == 4:
        ogrenci_ekle()


def ogrenci_bul():
    global ogrenci
    ara_ogrId = int(input("Aranacak ogrenci ID giriniz:"))
    b = ogrenci.get(ara_ogrId, "boyle bir ogrenci bulunmamaktadir.")
    print(b)


def cikis():
    print("Programdan ciktiniz!")
    return 0;


def ana_menu():
    while True:
        a = int(input(
            "-ogrenci bilgi fonksiyonu icin 1\n-ogrenci guncelle fonksiyonu icin 2\n-ogrenci sil fonksiyonu icin 3\n-ogrenci ekle"
            "fonksiyonu icin 4\n-ogrenci bul fonksiyonu icin 5 \n-programdan cikis icin 6\nbasiniz:"))
        if a == 1:
            ogrenci_bilgi()
        elif a == 2:
            ogrenci_guncelle()
        elif a == 3:
            ogrenci_sil(a)
        elif a == 4:
            ogrenci_sil(a)
        elif a == 5:
            ogrenci_bul()
        else:
            cikis()
            break;


ana_menu()

