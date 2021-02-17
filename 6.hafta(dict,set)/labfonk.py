# # #örnek1
# # import time
# #
# # def mukemmel_bul(adet,altlimit=0):
# #     sayac =0
# #     if altlimit <=0:
# #         altlimit = 1
# #     sayilar =list()
# #     def mukemmelmi(sayi):
# #         bolen_top = 0
# #         for i in range(1,sayi):
# #              if sayi%i == 0:
# #                 bolen_top +=i
# #         if bolen_top ==sayi:
# #                 return True
# #         else:
# #                 return False
# #     while sayac < adet:
# #         if mukemmelmi(altlimit):
# #                sayilar +=[altlimit]
# #                sayac = sayac + 1
# #         altlimit +=1
# #     return sayilar
# # start = time.time()
# # msayilar = mukemmel_bul(3 , 1)#6,28,496,8128,33550336
# # end = time.time()
# #
# # print(msayilar)
# # print("Time:{:.2f}".format(end-start))
#
# #2.ornek
# data_name = ["Id","Ad","Soyad","Maas","Cocuksay","Eskizam"]
# personel = None
# last_id = None
#
# def menu():
#     print("Personel Maas Zam Hesaplama Uygulaması")
#     print("Menu","----","1:Listele","2:Ara","3:Güncelle","4:Zam Hesapla","0:Çıkış",sep="\n")
#     secim = int(input("seçiminizi giriniz: "))
#     if secim == 1:
#         listele()
#     elif secim == 2:
#         pass
#     elif secim == 3:
#         pass
#     elif secim == 4:
#       pass
#     elif secim == 0:
#         exit()
#     else:
#         print("Yanlış Seçim Girdiniz:")
#
#
# def listele():
#     global personel
#
#     def file_read():
#         with open("personel.txt" , "r") as pfile:
#             personel_list = pfile.readlines()
#             per_format(personel_list)
#
#     def per_format(plist):
#         global personel
#         global last_id
#         for per in plist:
#             per_values = per.split(" ")
#             data = dict()
#             for ind in range(1,len(per_values)):
#                 data[data_name[ind]] = per_values[ind]
#                 personel[per_values[0]] = data
#                 last_id = per_values[0]
#     if personel == None:
#         personel = dict()
#         file_read()
#
#     for per_id in personel.keys():
#         print("per_İD={}".format(per_id),end =" ")
#         #tek tek yazma personel[per_id]["AdSoyad"]
#         for per_bilgi in personel[per_id].keys():
#             print("{:>5}={:8}".format(per_bilgi,personel[per_id][per_bilgi]),end=" ")
#         print()
# menu()
global ad
ad = "bilisim.text"
def dosyaac():
    sec = input("Dosya olusturmak istediğinizden eminmisiniz?")
    if sec == "E":
        ad = input("dosya adını giriniz:")
        ad = ad + ".text"
        with open(ad,"w") as dosya:
            dosya.close()
    if sec =="H":
        return
def listele():
    with open(ad,"r") as dosya:
        bilgiler = dosya.readlines()
        i=0
        for bilgi in bilgiler:
            print(i,".",bilgi)
            i+=1
def bilgiekle():
    with open(ad,"a") as dosya:
        bilgi = []
        bilgi.append(input("isim giriniz"))
        bilgi.append()
        bilgi.append(input("2.notu giriniz"))
        print(bilgi)
        dosya.writelines(bilgi)
def bilgisil():
    with open(ad,"r") as dosya:
        bilgiler = dosya.readlines()
        silinecek = int(input("silinecek numar giriniz:"))
        bilgiler.pop(silinecek)
    with open(ad,"w") as dosya:
        dosya.writelines(bilgiler)
while 1:
    x=int(input("bir sayı giriniz:"))
    if x==1:
        dosyaac()
    elif x==2:
        listele()
    elif x==3:
        bilgiekle()
    elif x==4:
        bilgisil()
    else:
        break;
























