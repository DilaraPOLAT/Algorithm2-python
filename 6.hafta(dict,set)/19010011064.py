# DİLARA SEVİM POLAT 19010011064

print("<< DİLARA 'NIN BURS OTOMASYONUNA HOŞGELDİNİZ >>")
ogr_name=["Id","Ad","Soyad","Kaz_bolum","Kac_Yıllık","Kacinci_sinif","Kardes_sayisi","Aylık_gelir","An-Ba_ayrımıveyasağmı"]
ogrenci = None
ogrenci_list = None
ogr_id = []
silinen = []

def ogr_dosya(ogr_bilgi):
    global ogrenci
    global ogr_id

    for i in ogr_bilgi:
        ogr_values = i.split(" ")
#Her boşluk gördüğünde listeyi ayırır ve ogr_values 'e atar.
        ogr_bil = dict()
        for ind in range(1, len(ogr_values)):
#Bilgileri tutmak için sözlük oluşturulur.İd'lerini yani sözlük içindeki keys'leri başka bir yapıda daha tutar(int olarak)
# diğer işlemler için gerekeçek.
            ogr_bil[ogr_name[ind]] = ogr_values[ind]
            ogrenci[ogr_values[0]] = ogr_bil
        ogr_id.append(int(ogr_values[0]))

#Eğer if'i sağlıyorsa içeriye girer öğrenci adında bir sözlük açar.Dosyayı okuma modunda açar ve içindekileri
#bir listeye atar listeyi ogr_dosya'ya yollar.
if ogrenci == None:
    ogrenci = dict()
    with open("19010011064.txt", "r") as ogr:
        ogrenci_list = ogr.readlines()
        ogr_dosya(ogrenci_list)

def ogrenci_guncelle():
    global ogrenci
    global ogrenci_list
    global ogr_id

    print("< Burs alan ogrenci bilgileri >")
#Anahtar değerleri alınacak döngü ile ve her bir keysin içinde bulunan keys değerleride alınıp karşılarına bilgileri yazılacak.
#Sözlüğün içindeki bilgileri parçalayıp düzgün bir şekilde yazmayı sağlar.
    for i in ogrenci.keys():
        print("ogr_Id={}".format(i),end =" ")
        for j in ogrenci[i].keys():
            print(" {} = {}".format(j,ogrenci[i][j]),end=" ")

        print()


def ogrenci_sil():
    global ogrenci
    global ogr_id
    global ogrenci_list
    global silinen

    k = input("Silenecek ögrenci Id'sine giriniz:")
    p = 0
# p ile girilen id'de öğrenci olup olmadığını bulurum.Öğrenci bulunursa girilen id'deki ogrenci silinir.Ve w modunda açılan dosya
#ya yeni listedeki değerler yazılır.Ve bilgiler tekrar güncellenir.
    for i in ogrenci.keys():
        if k == i:
           print("{} Id'li ogrenci bursu iptal edildi.".format(i))
           p = 1
           silinen.append(int(i))
#Silinen öğrenciynin id'sini silinen listeye atıyorum.çünkü öğrenci eklerisem ilk önce silinen öğrencilerin id'lerinden başlamak için.
           b = ogr_id.index(int(k))
           ogrenci_list.pop(b)
           ogr_id.pop(b)
           with open("19010011064.txt", "w") as ogr:
               ogr.seek(0)
               ogr.writelines(ogrenci_list)
           ogrenci = dict()
           for i in ogrenci_list :
               ogr_values = i.split(" ")
               ogr_bil = dict()
               for ind in range(1, len(ogr_values)):
                   ogr_bil[ogr_name[ind]] = ogr_values[ind]
                   ogrenci[ogr_values[0]] = ogr_bil

    if p != 1:
      print("Üzgünüz :( Girdiğiniz Id'de ogrenci bulunmamaktadır.")


def ogrenci_ara():
    global ogrenci
    global ogr_id
    p = 0
    x = input("Bulunacak ogrenci Id'sine giriniz:")
    for i in ogrenci.keys():
#Girilen id ile öğrenci aranır var ise bilgileri ekrana verilir.yok ise de if 'in içindeki mesaj ekrana verilir.
# p = 0 ise girilen id 'de öğrenci bulunmuştur.Değilsede bulunmamıştır.
        if x ==i :
            p = 1
            print("ogr_İD={}".format(x), end=" ")
            for j in ogrenci[x].keys():
                print(" {} = {}".format(j, ogrenci[x][j]), end=" ")
    if p!= 1:
        print("Üzgünüm :( girdiğiniz Id'de oğrenci bulunmamaktadır.")


def ogrenci_ekle():
  global ogrenci
  global ogr_id
  global ogrenci_list
  global id
  global silinen

  def ogrenci_kabul(aile):
      nonlocal t
      nonlocal k
      global ogrenci
      global ogr_id
      global ogrenci_list
      global silinen
