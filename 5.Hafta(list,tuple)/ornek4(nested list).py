"""
ornek4:
bir sirkete calisanlarin cocuk sayisina gore maaslarina zam yapilacaktir bu sirkete calisanlarin adini cocuk sayisini ve maasini kullanicidan
alarak listede tutunuz. cocuk sayisi 1 olan calisana 50Tl ,cocuk sayisi 2 olan calisana 75Tl ve cocuk sayisi 2 den fazla olan calisana
ise  cocuk basina 80Tl zam yapilacaktir.tum calisanlarin bilgilerini ve guncel maaslari listeleyiniz.
"""
calisanlar=[]
syc=int(input("sirketinizde kac calisaniz var:"))
for i in range(syc):
    calisanlar.append(list())
    ad=input("{}.calisanin ismi:".format(i+1))
    calisanlar[i].append(ad)
    cs=int(input("{}. calisanin cocuk sayisi:".format(i+1)))
    calisanlar[i].append(cs)
    maas=int(input("{}.calisanin maasi:".format(i+1)))
    calisanlar[i].append(maas)
#TUM CALİSANLAR
print("\n Tum calisanlar")
for i in range(syc):
    print("{}.calisanin adi :{}   cocuksayisi:{} maasi:{}".format(i+1,calisanlar[i][0],calisanlar[i][1],calisanlar[i][2]))
#Cocuk sayisina gore zam
for i in range(syc):
    if calisanlar[i][1]==1:
        calisanlar[i][2]+=50
    elif calisanlar[i][1] == 2:
        calisanlar[i][2] += 75
    elif calisanlar[i][1]>2:
        calisanlar[i][2]+=calisanlar[i][1]*80
    else:
        pass
print("\n Guncel maaslar")
for i in range(syc):
    print("{}.calisanin yeni maasi :{}".format(i+1,calisanlar[i][2]))











