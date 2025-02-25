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

k=input("Hodim boyini kiriting>>")

if k<"160":
    print("kechirarsiz togri kelmadiz")
elif k>160:
    print("hush kelibsiz")
else:
    print("hush kelibsiz")


l=input("3 ta til biladimi,kulib turadimi>>")
if l =="ha":
    print("yaxshi")
elif l =="yoq":
    print("yoq bolmadingiz")
else:
    print("yoq")


mj=input("Mijoz puli yetadimi>>")
if mj =="ha":
    print("Mana mahsulotingiz")
elif mj == "yoq ":
    print("kechirarsiz qarzga berilmidi")
else:
    print("yoq")


dr=input("")



