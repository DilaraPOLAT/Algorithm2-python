"""
kullanicidan alinan sayiya kadar olan asal sayilari tespit eden program.
"""
sayi=int(input("bir sayi giriniz:"))
asalmi=1
sayac=0
for i in range(2,sayi+1):
    asalmi=1
    for  j in range(2,i):
        if(i%j==0):
            asalmi=0
            break;
    if (asalmi == 1):
          sayac = sayac + 1
          print(i, end="\t")




print("\n toplamda {} adet asal sayi bulundu!".format(sayac))




