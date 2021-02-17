"""
ornek2:
rasgele uretilen bir listenin elemanlarinin frekans degerlerini bulan ve en yuksek frekans
degerine sahip sayiyi gosteren python kodunu yazınız.
"""
import random

randlist=[random.randint(1,100) for i in range(100)]
print(randlist)
freq=[0]*100
max_freq=0
max_num=0
# for num in range(1,100):
#     for item in randlist:
#         if num ==item:
#             freq[num]+=1
#     if max_freq < freq[num]:
#         max_freq=freq[num]
#         max_num=num
# print(freq)
# print("maks.frekans = {} ,sayi ={}".format(max_freq,max_num))

#2.YOL:
# for num in range(1,100):
#     for item in randlist:
#         if num ==item:
#            freq[num] += 1
# max_freq=max(freq)
# max_num=freq.index(max_freq)
# print(freq)
# print("maks.frekans = {} ,sayi ={}".format(max_freq,max_num))

#3.yol:
# for num in range(1,100):
#     freq[num] = randlist.count(num)
# max_freq = max(freq)
# max_num=freq.index(max_freq)
# print(freq)
# print("maks.frekans = {} ,sayi ={}".format(max_freq,max_num))

#4.YOL:
freq=[randlist.count(num) for num in range(1,100)]
max_freq = max(freq)
max_num=freq.index(max_freq)
print(freq)
print("maks.frekans = {} ,sayi ={}".format(max_freq,max_num))


