# AMİRAL BATTİ OYUNU
# DİLARA SEVİM POLAT  19010011064

import random
while True:
# En basta bir while dongusu kurdum cunku tekrar tekrar oyun baslamasi icin.
    print("\n<--- AMİRAL BATTİ OYUNUNA HOSGELDİNİZ --->\n")
    print("DİKKAT!\nDikey ='D',Yatay ='Y' ile gosterilir.\nACİK MODA = Gemilerin gorunumu '-' ile gosterilir.Gemilerin olmadigi bolgeler '?' ile gosterilir."
          "\nKAPALİ MODA = Atis basariliysa '+' basarizizsa '*' ile gosterilir.")
    alan = []
    alan1 = []
# İki tane oyun alaninin list aldim cunku biri acik modu gosterirken digeri kapali modu gosterecek.
    gsat = []
    gsut = []
    gkon = []
# Satir sutun ve konum bilgileri icin her gemi icin ayri olmasi icin liste alindi.
    harfler = 'DY'
# Harfler random ile dikey veya yataylik durumunu belirleyecek.
    b = 0
    y=1
    k = []
    l = []
    tsat=[]
    tsut=[]
    sayac1=0
    sayac2=0
    sayac3=0
    sayac4=0
# b her bir atis isabetli ise birer birer artacak  tum gemilerin bolumlerini vurdugunda kullanici oyunu kazandigini bilecek.
# y ile while kontrol edecez.
# k ve l listeleri kullanicini girecegi satir ve sutun sayilarini tutuyor liste seklinde olmasinin nedeni bir listeyle karsilastirdigim icin hata
#vermesini engellemek.
# tsat tsut ise girilen satir ve sutunun kordinatlari esit ise yani gemilerin ust uste gelmesini engelemek ıcın tanimlandi.
# Sayaclar ise her bir geminin tum parcalarini vurulduysa tebrikler gemi batirildi dondurmesini saglayacak.
    ad = input("-oyuncu adiniz:_")
    while True:
# burda ki while oyun alaninin boyuttunu en az 10 *10 birimlik olmasini sagliyor.
      boyut=int(input("->Oyun alanini boyutu kac birim kare olsun :"))
      if(boyut>=10):
         puan = (boyut*boyut) // 3
         print("->Puaniniz toplam hakinizdan her bir atisinizi   cikarilarak hesaplanacaktir\n!!! NOT:toplam atiş hakki <{}> dir.".format(puan))
         break;
      else:
        print("-Oyun alaninin boyutu en az 10*10 birim karelik olmali!\n->Lutfen tekrar deneyiniz. ")
#Burda ki for ile alan ve alan 1 listesi ? isareti ile dolduruluyor.
    for i in range(boyut):
        alan.append(["?"] * boyut)
        alan1.append(["?"] * boyut)
#Burdaki while ise ayni kordinatlara sahip olan yani ust uste gemiler olmamasini sagliyor
# ve icerdeki diger while ise randomla alinan satir sutun sayisi ornegin 4 brimlik gemi ise ve satir 11 ise dikey yone giderse
#alanin disina cikar ondan bu gibi sorunlar icin yapildi.
    while True:
      y=1
      for i in range(0, 4):
         gsat.append(random.randint(0, boyut-1))
         gsut.append(random.randint(0, boyut-1))
         gkon.append(random.choice(harfler))
         while True:

             if (boyut-3 <= gsat[i] <= boyut-1 and gkon[i] == "D"):
                gsat[i] = random.randint(0, boyut-1)
                gsut[i] = random.randint(0, boyut-1)
                gkon[i] = random.choice(harfler)

             elif (boyut-3 <= gsut[i] <= boyut-1 and gkon[i] == "Y"):
                gsat[i] = random.randint(0, boyut-1)
                gsut[i] = random.randint(0, boyut-1)
                gkon[i] = random.choice(harfler)
             else:
                break;
