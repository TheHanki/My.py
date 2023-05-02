#Benden izinsiz kullanan arabadan atlasin 4mi patlasin
#Cihanin hesap makinesi
from math import sqrt
from math import pow
import time

print("Cihan'in Hesap Makinesine Hos Geldin!")
print("Matematik yapmani kolaylatiracagim!!")
sonsuzhesaplama = 2

def Hesaplama():
    time.sleep(2)
    soru=input("Bir daha hesaplama yapmak istiyormusun? Evet yada Hayir yaz: ")
    if soru.lower() == "evet":
        sonsuzhesaplama = 2
    elif soru.lower() == "hayir" or soru.lower() == "hayır":
        print("Bay Bay!!")
        quit()

while sonsuzhesaplama == 2:
    number1 = int(input("Bir numara girin: "))
    xyz = input("Isleminizi Girin: ")
    number2 = int(input("Ikinci numarayi girin: "))
    if type(number1) != "str" and type(number2) != "str":
        def hesaplama(birincisayi, islem, ikincisayi):
            birincisayi = number1
            islem = xyz
            ikincisayi = number2
            if islem == "+":
                print(birincisayi+ikincisayi)
                sonsuzhesaplama = 1
            if islem == "-":
                print(birincisayi-ikincisayi)
                sonsuzhesaplama = 1
            if islem == "x" or islem == "*":
                print(birincisayi*ikincisayi)
                sonsuzhesaplama = 1
            if islem == "/":
                print(birincisayi/ikincisayi)
                sonsuzhesaplama = 1
            if islem == "%":
                print(float(birincisayi%ikincisayi))
                sonsuzhesaplama = 1
            if islem == "²" or islem == "usluhesaplama":
                print(pow(birincisayi, ikincisayi))
                sonsuzhesaplama = 1
            if islem == "√" or islem == "√¯" or islem == "→" or islem == "karekokhesaplama":
                print("1.sayinin karekoku:",sqrt(birincisayi))
                print("2.sayinin karekoku:",sqrt(ikincisayi))
                sonsuzhesaplama = 1
                
        if xyz == "+":
            hesaplama(number1,"+",number2)
            Hesaplama()
        elif xyz == "-":
            hesaplama(number1,"-",number2)
            Hesaplama()
        elif xyz == "*" or xyz == "x":
            hesaplama(number1,"*",number2)
            Hesaplama()
        elif xyz == "/":
            hesaplama(number1,"/",number2)
            Hesaplama()
        elif xyz == "%":
            hesaplama(number1,"%",number2)
            Hesaplama()
        elif xyz == "²" or xyz == "usluhesaplama":
            hesaplama(number1,"usluhesaplama",number2)
            Hesaplama()
        elif xyz == "√" or xyz == "√¯" or xyz == "→" or xyz == "karekokhesaplama":
            hesaplama(number1,"karekokhesaplama",number2)
            Hesaplama()
    else:
        print("Lutfen harf yerine sayi giriniz!!! Harflerle matematik yapamam :c")
        sonsuzhesaplama = 2
if sonsuzhesaplama != 2:
    print("Bay bay")
