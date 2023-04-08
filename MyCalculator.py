#Benden izinsiz kullanan arabadan atlasin 4mi patlasin
from math import sqrt
from math import pow

print("Hanki'nin Hesap Mskinesine Hos Geldiniz!")
print("Matematik yapmani kolaylatiracagim!!")
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
        if islem == "-":
            print(birincisayi-ikincisayi)
        if islem == "x" or islem == "*":
            print(birincisayi*ikincisayi)
        if islem == "/":
            print(birincisayi/ikincisayi)
        if islem == "%":
            print(float(birincisayi%ikincisayi))
        if islem == "²" or islem == "usluhesaplama":
            print(pow(birincisayi, ikincisayi))
        if islem == "√" or islem == "√¯" or islem == "→" or islem == "karekokhesaplama":
            print("1.sayinin karekoku:",sqrt(birincisayi))
            print("2.sayinin karekoku:",sqrt(ikincisayi))
            
    if xyz == "+":
        hesaplama(number1,"+",number2)
    elif xyz == "-":
        hesaplama(number1,"-",number2)
    elif xyz == "*" or xyz == "x":
        hesaplama(number1,"*",number2)
    elif xyz == "/":
        hesaplama(number1,"/",number2)
    elif xyz == "%":
        hesaplama(number1,"%",number2)
    elif xyz == "²" or xyz == "usluhesaplama":
        hesaplama(number1,"usluhesaplama",number2)
    elif xyz == "√" or xyz == "√¯" or xyz == "→" or xyz == "karekokhesaplama":
        hesaplama(number1,"karekokhesaplama",number2)
        


