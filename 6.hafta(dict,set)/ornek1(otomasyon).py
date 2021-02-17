# #maas zami hesaplama ornegi
# personel =dict()
# per_say=int(input("Kac adet personel girilecek:"))
# id=100
# #bilgi=dict()
# for i in range(1,per_say+1):
#     bilgi=dict() #hatirlat
#     adsoyad=input("{}.personel ad-soyad:".format(i))
#     bilgi["AdSoyad"]=adsoyad
#     maas=int(input("{}.personal maas:".format(i)))
#     bilgi["Maas"]=maas
#     cs = int(input("{}.personal cocuk sayisi:".format(i)))
#     bilgi["CS"] = cs
#     ezam=int(input("{}.personel eski zam:".format(i)))
#     bilgi["EZam"]=ezam
#     personel[id+i]=bilgi #bilgi.copy()
# print(personel)
#
#
# #personel listele
# for per_id in personel.keys():
#     print("per ID ={}".format(per_id),end=" ")
#     #tek tek yazma peersonel[per_id]["xxx]
#     for per_bilgi in personel[per_id].keys():
#         print("{}={}".format(per_bilgi,personel[per_id][per_bilgi]),end=" ")
#     print()
# #Eski zam oranlari bul
# for per_id in personel.keys():
#     ezam_oran=personel[per_id]["EZam"]/personel[per_id]["Maas"]
#     print("per_ID={} , per_EZamoran:{:.2f}".format(per_id,ezam_oran))
# #Ara
# ara_perId=int(input("Aranacak personel ID giriniz:"))
# bilgi=personel.get(ara_perId,"boyle bir personel bulunmamaktadir.")
# print(bilgi)
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
#Her boşluk gördüğünde listeyi ayırır ve ogr_values 'a atar.
        ogr_bil = dict()
        for ind in range(1, len(ogr_values)):
#Bilgileri tutmak için sözlük oluşturulur.İd'lerini yani sözlük içindeki keys'leri başka bir yapıda daha tutar diğer işlemler için gerekeçek.
            ogr_bil[ogr_name[ind]] = ogr_values[ind]
            ogrenci[ogr_values[0]] = ogr_bil
        ogr_id.append(int(ogr_values[0]))

#Eğer if'i sağlıyorsa içeriye girer öğrenci adında bir sözlük açar.Dosyayı okuma modunda açar ve içindekileri
#bir listeye atar listeyi ogr_dosya'ya yollar.
if ogrenci == None:
    ogrenci = dict()
    with open("ogrenci.txt", "r") as ogr:
        ogrenci_list = ogr.readlines()
        ogr_dosya(ogrenci_list)

def ogrenci_guncelle():
    global ogrenci
    global ogrenci_list
    global ogr_id
    print("< Burs alan ogrenci bilgileri >")
#Anahtar değerleri alınacak döngü ile her bir keysin içinde bulunan keys değerleride alınıp karşılarına bilgileri yazılacak.
#Sözlüğün içindeki bilgileri parçalayıp düzgün bir şekilde yazmayı sağlar.
    for i in ogrenci.keys():
        print("ogr_Id={}".format(i),end =" ")
        for j in ogrenci[i].keys():
            print(" {} = {}".format(j,ogrenci[i][j]),end=" ")

        print()


def ogrenci_sil():
    global ogrenci
    global ogr_id
    global silinen

    k = input("Silenecek ögrenci Id'sine giriniz:")
    p = 0
# p ile girilen id'de öğrenci olup olmadığını bulurum.
    for i in ogrenci.keys():
        if k == i:
           print("{} Id'li ogrenci bursu iptal edildi.".format(i))
           p = 1
           silinen.append(int(i))
           b = ogr_id.index(int(k))
           ogrenci_list.pop(b)
           ogr_id.pop(b)
           with open("ogrenci.txt", "w") as ogr:
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
      print("Üzgünüz:( Girdiğiniz Id'de ogrenci bulunmamaktadır.")


