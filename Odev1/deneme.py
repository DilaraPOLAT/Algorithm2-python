"""
kullanici tarafindan belirlenen  sifrenin
-  sifre en az 8,en fazla 12 karakter icermelidir.
-  sayi ile baslayip sayi ile bitemez.
-  en az 1 buyuk harf ve en az 1 kucuk harf karakteri icermelidir.
-  bosluk karakteri icermez.
-  sifre en az 1 tane alfanumerik olmayan karakter icermelidir.
-  sifre icinde tekrarlayan karakter bulunmamalidir.
-  sifrenin ilk harfi kucuk 'a'  olmamalidir.
-  sifre belirme hakki  10 dur.
"""
# DİLARA SEVİM POLAT 19010011064

# benim belirledigim iki ozellik: 10 sifre belirleme hakki ve ilk karakterin kucuk 'a' olmamasi
sayac1=1
print("- sifre belirme hakkiniz 10 dur! unutmayiniz. ")
x=input("{}. belirleme hakkiniz sifrenizi belirleyiniz:".format(sayac1))
m=int(len(x))

k=1;
b=1

for f in range(0,10):
       for i in range(m):
          if x.startswith(str(i)):
             sayac1 = sayac1 + 1
             if sayac1 <=10:
                 print("-> sifre rakam ile baslayamaz ! lutfen tekrar deneyniz...")
                 x = input("{}. belirleme hakkiniz sifrenizi tekrar belirleyiniz:".format(sayac1))
                 m = int(len(x))
                 break;
             else:
                 b=0
                 break;

          if x.endswith(str(i)):
             sayac1 = sayac1 + 1
             if sayac1 <= 10:
                 print("-> sifre rakam ile bitemez ! lutfen tekrar deneyiniz... ")
                 x = input("{}. belirleme hakkiniz sifrenizi tekrar belirleyiniz:".format(sayac1))
                 m = int(len(x))
             else:
                b=0
                break;


       for i in x:
            t = x.count(i)
            if (t != 1):
                sayac1 = sayac1 + 1
                if sayac1 <= 10:
                    print("-> sifrenizde tekrarlanan karakter bulunmamalidir ! lutfen  tekrar deneyiniz...")
                    x = input("{}. belirleme hakkiniz sifrenizi tekrar  belirleyiniz:".format(sayac1))
                    m = int(len(x))
                    break;
                else:
                    b=0
                    break;

       for i in range(m):
         if (i < m):
            if x[i] == ' ':
                sayac1 = sayac1 + 1
                if sayac1 <= 10:
                    print("-> sifrenizde bosluk bulunmamali ! lutfen tekrar deneyiniz... ")
                    x = input("{}. belirleme hakkiniz sifrenizi tekrar belirleyiniz:".format(sayac1))
                    m = int(len(x))
                    break;
                else :
                    b=0
                    break;

       if x.startswith("a") :
           sayac1 = sayac1 + 1
           if sayac1 <= 10:
             print("-> sifreniz ilk harfi a  olmamali ! luten tekrar deneyiniz... ")
             x = input("{}. belirleme hakkiniz sifrenizi tekrar belirleyiniz:".format(sayac1))
             m = int(len(x))
           else:
               b=0

       if x.isalnum():
         sayac1 = sayac1 + 1
         if sayac1 <= 10:
           print("-> sifrenizde alfanumerik olmayan  en az 1 tane karakter bulunamadi ! lutfen tekrar deneyiniz... ")
           x = input("{}. belirleme hakkiniz sifrenizi tekrar belirleyiniz:".format(sayac1))
           m = int(len(x))
         else:
             b=0

       if x.isupper():
         sayac1 = sayac1 + 1
         if sayac1 <= 10:
            print("-> sifrenizde en az bir kucuk harf bulunmali ! lutfen tekrar deneyiniz...")
            x = input("{}. belirleme hakkiniz sifrenizi tekrar belirleyiniz:".format(sayac1))
            m = int(len(x))
         else:
             b=0

       if x.islower():
          sayac1 = sayac1 + 1
          if sayac1 <= 10:
            print("-> sifrenizde en az bir tane buyuk harf bulunmali ! lutfen tekrar deneyiniz...")
            x = input("{}. belirleme hakkiniz sifrenizi tekrar belirleyiniz:".format(sayac1))
            m = int(len(x))
          else:
              b=0

       if(12 < len(x)):
          sayac1 = sayac1 + 1
          if sayac1 <= 10:
             print("-> sifre uzunlugu en fazla 12 karakter icermeli !  lutfen  tekrar deneyiniz...")
             x = input("{}. belirleme hakkiniz sifrenizi tekrar belirleyiniz:".format(sayac1))
             m = int(len(x))
          else:
              b=0

       if(8>len(x)):
          sayac1 = sayac1 + 1
          if sayac1 <= 10:
            print("-> sifre uzunlgu en az 8 karakter icermeli ! lutfen tekrar deneyiniz...")
            x = input("{}. belirleme hakkiniz sifrenizi tekrar belirleyiniz:".format(sayac1))
            m = int(len(x))
          else:
              b=0

       if sayac1>10:
           b = 0
           k=0
           break;
           #sayac 10 dan buyukkse for dongusunden cikar ve else blogunda b=0 ile 1. whilden cikar ya da
           #kosullarin hepsi saglanmissa for dan cikip 1.while den de cikar ve son while da kalir


if k==0:
       print("",end="\n")
       if sayac1<=10:
         print("<<< sifre basariyla olusturuldu tebrikler. >>>")
         k = 0
       else:
          print("<<< sifre belirleme hakkinizi astiniz !!! malesef sistem sizi disari atti. >>>")
          k=0
#son while else le kontrol edilir sayacim hala 10 ya da ondan kucukse gerken sartlarin hepsini sagliyorve sifre basriyla olusturuldu ekrana yazilir
#eger sayacim ondan buyukse sartlar dan biri ya da daha fazlasi saglanmamis else le print icindeki yazi ekrana yazilir