#burda random ile alinan satir sutunlari baska satir sutun listesine eslesiyor.burda farkli bir liste tutmamin nedeni:
#gsat gsut 2 birimlik geminin sadece baslangic konumunu alir tsat tsut ile 2 birimlik geminin tum parcalari alinir.
         for j in range(4):
             if (gkon[i] == "D"):
                 if (i == 0 and j == 0):
                    tsat.append(gsat[i])
                    tsut.append(gsut[i])
                 elif (i == 1 and 1 >= j >= 0):
                    tsat.append(gsat[i] + j)
                    tsut.append(gsut[i])
                 elif (i == 2 and 2 >= j >= 0):
                    tsat.append(gsat[i] + j)
                    tsut.append(gsut[i])
                 elif (i == 3 and 3 >= j >= 0):
                    tsat.append(gsat[i] + j)
                    tsut.append(gsut[i])
             elif (gkon[i] == "Y"):
                 if (i == 0 and j == 0):
                    tsat.append(gsat[i])
                    tsut.append(gsut[i] + j)
                 elif (i == 1 and 1 >= j >= 0):
                    tsat.append(gsat[i])
                    tsut.append(gsut[i] + j)
                 elif (i == 2 and 2 >= j >= 0):
                    tsat.append(gsat[i])
                    tsut.append(gsut[i] + j)
                 elif (i == 3 and 3 >= j >= 0):
                    tsat.append(gsat[i])
                    tsut.append(gsut[i] + j)
#burda ise y=1 ise ikinci fora girer. burda butun gemilerin birden baslayip tum paraclari da dahil sirasiyla satir ve sutun sayisi
#bir sonraki indexsteki sayiyla esit ise bu gemiler ust uste konumlu if'e girer ve daha onceki aldigimiz bilgileri temizler ve tekrar basa doner
#esit degilsede y=1 dır hala ondan dolayi whiledan cikar ve bir sonraki isleme gecer.
# burda basta if esitse 0 a fordan cik dememin sebebi y=0 oldugunda for devam eder dongusu ve buda index hatasi olur bunu engellemek icin yazdim.
      for p in range(0,9):
         if (y == 0):
              break;
         for c in range(p + 1, 9):
             if (tsat[p] == tsat[c + 1] and tsut[p] == tsut[c + 1]):
                 y=0
#burda onceki listeleri icini temizlerim yoksa sonsuz donguye girer bunu engellemek icin ve  yeni degerler almak icin.
                 gsat.clear()
                 gsut.clear()
                 gkon.clear()
                 tsat.clear()
                 tsut.clear()
#print icindekini yazmamin nedeni ust uste konumlu geminin oldugu ve tekrar random sayilar atildigini gormenizi saglamak.
                 print("-->ust uste konumlu gemi oldugundan tekrar basa donuldu.Random sayilar atandi.")
                 break;
      if (y!=0):
#programin dogru calisip calismadigini gormeniz icin yazdim print icindekini.
         print("-->ust uste konumlu gemi bulunmamaktadir.")
         break;
#burada alan' a gemilerin tum parcalarinin konumlarindaki bolgeyi - doldurmasini saglar.
    for i in range(4):
      print("- {} Birimik geminin baslangic kordinatlari: ({},{}) ve konumu:{}".format(i + 1, gsat[i], gsut[i], gkon[i]))
    for i in range(4):
        if (i == 0):
            alan[gsat[i]][gsut[i]] = "-"
        elif (i == 1):
            if (gkon[i] == "Y"):
                alan[gsat[i]][gsut[i]] = "-"
                alan[gsat[i]][gsut[i] + 1] = "-"

            elif (gkon[i] == "D"):
                alan[gsat[i]][gsut[i]] = "-"
                alan[gsat[i] + 1][gsut[i]] = "-"

        elif (i == 2):
            if (gkon[i] == "Y"):
                alan[gsat[i]][gsut[i]] = "-"
                alan[gsat[i]][gsut[i] + 1] = "-"
                alan[gsat[i]][gsut[i] + 2] = "-"

            elif (gkon[i] == "D"):
                alan[gsat[i]][gsut[i]] = "-"
                alan[gsat[i] + 1][gsut[i]] = "-"
                alan[gsat[i] + 2][gsut[i]] = "-"


        elif (i == 3):
            if (gkon[i] == "Y"):
                alan[gsat[i]][gsut[i]] = "-"
                alan[gsat[i]][gsut[i] + 1] = "-"
                alan[gsat[i]][gsut[i] + 2] = "-"
                alan[gsat[i]][gsut[i] + 3] = "-"
            elif (gkon[i] == "D"):
                alan[gsat[i]][gsut[i]] = "-"
                alan[gsat[i] + 1][gsut[i]] = "-"
                alan[gsat[i] + 2][gsut[i]] = "-"
                alan[gsat[i] + 3][gsut[i]] = "-"


