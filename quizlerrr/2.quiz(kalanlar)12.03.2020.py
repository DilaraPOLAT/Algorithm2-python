"""
guiz 2 sorusu:
1-100 arasinda uretilen sayi 50-55 arasinda olana kadar random sayilar üretiniz .bu üretilen sayilar
arasinda ardişik olarak en cok tekrar eden cift sayi adetini ve en cok tekrar eden tek sayi adetini
ve en cok tekrar eden tek sayi adetini bulup ekrana yazdiriniz .
dizi ve liste kullanmayiniz.

"""
import random
csayac=0
tsayac=0
k=-1
b=0
a=0
while True:
    sayi=random.randint(1,100)
    print(sayi,end="\t")

    if(sayi%2==0 and k%2==0):
        k = sayi
        csayac=csayac+1
        if(b<=csayac):
            b=csayac

    elif(sayi%2!=0 and k%2!=0):
        k = sayi
        tsayac=tsayac+1
        if(a<=tsayac):
            a=tsayac

    else:
       if(sayi%2==0):
           if (csayac >= 1):
               csayac = 0
           csayac = csayac + 1
           k=sayi

       else:
          if (tsayac >= 1):
             tsayac = 0
          tsayac=tsayac+1
          k=sayi

    if (sayi <= 55 and sayi >= 50):
        break;
print(end="\n")
print("ardisik olarak en fazla tekrar eden cift sayi adeti {} \nardisik olarak en fazla tekrar eden tek sayi adeti {}".format(b,a))