#Bu fonksiyon ile gerken kriterleri sağlıyorsa öğrencinin burs başvurusu kabul olur , sağlamıyor ise burs başvurusu kabul olmaz.
# t ile eklenen öğrencinin  bilgilerine ulaşırız t=ogrencikeys'dir

      aylık = int(ogrenci[t]["Aylık_gelir"])
      kardes = int(ogrenci[t]["Kardes_sayisi"])
      if ( aile == 'Y'):
#Burs başvurusu kabul olursa tekrardan dosayaya yazdırmaya gerek yok zaten eklerken gereken işlemler yapıldı.
          print("Burs basvurunuz kabul edilmistir.En yakın zamanda bursunuz yatmaya baslayacaktır :)")
          if k!=0:
# k ile silinen id 'de öğrenci var ise ve o öğrencinin id'si eklenen öğrenciye verilmiştir. Ve bursu kabul olur ise
#silinen 'deki alınan  id silinir.çünkü silinen öğrencinin id'sinde bir öğrenci eklenmiştir.
           silinen.pop(0)

      elif (aile == 'V'):
          toplam_aile = kardes + 2
          Topmaas = aylık // toplam_aile
          if (Topmaas <= 900):
              print("Burs basvurunuz kabul edilmistir.En yakın zamanda bursunuz yatmaya baslayacaktır :)")
              if k != 0:
                  silinen.pop(0)
          else:
#Eğer burs başvurusu kabul olmaz ise dosya içine eklenen bilgiler silinir ve tekrar okunur  bilgiler güncellenir.
              print("Üzgünüm,burs basvurunuz kabul edilmemistir :(")
              b = ogr_id.index(int(t))
              ogrenci_list.pop(b)
              ogr_id.pop(b)
              with open("19010011064.txt", "w") as ogr:
                  ogr.seek(0)
                  ogr.writelines(ogrenci_list)
                  ogrenci = dict()
                  ogr_id = []
                  for i in ogrenci_list:
                      ogr_values = i.split(" ")
                      ogr_bil = dict()
                      for ind in range(1, len(ogr_values)):
                          ogr_bil[ogr_name[ind]] = ogr_values[ind]
                          ogrenci[ogr_values[0]] = ogr_bil
                      ogr_id.append(int(ogr_values[0]))

      elif (aile == 'A') :
          toplam_aile = kardes + 2
          Topmaas = aylık//toplam_aile
          if (Topmaas<=750):
              print("Burs basvurunuz kabul edilmistir.En yakın zamanda bursunuz yatmaya baslayacaktır :)")
              if k != 0:
                  silinen.pop(0)
          else:
              print("Üzgünüm,burs basvurunuz kabul edilmemistir :(")
              b = ogr_id.index(int(t))
              ogrenci_list.pop(b)
              ogr_id.pop(b)
              with open("19010011064.txt", "w") as ogr:
                  ogr.seek(0)
                  ogr.writelines(ogrenci_list)
                  ogrenci = dict()
                  ogr_id = []
                  for i in ogrenci_list:
                      ogr_values = i.split(" ")
                      ogr_bil = dict()
                      for ind in range(1, len(ogr_values)):
                          ogr_bil[ogr_name[ind]] = ogr_values[ind]
                          ogrenci[ogr_values[0]] = ogr_bil
                      ogr_id.append(int(ogr_values[0]))

      else:
          toplam2_aile = kardes + 3
          Topmaas2 = aylık//toplam2_aile
          if (Topmaas2 <= 650):
              if k != 0:
                  silinen.pop(0)
              print("Burs basvurunuz kabul edilmistir.En yakın zamanda bursunuz yatmaya baslayacaktır :)")
          else:
              print("Üzgünüm,burs basvurunuz kabul edilmemistir :(")
              b = ogr_id.index(int(t))
#Buradaki b silinecek öğrencinin id'sini bulmak için yazılmıştır.
              ogrenci_list.pop(b)
              ogr_id.pop(b)
              with open("19010011064.txt", "w") as ogr:
                  ogr.seek(0)
                  ogr.writelines(ogrenci_list)
                  ogrenci = dict()
                  ogr_id = []
                  for i in ogrenci_list:
                      ogr_values = i.split(" ")
                      ogr_bil = dict()
                      for ind in range(1, len(ogr_values)):
                          ogr_bil[ogr_name[ind]] = ogr_values[ind]
                          ogrenci[ogr_values[0]] = ogr_bil
                      ogr_id.append(int(ogr_values[0]))