#burada acik modu alan ile yazip randomla aldigimiz gemilerin yerlerini yazdiririz.
    print("\n<- ACİK MOD ->")
    print(end="\t")
    for i in range(boyut):
        print(i, end="\t")
    print("\n")
    for i in range(boyut):
        print(i, end="\t")
        for j in range(boyut):
            print(alan[i][j], end="\t")
        print("")
    print("\n")
#alan1 ile kapali modu yazdiririz.fazladan birkac islem var onlarin nedeni satir ve sutun indekslerini terminalde gostermek.
    print("<- KAPALİ MOD ->")
    print(end="\t")
    for i in range(boyut):
        print(i, end="\t")
    print("\n")
    for i in range(boyut):
        print(i, end="\t")
        for j in range(boyut):
            print(alan1[i][j], end="\t")
        print("")
#burda ise for la kullanicini yaptigi atislari ile ilgili islemler.
    for t in range(puan+1):
        k = int(input("->Satir sayisinin kordinatlarini giriniz:"))
        l = int(input("->Sutun sayisinin kordinatlarina giriniz:"))
#burdak while kullanici boyuttun indeksi disin da bir kordinat girmisse tekrar kullanicidan kordinat alasini saglar.
#ornegin 10*10 boyut 10 girmise veya 10 dan buyuk sayi girmisse  tekrar kullanicidan sayi ister
        while True:
            if (k >= boyut or l >= boyut):
                print("-Girdiginiz kordinatlar oyun alaninda bulunamadi :(\n-Lutfen tekrar deneyiniz:")
                k = int(input("->Satir sayisinin kordinatlarini giriniz:"))
                l = int(input("->Sutun sayisinin kordinatlarina giriniz:"))

            else:
                break;
#burdaki ifle eger girdigim kordinatlarda gemi daha once vurulduysa tekrar kullanicidan sayi almasini saglar tabiki atis yaptigi icin puanida eksilir.
        if (alan[k][l] == "+"):
            puan = puan - 1
            print("->Malesef daha once bu kordinatlara girmistiniz. tekrar deneyiniz.")
            print("---> KALAN HAKKİNİZ:{}".format(puan))
#buradaki iki for ise girilen kordinatlar varsa if bloguna girer ve icerdeki islemleri gerceklestirir  + isareti alir.if bloguna girmesede
#asagidaki else bloguna girer isabetsiz atis tekrar giriniz ve girilen kordinat bolgesine * isareti alir
        for i in range(0, 4):
            for j in range(0, 4):
                if (alan[k][l] == "-"):
                    if (k == gsat[i] + j and l == gsut[i] and gkon[i] == "D"):
                        puan = puan - 1
                        print("->Tebrikler isabetli atis :)")
                        print("---> KALAN HAKKİNİZ:{}".format(puan))
                        b = b + 1
                        if (i == 0):
                            alan1[gsat[i] + j][gsut[i]] = "+"
                            alan[k][l]=alan1[gsat[i] + j][gsut[i]]
                            sayac1=sayac1+1
                        elif (i == 1):
                            alan1[gsat[i]+j][gsut[i]] ="+"
                            alan[k][l] = alan1[gsat[i] + j][gsut[i]]
                            sayac2 = sayac2 + 1
                        elif (i == 2):
                            alan1[gsat[i]+j][gsut[i]] = "+"
                            alan[k][l] = alan1[gsat[i] + j][gsut[i]]
                            sayac3 = sayac3 + 1
                        elif (i == 3):
                            alan1[gsat[i]+j][gsut[i]] = "+"
                            alan[k][l] = alan1[gsat[i] + j][gsut[i]]
                            sayac4 = sayac4 + 1

                    if (k == gsat[i] and l == gsut[i] + j and gkon[i] == "Y"):
                        puan = puan - 1
                        print("->Tebrikler isabetli atis :)")
                        print("---> KALAN HAKKİNİZ:{}".format(puan))
                        b = b + 1
                        if (i == 0):
                            alan1[k][l] = "+"
                            alan[k][l] = alan1[gsat[i]][gsut[i]+j]
                            sayac1 = sayac1 + 1
                        elif (i == 1):
                            alan1[gsat[i]][gsut[i] + j] = "+"
                            alan[k][l] = alan1[gsat[i]][gsut[i]+j]
                            sayac2 = sayac2 + 1

                        elif (i == 2):
                            alan1[gsat[i]][gsut[i] + j] = "+"
                            alan[k][l] = alan1[gsat[i]][gsut[i]+j]
                            sayac3 = sayac3 + 1

                        elif (i == 3):
                            alan1[gsat[i]][gsut[i]+j] = "+"
                            alan[k][l] = alan1[gsat[i]][gsut[i]+j]
                            sayac4 = sayac4 + 1

        else:
            if (alan[k][l] != "-" and alan[k][l] != "+" ):
                alan1[k][l] = "*"
                puan = puan - 1
                print("->Malesef isabetsiz atis  tekrar deneyiniz :(")
                print("---> KALAN HAKKİNİZ:{}".format(puan))
