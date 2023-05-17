#Çalanı sikerim
import time
boy=float(input("Boyunuzu giriniz: "))
kilo=int(input("Kilonuzu giriniz: "))
boy2=boy*boy
endeks=kilo/boy2
time.sleep(1)

while endeks!= 40:
    if endeks <18:
        print("Zayıfsınız")
        break
    elif endeks >= 18 and endeks <25 :
        print("Normal kilodasınız")
        break
    elif endeks >= 25 and endeks <30:
        print("Kilolusunuz")
        break
    elif endeks >= 30 and endeks <35:
        print("Obezsiniz")
        break
    else:
        print("Ciddi obezite!!")
        break
