"""
kullanici tarafindan girilen sayinin asal bolenlerini bulan ve
ekrana yazdiran pyhton kodu...
"""
sayi=int(input("bir sayi giriniz:"))
asalmi=1
for i in range(2,sayi+1):
    asalmi=1
    for  j in range(2,i):
        if(i%j==0):
            asalmi=0
            break;
    if (asalmi == 1):
          if(sayi%i==0):
              print(i, end="\t")