#buradaki if ler ise sayac1 =1 ise demeki 1 birimlik geminin tamami vurulmus ve tekrar sayac 0 lanir.sayaclari 0 yapmamin nedeni:
#ornegin 1 birimlik gemiyi batirmissa sayac hep 1 olarak kalir her islemde surekli gemi batirildi diye yazi gelir bunu engellemek icin yaptim.
        if (sayac1 == 1):
            print("-->TEBRİKLER BİR GEMİ BATİRDİNİZ :)")
            sayac1=0

        if (sayac2 == 2):
            print("-->TEBRİKLER BİR GEMİ BATİRDİNİZ :)")
            sayac2 = 0

        if (sayac3 == 3):
            print("-->TEBRİKLER BİR GEMİ BATİRDİNİZ :)")
            sayac3 = 0

        if (sayac4 == 4):
            print("-->TEBRİKLER BİR GEMİ BATİRDİNİZ :)")
            sayac4 = 0

#burada ise kullanici girdigi her bir kordinattan sonra oyun alaninin gorunumunu gorecektir
        print("\n<- ATİS YAPİLDİKTAN SONRAKİ KAPALİ MODUN  HALİ ->")
        print(end="\t")
        for i in range(boyut):
            print(i, end="\t")
        print("\n")
        for i in range(boyut):
            print(i, end="\t")
            for j in range(boyut):
                print(alan1[i][j], end="\t")
            print("")
#b=10 ise demekki tum gemiler batirilmis break ile baslangictaki fordan cikar.
        if (b == 10):
            print("-->TEBRİLER {}! OYUNU KAZANDİNİZ :)\nPUANİNİZ : {}".format(ad, puan))
            m = int(input("-Tekrar oynamak icin herhangi bir sayi tusuna  basiniz , oyunu oynamak istemiyorsaniz '2' ye  basiniz:"))
#print icinedini yazmamin nedeni goruntu guzeligi.
            print('\n' * 30)
            break;
#burda ise  yapilan atislar hak sayisini gecmişse ve tum gemiler batmamissa if bloguna girer.burada b<10 yapma sebebim oyunu oynayan kisi son 1
#hakkinda isabetli atis yapip tum gemiler batmissa bu if bloguna girmez.
        if (puan==0 and b<10):
            print("-->MALESEF {}! OYUNU KAYBETİNİZ :(\n-SİZE VERİLEN HAKLAR BİTTİ.\nPUANİNİZ :{}".format(ad,puan))
            m=int(input("-Tekrar oynamak icin herhangi bir sayi tusuna  basiniz , oyunu oynamak istemiyorsaniz '2' ye  basiniz:"))
            print('\n'*30)
            break;
#fordan cikmadan once sordugu soru m= 2 olmyan herhangi bir sayi ise oyun tekrar basliyor, m=2 ise oyundan cikilyor.
    if(m == 2):
        print("->OYUNDAN CİKTİNİZ :(")
        break;

