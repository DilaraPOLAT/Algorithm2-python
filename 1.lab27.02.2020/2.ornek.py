"""
2.ornek:kullanicidan alinan iki float sayinin toplam,fark,bolum,carpım,us,mod islemlerini hesaplayiniz
"""
sayi_1=float(input("birinci sayiya giriniz:"))
sayi_2=float(input("ikinci sayiya giriniz:"))

toplam=sayi_1+sayi_2
fark=sayi_1-sayi_2
bolum=sayi_1/sayi_2
carpim=sayi_1*sayi_2
us=sayi_1**sayi_2
mod=sayi_1%sayi_2

print("sayi_1,sayi_2")
print(toplam,fark,bolum,carpim,us,mod,sep="\n")
#ya da asagidaki gibi yazilabilir
#print("toplam:",sayi_1+sayi_2)seklinde de yazilabilir.
