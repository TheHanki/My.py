import random
import time
print("Zar oyununa hoşgeldiniz!")
print("Oyun başlıyor...")
time.sleep(1)
bilgisayar=random.randint(1, 6)
print("Bilgisayarın seçimi", bilgisayar)
time.sleep(0.8)
karar=input("Zarı atmak istiyor musun? ")
while karar == "Evet" or karar == "evet":
    zar=random.randint(1, 6)
    if zar<bilgisayar:
        print("Attığınız zar:",zar)
        print("Kaybettiniz.")
        break
    elif zar>bilgisayar:
        print("Attığınız zar:",zar)
        print("Tebrikler Kazandınız!!")
        break
