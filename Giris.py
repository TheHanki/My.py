#Calani sikerim ez
import time
print("Giris yapmak icin adinizi ve sifrenizi girin")
isim=input("Kullanici adinizi giriniz:")
sifre=input("Sifrenizi giriniz:")

sayac = 0
while sayac == 0:
    if isim=="Arda":
        if sifre=="12345":
            print("Giris yapiliyor....")
            time.sleep(3)
            print("Giris yapildi, Hosgeldin Arda Delialioglu")
            sayac = 1
        else:
            print("Sifre yanlis, programi yeniden baslatip tekrar deneyin")
            break
    else:
        print("Kullanici adi yanlis, programi yeniden baslatip tekrar deneyin")
        break