#Burs alan öğrencilerin id'leri ogr_id 'de tutulur. Eğer uzunluğu 10'a eşit ise öğrenci eklenmez.
  for i in range(len(ogr_id)):
      i+=1
  if i==10:
      print("Üzgünüz,burs başvuru sayısı dolmuştur :( ")
  else:
    print("< Burs başvuru formu >")
    k = len(silinen)
#silinen öğrencilerin id'sini bulmak için bakılır.Eğer k=0  ise son id'deki öğrencinin id'sine 1 ekleyerek devam eder .
#Değilsede silinen öğrencinin id'sini alır.silinen ilk elemanını alır.
    if k==0:
         t = str(ogr_id[-1] + 1)
    else:
        t = str(silinen[0])
#Öğrencinin bilgileri liste şeklinde  alınır id'si zaten program tarafından önceden belirlenir.
#t'yi str olarak alırız çünkü dosyaya yazdıracaz.
    with open("19010011064.txt", "a") as dosya:
        bilgi = []
        bilgi.append(t)
        bilgi.append(" ")
        bilgi.append(input("-> İsminizi giriniz:"))
        bilgi.append(" ")
        bilgi.append(input("-> Soyadınızı giriniz:"))
        bilgi.append(" ")
        bilgi.append(input("-> Kazandığınız bölüm:"))
        bilgi.append(" ")
        bilgi.append(input("-> Kac yıllık:"))
        bilgi.append(" ")
        bilgi.append(input("-> Kacıncı sınıf:"))
        bilgi.append(" ")
        bilgi.append(input("-> Kardessayınız:"))
        bilgi.append(" ")
        bilgi.append(input("-> Aylık geliriniz:"))
        bilgi.append(" ")
        bilgi.append(input("->Aile durumunuz.\n-Anne baba ayrı ise'A' ya basınız.\n-Herhangi biri  sağ  değilsede 'V' ye basınız."
                           "\n-Her ikisi sağ değilse 'Y' ye basınız'\n-Yukarıdaki her üç durumda yoksa herhangi bir tuşa basınız."))
# a modunda açılan dosyaya bilgiler eklenir.
        al = bilgi[16]
        bilgi.append("\n")
        dosya.writelines(bilgi)
        ogrenci = dict()
        ogr_id.append(int(bilgi[0]))
#Tekrardan dosyanın içindeki bilgiler okunur ve gerekli yerlere bilgiler güncellenir.
    with open("19010011064.txt", "r") as ogr:
        ogrenci_list = ogr.readlines()
        ogr_id = []
        for i in ogrenci_list:
            ogr_values = i.split(" ")
            ogr_bil = dict()
            for ind in range(1, len(ogr_values)):
                ogr_bil[ogr_name[ind]] = ogr_values[ind]
                ogrenci[ogr_values[0]] = ogr_bil
            ogr_id.append(int(ogr_values[0]))
#ogrenci kabul fonksiyonuna gidilir.al ile aile durumu ne olduğu alınır ve  kabul fonsiyonuna gönderilir.
    ogrenci_kabul(al)


def ogrenci_yıl():
    global ogrenci
    global ogrenci_list
    global ogr_id
    global silinen
    d=[]
#d ile kaç sene geçti ise öğrenci nin kaçıncı sınıfta ise eklenir örneğin 1. sınıfta olan öğrenci 2 yıl geçmişse 3.sınıfta olur.
    hesap=[]
#hesap ile öğrencinin şu anlık kaçıncı sınfta olduğunu bulur ve bölümü kaç yıllık ise onunla karşılaştırır.
    sene=int(input("- Kac yıl gecti :"))
    for i in ogrenci.keys():
        kac_sınıf = int(ogrenci[i]["Kacinci_sinif"])
        hesap .append(kac_sınıf + sene)
        d.append(kac_sınıf + sene)
    o = 0
#Buradaki o ise d nin indeksini gezmeyi sağlar.
    with open("19010011064.txt", "w") as ogr:
      for a in ogrenci_list:
            ogr_values = a.split(" ")
            x = []
            t = 0
#Burada ogrenci_list yeni bir listeye eklenir ve bosluk karakteri olanları ayırır ve burda t eşit ise 8 demek
#öğrencinin son bilgisi alınır ve ardına boşluk bırakmaması için yapılır .
            for j in ogr_values:
                if t == 8:
                    x.append(j)
                else:
                    x.append(j)
                    x.append(" ")
                t += 1
#Burada x[10] demek kacıncı sınıf bilgisinin değiştirir.10 kaçıncı sınıf bilgisinin indeksidir.
            x[10] = str(d[o])
            o += 1
            with open("19010011064.txt", "a") as ogr:
                  ogr.writelines(x)
#Kaç yıl geçmişse bunun bilgisini alır listeye ekler ve bilgileri dosaya da ekler.Ve dosya okunur.
 # ve bilgiler tekrardan gerekli olan yerlere günecellenir.
    ogrenci = dict()
    with open("19010011064.txt", "r") as ogr:
        ogrenci_list = ogr.readlines()
        ogr_dosya(ogrenci_list)
        e =0
