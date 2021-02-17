"""
ornek1:
verilen bir liste icindeki listedeki sayilarin baska bir liste icinde olup olmadigini
kontrol eden python kodunu yaziniz.
"""
#program kontrol elemanları ile cozum.

liste1=[[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15]]
liste2=[99,4,10,7,11,45,85,2,10,45,7,6,1,2,3,4,5,6,7,8,9,10]

# for nestlist in liste1:
#     temp = []
#     for item in nestlist:
#       if item in liste2:
#         temp += [item]
#     if nestlist == temp:
#         print(nestlist)


#liste uretecleri ile cozum.
for i in liste1:
    ortak=[z for z in i if z in liste2]
    if len(ortak)== len(i):
        print(i)

