"""
quiz 1 sorusu:
1-100 arasinda üretilen sayi 70-75 arasinda olana kadar random sayilar üretiniz .
bu üretilen sayilar arasinda ardisik olarak en kucuk farka sahip (mutlak olarak)
iki sayiyi ve farkini ekrana yazdiriniz .
dizi ve liste kullanmayinz.
"""
import random

xsayi=100
minfark=100
k=1
while (k==1):
    rsayi = random.randint(1, 100)
    print(rsayi,end="\t")

    if(rsayi>=xsayi):
      a=int(rsayi-xsayi)
      b = xsayi
      xsayi=rsayi
      if(minfark>=a):
          minfark=a
          t = b
          m = rsayi

    else:
        a= int(xsayi- rsayi)
        b = xsayi
        xsayi = rsayi
        if (minfark >= a):
            minfark = a
            t=b
            m=rsayi
    if (70<rsayi and rsayi<75):
        k=0

print("\nmin fark {} ile {} arasinda ={}".format(t,m,minfark))



