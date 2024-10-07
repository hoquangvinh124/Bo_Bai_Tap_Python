#Bai tap 58
import math

xA = float(input("xA: "))
yA = float(input("yA: "))
xB = float(input("xB: "))
yB = float(input("yB: "))


def Tinhdodaivecto (xA, yA, xB, yB):
   Do_Dai_AB = math.sqrt(((xB - xA) ** 2) + ((yB - yA) ** 2) )
   return round(Do_Dai_AB, 2)


print("Do Dai cua vecto AB: ", Tinhdodaivecto(xA, yA, xB, yB))




