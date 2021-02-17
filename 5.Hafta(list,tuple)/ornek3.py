"""
ornek3:
liste veri tipi kullilarak kullanicidan alinan ogrenci isim,numara ve vize notu bilgilerini ayrı listelerde tutunuz.
tum ogrenci bilgilerini ve vize notu 70 den buyuk olan ogrencilerin bilgilerini ayri ayri aliniz.
"""
ogr_ad=[]
ogr_no=[]
ogr_vizenot=[]
syc=int(input("kac ogrenci bilgisi gireceksiniz:"))
for i in range(syc):
    ad=input("ogrencinin adini giriniz:")
    ogr_ad.append(ad)
    no=int(input("ogrencinin numarasini giriniz:"))
    ogr_no.append(no)
    vizenot=int(input("ogrencinin vize notunu giriniz:"))
    ogr_vizenot.append(vizenot)
#tum ogrenci bilgilerini listeleme
print("tum ogrenciler:")
for i in range(syc):
    print("{}. ogrencinin adi:{},numarasi:{} , vizenotu:{}".format(i+1,ogr_ad[i],ogr_no[i],ogr_vizenot[i]))
#vize notu 70 den buyuk ogrenci bilgilerini listeleme
print("vizenotu 70 den yuksek ogrenciler:")
for i in range(syc):
    if ogr_vizenot[i]>70:
        print("ogrencinin adi:{} , numarasi:{} , vizenotu:{}".format(ogr_ad[i],ogr_no[i],ogr_vizenot[i]))
