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
    print("hali ochilmagan😐🤚")

elif n>"23:00":
    print("biz yopildik🫥❌")
else:
     print("hush kelibsiz👤😁")


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
    print("etiboringiz uchun ramat👍")
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








class Transport:
    def __init__(self, davlat_raqami, turi):
        self.davlat_raqami = davlat_raqami
        self.turi = turi

    def __str__(self):
        return f"{self.turi} ({self.davlat_raqami})"

class ParkovkaJoy:
    def __init__(self, joy_raqami, joy_turi):
        self.joy_raqami = joy_raqami
        self.joy_turi = joy_turi
        self.band = False
        self.transport = None

    def transport_joylashtir(self, transport):
        if not self.band:
            self.transport = transport
            self.band = True
            return True
        return False

    def transport_chiqar(self):
        if self.band:
            self.transport = None
            self.band = False
            return True
        return False

    def __str__(self):
        return f"Joy {self.joy_raqami} ({self.joy_turi}) - {'Band' if self.band else 'Bosh'}"

class Parkovka:
    def __init__(self, sigimi):
        self.joylar = [ParkovkaJoy(i, "Yengil mashina") for i in range(1, sigimi + 1)]

    def bosh_joy_top(self):
        for joy in self.joylar:
            if not joy.band:
                return joy
        return None

    def transport_kirit(self, transport):
        joy = self.bosh_joy_top()
        if joy:
            joy.transport_joylashtir(transport)
            print(f"{transport} {joy} joyga qoyildi.")
        else:
            print("Bo‘sh parkovka joyi yoq.")

    def transport_chiqar(self, davlat_raqami):
        for joy in self.joylar:
            if joy.band and joy.transport.davlat_raqami == davlat_raqami:
                joy.transport_chiqar()
                print(f"Transport {davlat_raqami} {joy} joydan chiqarildi.")
                return
        print(f"Transport {davlat_raqami} parkovkada topilmadi.")

    def parkovka_holati(self):
        for joy in self.joylar:
            print(joy)