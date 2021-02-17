"""
1.ornek : kullanicidan ad, soyad,dogum yili,ve bolum bilgilerini alip ,
ad soyad yas ve bolum bilgilerini ekrandaki ciktiya gore yaziniz.

ad='Dilara Sevim'
soyad='Polat'
yas=19
bolum='Bilgisayar muhendisligi'

print(ad,soyad,end="->")
print(yas,bolum,sep="->")
#ya da asagidaki gibide yazilabilir.
#print(ad+" "+soyad,yas,bolum,sep="->")

#kullanicidan alalim.
ad=input("adinizi giriniz:")
soyad=input("soyadinizi giriniz:")
yas = int(input("yasinizi giriniz:"))

print(ad,soyad,yas)
"""
#baska sekilde yazalim.
ad=input("adinizi giriniz:")
soyad=input("soyadinizi giriniz:")
yil=int(input("dogum yilinizi giriniz:"))

yas=2020-yil
print(ad,soyad,yas)




















