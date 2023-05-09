#ez made by Hanki
import time
import random
time.sleep(1)
kelimeler = ['buz', 'muz', 'laz']
rastgelekelime = random.choice(kelimeler)
ilkharf = str(input("İlk Harfi Giriniz: "))
loop=0
while loop==0:
    if rastgelekelime.find(ilkharf)==0:
        print("Doğru Gidiyorsun!!")
        ikinciharf = input("İkinci Harfi Giriniz: ")
        if rastgelekelime.find(ikinciharf)==1:
            print("Doğru!!")
            ucuncuharf = input("Üçüncü Harfi Giriniz:")
            if  rastgelekelime.find(ucuncuharf)==2:
                print("Kazandın!!!!!!!!!!!!!!!!!!")
                print("Tebrikler!")
                loop=1
            else:
                print("Bunu nasıl yapamıyorsun......")
                loop=1
        else:
            print("Yanlış...")
            loop=1
    else:
        print("Başarısız oldun.")
        print("Doğru kelime "+rastgelekelime)
        loop=1
