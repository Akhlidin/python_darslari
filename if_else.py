# -*- coding: utf-8 -*-
"""
Akhlidin Shermatov Sharobiddin o'g'li
Created on Wed Nov 10 08:42:35 2021

@author: Axlidin
"""

# son = -50
# if son<0:
#     print("manfiy son")
# else:
#     print("musbat son")
    
# yosh = int(input("yoshingizni kiriting:"))
# if yosh<=4:
#    narh = 0
# elif yosh<=10:
#    narh = 5000
# elif yosh<=15:
#    narh = 8000
# else:
#     narh = 10000
# print(f"sizga kirish {narh} so'm")
# kun = input("bugun nima kun?")
# if kun.lower() == "shanba" or kun.lower() == "yakshanba":
#     print("bugun dam olish kuni.")
# else:
#     print("bugun ish kuni.")
# kun = input("bugun kun nima?\n>>>")
# harorat = float(input("havo harorati qanday?\n>>>"))
# if (kun.lower()=='yakshanba' or kun.lower()== 'shanba') and harorat>=30:
#     print('cho\'milgani ketdik,')

# elif (kun.lower()=='yakshanba' or kun.lower()== 'shanba')  and harorat<30:
#     print("uyda dam olamiz.")
# else:
# #     print("bormaymiz")
# kun = input("bugun nima kun?")
# harorat = float(input("havo xarorati qanday?"))

# if kun.lower()=='shanba' and harorat>=30:
#     print("cho'milishga olg'a")
# elif kun.lower()=='shanba'  and harorat<30:
#     print("uydamiz")
# narh = 10000
# choy = True
# salat = True

# if choy and salat:
#     narh = narh + 10000
# elif choy or salat:
#     narh = narh + 5000
    
# print(f"jami {narh} so'm ")
# narh = 15000
# choy = True 
# salat = True
# non = False
# kompot = True
# ovqat = True

# if choy:
#     print("mijoz choy oldi,")
#     narh = narh + 2000
    
# if salat:
#     print("mijoz salat oldi,")
#     narh = narh + 5000
    
# if kompot:
#     print("mijoz kopmot oldi,")
#     narh = narh + 1000
    
# if ovqat:
#     print("mijoz ovqat oldi,")
#     narh = narh + 3000
# print(f"jami {narh} so'm")
    
# menu = ["osh", "sho'rva","shashlik", "somsa", "qozonkabob"]
# ovqat = input("nima ovqat buyurtma qabul qilasiz/n>>>") 
# if ovqat.lower() in menu:
#      print("buyurtma qabul qilindi")
# else:
#     print("afsuski bizda bunday ovqat yo'q")
   
# menu = ["osh", "sho'rva","shashlik", "somsa", "qozonkabob"]
# ovqat = input("nima ovqat buyurtma qabul qilasiz/n>>>") 
# if ovqat.lower() not in menu:
#     print("afsuski bizda bunday ovqat yo'q")   
# else:
 
#     print("buyurtma qabul qilindi")
# menu = ["osh", "shashlik", "somsa", "manti"]
# buyurtmalar = ["somsa", "osh", "shashlik", "sho'rva"] 
 
# if buyurtmalar:
#     for taom in buyurtmalar:
#         if taom in menu:
#             print(f"menuda {taom} bor")
        
#         else:
#             print(f"kechirasiz menuda {taom} yo'q")

# else:
#     print("savatchangiz bo'sh")        
# # # Amaliyot
# son = float(input("juft son kiriting:"))
# if son%2:

#     print("juft son yozing")
# else:
    
#     print("rahmat")
# yosh = int(input("yoshingizni kiriting>>>"))
# if yosh<=4 or yosh>=60:
    
#     print("sizga krish bepul")
# elif yosh<18:
#     print("sizga kirish 50000")
    
# else:
#     print("sizga kirish 10000"
# x = float(input("birinchi sonni kiriting: "))
# y = float(input("ikkinchi sonni kiriting : "))
# if x==y:
#     print(f"{x}={y}")
# elif x<y:
#     print(f"{x}<{y}")
# else:
#     print(f"{x}>{y}")  
# mahsulotlar = {"olma", "non", "olma suvi", "tarvuz", "ichimlik", "to'rt", "mevalar"}
# savat =[]
# savat = input("5ta mahsulot tang?>>>")
# if savat.lower() in mahsulotlar:
#     print("mahsulot do'konmizda bor.")
# else :
# #     print("mahsulot bizning do'konimizda yo'q.")
# mahsulotlar = ['olma', 'uzum', 'non', 'kalbassa', 'piyoz', 'guruch', 'sabzi']
# savat = []

# for n in range(5):
#      savat.append(input(f"savatga {n+1}-mahsulotni qo'shing>>>"))
# # for mahsulot in savat:
# #     if mahsulot in mahsulotlar:
# #         print(f"do'konimizda {mahsulot} bor")
# #     else:
# #         print(f"do'konimizda {mahsulot} yo'q.")
# # mahsulot1 = input("5 ta mahsulot kiriting: ")
# bor_mahsulot = []
# yoq_mahsulot = []
# # for n in range(5):
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         bor_mahsulot.append(mahsulot)
#     else:
#         yoq_mahsulot.append(mahsulot)
# if yoq_mahsulot:
#     print(f"do'konimizda quyidagi mahsulotolar yo'q: ")
#     for mahsulot in yoq_mahsulot:
#         print(mahsulot)
    
# else:
#     print("siz so'ragan barcha mahsulotlar do'konimizda bor.")
# foydalanuvchilar = ["axlidin", "ali", "salim", "xusniddin", "nuriddin"]
# f = input(f"login tanleng: ")
# if f in foydalanuvchilar:
#     print("login band,  boshqa login tanlang! ")
# else:
#     print("xush kelibsiz")

# son = int(input("istalgan butun son kiriting: "))
# for n in range(2, 11):
#     if not (son%n):
#         print(f"{son} {n} ga qoldiqsiz bo'linadi.")