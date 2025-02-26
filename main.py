from abc import ABC,abstractmethod
from uuid import *

class Korzinka(ABC):
    @abstractmethod
    def __init__(self,ochilish,yopilish):
        self.__ochilish=ochilish
        self.__yopilish=yopilish

    def say_hi(self):
        return f"{self.ochilish} - {self.yopilish}"


n= input("ishlash vaqti>>")
if  n<"07:00":
    print("hali vahti bolmagan")

elif n>"23:00":
    print("biz yopildik")
else:
     print("hush kelibsiz")


class Joylashuv(Korzinka):
    def __init__(self,qator,sanogi,rangi,lokatsiya,kengligi):
        self.__qator=qator
        self.__sanogi =sanogi
        self.__rangi=rangi
        self.__lokatsiya=lokatsiya
        self.__kengligi=kengligi

    def joy(self):
        return f"{self.qator} - {self.sanogi} - {self.rangi} -{self.lokatsiya}- {self.kengligi}"

m=input("korzinka haqida malumot kerakmi>>")

if m.strip().lower()=="ha":
    print("6ta qator","5 ta filial","qizil va oq","sergili","1 gektar")
elif m.strip().lower()=="yoq":
    print("etiboringiz uchun ramat")
else:
    print("yaxshi")


class Human:
    def __init__(self,hodimlar,kassirlar,mijozlar,direktor):
        self.__hodimlar=hodimlar
        self.__kassirlar=kassirlar
        self.__mijozlar=mijozlar
        self.__direktor=direktor

    def inson(self):
        return f"{self.hodimlar} - {self.kassirlar} - {self.mijozlar} - {self.direktor}"

    def qabul(self,boyi,yoshi,tili):indent=4

class Hodim(Human):
    def say(self):
        return f"{self.hodim}"


def ishga_qabul():

        javob = input("Ishga qabul qilamiz. Rozimisiz? (ha/yo'q): ").strip().lower()

        if javob == "ha":
            ism = input("Ismingizni kiriting: ")
            yosh = input("Yoshingizni kiriting: ")
            telefon = input("Telefon raqamingizni kiriting: ")

            print("\nRahmat! Sizning ma'lumotlaringiz qabul qilindi.")
            print(f"Ism: {ism}\nYosh: {yosh}\nTelefon: {telefon}\n")
        elif javob == "yo'q":
            print("Keyingi nomzodga o'tamiz...\n")
        else:
            print("Iltimos, faqat 'ha' yoki 'yo'q' deb javob bering.")


ishga_qabul()


class Kassir(Human):
    def say(self):
        return f"{self.kassir}"
k=input("Siz ishga kirmoqchimisz malumot berilikmi?>>")

l=input("3 ta til biladimi,kulib turadimi>>")
if l =="ha":
    print("yaxshi")

elif l =="yoq":
    print("yoq bolmadingiz")
else:
    print("yoq")


class Mijoz(Human):

    def get(self):
        return f"{self.mijoz}"
mj=input(""
         "Mijozlarga otamiz:>>"
         "Mijoz puli yetadimi>>")
if mj =="ha":
    print("Mana mahsulotingiz")
elif mj == "yoq ":
    print("kechirarsiz qarzga berilmidi")
else:
    print("yoq")


dr=input("Direktor yaxshimi>>")
if mj =="ha":
    print("yaxshi")
elif mj == "yoq ":
    print("ozgartirishni oylab koramiz")
else:
    print("ayb sizda")


class Product:
    def __init__(self,mahsulot,muddati,narx,hisoblash):
        self.mahsulot=mahsulot
        self.muddati=muddati
        self.narx=narx
        self.hisoblash=hisoblash

    def malumot(self):
        return f"{self.mahsulot} -  {self.muddati} - {self.narx} - {self.hisoblash}"








