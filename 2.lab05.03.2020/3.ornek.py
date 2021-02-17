"""
ornek3:maksimum 10 tahmin hakki bulunan sayi tahmin oyunu
"""
import random
rsayi=random.randint(1,100)
print("1-100 arasainda rasgele uretilen sayiyi 10 tahmin hakkinda bulmamizi isteyen program")

sayac=0
while (sayac<10):
    tahmin=int(input("sayi tahmininiz:"))
    sayac=sayac+1
    if(tahmin==rsayi):
        break;
    elif(tahmin<rsayi):
        print("malesef yanlis tahmin \n ipucu : daha buyuk sayi tahmin ediniz...")
    else:
        print("malesef yanlis tahmin \n ipucu : daha kucuk  sayi tahmin ediniz...")
if(sayac==10):
            print("10 tahmin hakkiniz doldu ,sayiyi bulamadiniz -> {}".format(rsayi))
else:
            print("tebrikler sayiyi buldunuz -> {}".format(rsayi))