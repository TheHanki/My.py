#Ahmet Tahanin Tas Kagit makas oyunu ez
import random
secimler=["taş", "kağıt", "makas"]
bilgisayar=random.choice(secimler)
print("Taş Kağıt Makas Oyununa Hoşgeldin!!!")
giris=input("Seçiminizi Girin: ")
sayac=1

while True:
    if bilgisayar=="taş" and giris.lower()=="kağıt":
        print("Kazandın!!")
        print("Bilgisayarın seçimi:",bilgisayar)
        break
    elif bilgisayar=="kağıt" and giris.lower()=="makas":
        print("Kazandın!!")
        print("Bilgisayarın seçimi:",bilgisayar)
        break
    elif bilgisayar=="makas" and giris.lower()=="taş":
        print("Kazandın!!")
        print("Bilgisayarın seçimi:",bilgisayar)
        break
    elif bilgisayar=="taş" and giris.lower()=="makas":
        print("Kaybettin")
        print("Bilgisayarın seçimi:",bilgisayar)
        break
    elif bilgisayar=="kağıt" and giris.lower()=="taş":
        print("Kaybettin")
        print("Bilgisayarın seçimi:",bilgisayar)
        break
    elif bilgisayar=="makas" and giris.lower()=="kağıt":
        print("Kaybettin")
        print("Bilgisayarın seçimi:",bilgisayar)
        break
    elif giris.lower()=="messi":
        print("messi goat herkesi yener :sunglasses:")
        print("Bilgisayarın seçimi:",bilgisayar)
        break