def ogrenci_ara():
    global ogrenci
    global ogr_id
    p = 0
    x = input("Bulunacak ogrenci Id'sine giriniz:")
    for i in ogrenci.keys():
        if x ==i :
            p = i
            print("ogr_İD={}".format(x), end=" ")
            for j in ogrenci[x].keys():
                print(" {} = {}".format(j, ogrenci[x][j]), end=" ")
    if p!= x:
        print("Üzgünüm :(girdiğiniz Id'de oğrenci bulunmamaktadır.")


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

      aylık = int(ogrenci[t]["Aylık_gelir"])
      kardes = int(ogrenci[t]["Kardes_sayisi"])

      if ( aile == 'Y'):
          print("Burs basvurunuz kabul edilmistir.En yakın zamanda bursunuz yatmaya baslayacaktır:)")
          if k!=0:
           silinen.pop(0)
      elif (aile == 'V'):
          toplam_aile = kardes + 2
          Topmaas = aylık // toplam_aile
          if (Topmaas <= 900):
              print("Burs basvurunuz kabul edilmistir.En yakın zamanda bursunuz yatmaya baslayacaktır:)")
              if k != 0:
                  silinen.pop(0)
          else:
              print("Üzgünüm,burs basvurunuz kabul edilmemistir:(")
              b = ogr_id.index(int(t))
              ogrenci_list.pop(b)
              ogr_id.pop(b)
              with open("ogrenci.txt", "w") as ogr:
                  ogr.seek(0)
                  ogr.writelines(ogrenci_list)
                  ogrenci = dict()
                  for i in ogrenci_list:
                      ogr_values = i.split(" ")
                      ogr_bil = dict()
                      for ind in range(1, len(ogr_values)):
                          ogr_bil[ogr_name[ind]] = ogr_values[ind]
                          ogrenci[ogr_values[0]] = ogr_bil
      elif (aile == 'A') :
          toplam_aile = kardes + 2
          Topmaas = aylık//toplam_aile
          if (Topmaas<=750):
              print("Burs basvurunuz kabul edilmistir.En yakın zamanda bursunuz yatmaya baslayacaktır:)")
              if k != 0:
                  silinen.pop(0)
          else:
              print("Üzgünüm,burs basvurunuz kabul edilmemistir:(")
              b = ogr_id.index(int(t))
              ogrenci_list.pop(b)
              ogr_id.pop(b)
              with open("ogrenci.txt", "w") as ogr:
                  ogr.seek(0)
                  ogr.writelines(ogrenci_list)
                  ogrenci = dict()
                  for i in ogrenci_list:
                      ogr_values = i.split(" ")
                      ogr_bil = dict()
                      for ind in range(1, len(ogr_values)):
                          ogr_bil[ogr_name[ind]] = ogr_values[ind]
                          ogrenci[ogr_values[0]] = ogr_bil

      else:
          toplam2_aile = kardes + 3
          Topmaas2 = aylık//toplam2_aile
          if (Topmaas2 <= 650):
              if k != 0:
                  silinen.pop(0)
              print("Burs basvurunuz kabul edilmistir.En yakın zamanda bursunuz yatmaya baslayacaktır:)")
          else:
              print("Üzgünüm,burs basvurunuz kabul edilmemistir:(")
              b = ogr_id.index(int(t))
              ogrenci_list.pop(b)
              ogr_id.pop(b)
              with open("ogrenci.txt", "w") as ogr:
                  ogr.seek(0)
                  ogr.writelines(ogrenci_list)
                  ogrenci = dict()
                  for i in ogrenci_list:
                      ogr_values = i.split(" ")
                      ogr_bil = dict()
                      for ind in range(1, len(ogr_values)):
                          ogr_bil[ogr_name[ind]] = ogr_values[ind]
                          ogrenci[ogr_values[0]] = ogr_bil

  for i in range(len(ogr_id)):
      i+=1
  if i>=10:
      print("Üzgünüz,burs başvuru sayısı dolmuştur :( ")
  else:
    print("< Burs başvuru formu >")
    k = len(silinen)
    if k==0:
         t = str(ogr_id[-1] + 1)
    else:
        t = str(silinen[0])

    with open("ogrenci.txt", "a") as dosya:
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

        al = bilgi[16]
        bilgi.append("\n")
        dosya.writelines(bilgi)
        ogrenci = dict()
        ogr_id.append(int(bilgi[0]))
    with open("ogrenci.txt", "r") as ogr:
        ogrenci_list = ogr.readlines()
        for i in ogrenci_list:
            ogr_values = i.split(" ")
            ogr_bil = dict()
            for ind in range(1, len(ogr_values)):
                ogr_bil[ogr_name[ind]] = ogr_values[ind]
                ogrenci[ogr_values[0]] = ogr_bil
    ogrenci_kabul(al)


def ogrenci_yıl():
    global ogrenci
    global ogrenci_list
    global ogr_id
    global silinen
    d=[]
    hesap=[]

    sene=int(input("Kac yıl gecti :"))
    for i in ogrenci.keys():
        kac_sınıf = int(ogrenci[i]["Kacinci_sinif"])
        hesap .append(kac_sınıf + sene)
        d.append(kac_sınıf + sene)
    o = 0
    with open("ogrenci.txt", "w") as ogr:
      for a in ogrenci_list:
            ogr_values = a.split(" ")
            x = []
            t = 0

            for j in ogr_values:
                if t == 8:

                    x.append(j)
                else:
                    x.append(j)
                    x.append(" ")
                t += 1
            x[10] = str(d[o])
            o += 1
            with open("ogrenci.txt", "a") as ogr:
                  ogr.writelines(x)

    ogrenci = dict()
    with open("ogrenci.txt", "r") as ogr:
        ogrenci_list = ogr.readlines()
        ogr_dosya(ogrenci_list)
        e =0
        for i in ogrenci.keys():
            kac_yıl = int(ogrenci[i]["Kac_Yıllık"])

            if hesap[e] > kac_yıl:
                print("{} Id'li ogrencinin burs alma zamanı doldu.Bursu iptal edildi.".format(i))
                silinen.append(int(i))
                b = ogr_id.index(int(i))
                ogrenci_list.pop(b)
                ogr_id.pop(b)
                with open("ogrenci.txt", "w") as ogr:
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
    b = 100000
    aynı = -1
    paynı = -1
    baynı=-1
    kaynı=-1
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
        if x >= a:
            if x ==a:
                aynı = x
                kaynı = i
            else:
                a = x
                k = i

        if x <= b:
            if x ==b:
                baynı = x
                paynı = i
            else:
                b = x
                p = i
    print()
    if aynı == a:
       print("-> Kişi başına düşen aylık geliri en fazla olan öğrencilerin id'si = {} , {}".format(k,kaynı))
    else:
        print("-> Kişi başına düşen aylık geliri en fazla olan öğrenci id'si = {}".format(k))

    if baynı == b:
       print("-> Kişi başına düşen aylık geliri en fazla olan öğrencilerin id'si = {} , {}".format(p,paynı))
    else:
        print("-> Kişi başına düşen aylık geliri en fazla olan öğrenci id'si = {}".format(p))


def cikis():
    print("Programdan çıktınız.")
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
