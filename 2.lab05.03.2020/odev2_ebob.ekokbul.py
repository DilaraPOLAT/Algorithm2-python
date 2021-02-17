"""
kullanici tarafindan girilen 2 sayinin
 EBOB ve EKOK unu bulan pyhton kodu...
"""
sayi_1=int(input("1.sayiya giriniz:"))
sayi_2=int(input("2. sayi giriniz:"))
ebob=1
ekok=1
if(sayi_2 > sayi_1):
  for i in range(2,sayi_1 + 1):
        if(sayi_1 % i==0 and sayi_2 % i==0):
            ebob=ebob*i
            sayi_1=sayi_1 //i
            sayi_2=sayi_2 //i
  ekok=ebob*sayi_1*sayi_2
else:
  for i in range(2,sayi_2 + 1):
        if(sayi_1 % i==0 and sayi_2 % i==0):
            ebob=ebob*i
            sayi_1=sayi_1 //i
            sayi_2=sayi_2 //i
  ekok = ebob * sayi_1 * sayi_2
print("ebob= {}".format(ebob))
print("ekok= {}".format(ekok))
