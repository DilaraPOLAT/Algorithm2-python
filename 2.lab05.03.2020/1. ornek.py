"""
kullanicidan alinan vize final notuna gore gecme notunu ve harfi hesplayan program
"""
vizenotu=int(input("vize notu giriniz:"))
finalnotu=int(input("final notu giriniz:"))
donemsonunotu=vizenotu*0.4+finalnotu*0.6
harfnotu=""
if(donemsonunotu<=30):
    harfnotu="FF"
elif(donemsonunotu<=60):
    harfnotu="CC"
elif(donemsonunotu<=90):
    harfnotu="BB"
else :
    harfnotu="AA"
print("donem sonu notu: {}\n harf notu {}".format(donemsonunotu,harfnotu))