#Buradaki e  hesap listesini gezmek için kullanılır.
        for i in ogrenci.keys():
            kac_yıl = int(ogrenci[i]["Kac_Yıllık"])
#Oğrenci mezun olmuşşsa listeden siler ve dosya ya tekrardan yazılır.
            if hesap[e] > kac_yıl:
                print("{} Id'li ogrencinin burs alma zamanı doldu.Bursu iptal edildi.".format(i))
                silinen.append(int(i))
                b = ogr_id.index(int(i))
                ogrenci_list.pop(b)
                ogr_id.pop(b)
                with open("19010011064.txt", "w") as ogr:
                    ogr.seek(0)
                    ogr.writelines(ogrenci_list)
                    ogrenci = dict()
                    for i in ogrenci_list:
                        ogr_values = i.split(" ")
                        ogr_bil = dict()

                        for ind in range(1, len(ogr_values)):
                            ogr_bil[ogr_name[ind]] = ogr_values[ind]
                            ogrenci[ogr_values[0]] = ogr_bil
            e += 1


def ogrenci_istatislik():
    print("< Burs alan ogrenci istatislikleri >")
    a = 0
#a ile en yuksek kişi başına düşen aylık geliri bulmamızı sağlar.
    b = 100000
#b ile en düşük kişi başına düşen aylık geliri bulmamızı sağlar.
    t = 0
    c = 0
#Kaç tane öğrencinin kişi başına düşen aylık gelir  ve en az ve en fazla  onu bulmayı sağlar.
    for i in ogrenci.keys():
        Aylık = int(ogrenci[i]["Aylık_gelir"])
        kardes = int(ogrenci[i]["Kardes_sayisi"])
        Aile = ogrenci[i]["An-Ba_ayrımıveyasağmı"]
        if Aile == "A\n":
          Top_Aile = kardes + 2

        elif Aile == "V\n":
          Top_Aile = kardes + 2

        elif Aile == "Y\n":
          Top_Aile = kardes + 1

        else:
          Top_Aile = kardes + 3

        x = Aylık //Top_Aile
        print("{} Id'li öğrencinin ailesinin toplam aylık geliri = {}.\tKişi başına düşen aylık gelir = {}".format(i,Aylık,x))
        if x > a:
                a = x
        if x < b:
                b = x
    print()
#yukarıdaki for döngüsü ile kişi başına düşen aylık geliri ve en az en fazla kişi başına düşen aylık geliri  hesaplanıyor
#Aşağıdaki for ile kaç kişinin en az en fazla olduğunu hesaplanıyor.
    for i in ogrenci.keys():
        Aylık = int(ogrenci[i]["Aylık_gelir"])
        kardes = int(ogrenci[i]["Kardes_sayisi"])
        Aile = ogrenci[i]["An-Ba_ayrımıveyasağmı"]
        if Aile == "A\n":
            Top_Aile = kardes + 2

        elif Aile == "V\n":
            Top_Aile = kardes + 2

        elif Aile == "Y\n":
            Top_Aile = kardes + 1

        else:
            Top_Aile = kardes + 3

        x = Aylık // Top_Aile
        k = i
        if x == a:
          print("-> Kişi başına düşen aylık geliri en fazla olan öğrenci id'si = {}".format(k))
          t+=1
        if x == b:
          print("-> Kişi başına düşen aylık geliri en az olan öğrenci id'si = {}".format(k))
          c+=1
    print("- kişi başına düşen aylık geliri en fazla {} öğrencinin .\t"
          " kişi başına düşen aylık gelir en az {} öğrencinin.".format(t,c))


def cikis():
    print("< Programdan çıktınız...>")
    return 0


def ana_menu():
  while True:
     print()
     print("  <<  BURS OTOMASYON  MENÜSÜ  >>")
     a=int(input("- Ogrenci güncelle fonksiyonu icin '1'\n- Ogrenci sil fonksiyonu icin '2'\n- Ogrenci ara fonksiyonu icin '3'\n- Ogrenci ekle"
                "fonksiyonu icin '4'\n- Ogrenci yıl fonksiyonu icin '5'\n- Ogrenci istatislik icin '6' \n- Programdan cikis icin '7'\nbasiniz:"))
     if a==1:
         ogrenci_guncelle()
     elif a==2:
         ogrenci_sil()
     elif a==3:
         ogrenci_ara()
     elif a==4:
         ogrenci_ekle()
     elif a==5:
         ogrenci_yıl()
     elif a==6:
         ogrenci_istatislik()
     elif a==7:
         cikis()
         break;


ana_menu()