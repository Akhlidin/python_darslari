# -*- coding: utf-8 -*-
"""
Shermatov Akhlidin Sharobiddin o'g'li

Created on Tue Nov 23 21:56:28 2021

@author: Axlidin
"""

# talaba = {
#     'ism': 'Akhlidin',
#     'yosh': 25,
#     'yil': 1996,
#     't_joy': 'Andijon',
#     'kurs': 2
#     }
# print(talaba.items())

# for kalit, qiymat in talaba.items():
#     print(f"kalit:n {kalit}")
#     print(f"qiymat: {qiymat} \n")
# telefon = {
#     'ali': 'iphone',
#     'salim': 'samsung',
#     'vali': 'redmi',
#     'anvar': 'nokia',
#     'olim': 'iphone'
#     }
# for k, q in telefon.items():
# #     print(f"{k.title()}ning telefoni {q}")
# mahsulotlar = {
#     'olma': 10000,
#     'uzum': 4000,
#     'anjir': 5000,
#     'nok': 2000
#     }
# print('Do\'kondagi mahsulotlar: ')
# for mahsulot in mahsulotlar:
#     print(mahsulot.title())
# for k, q in mahsulotlar.items():
#     print(f"kalit: {k}")
#     print(f"qiymat: {q}")
# bozorlik = ['olma', 'non', 'nok', 'go\'sht']
# for mahsulot in mahsulotlar:
#     if mahsulot in bozorlik:
#         print(f"{mahsulot.title()} {mahsulotlar [mahsulot]} so\'m")
        
# for n in bozorlik:
#     if n not in mahsulotlar:
#         print(f"iltimos do'koningizga {n} ham olib kelind!")
# print("do'konimizdagi mahsulotlar")
# for mahsulot in sorted(mahsulotlar):
#     print(mahsulot.title())
# print("foydalanuvchilar quyidagi telefonlar ishlatishadi: ")
# for tel in set(telefon.values()):
#     print(tel)    
    
# toys = {'ball', 'doll', 'car', 'lego', 'ball'}
# print(toys)

# AMALIYOT
# words = {
#         'boolean': 'mantiqiy qiymat',
#         'for': 'biror narsani qayta-qayta bajarish stsikli',
#         'if': 'agar, shartlarni tekshirish operatori',
#         'integer': 'butunson'
#         }
# for key, value in sorted(words.items()):
#     print(f"{key.title()} - {value} ")

# Dunyo davlatlari:  Davlatlarning poytaxtlari

# davlatlar = {
#     'o\'zbekiston': 'Tashkent',
#     'amerika': 'vashington',
#     'rossia': 'moskwa',
#     'qirg\'izton': 'bishkek',
#     'italiya': 'rim',
#     'ispaniya': 'madrid'
#     # 'germaniya': 'berlin',
#     # 'uk': 'london'
#     }
# print("dunyo davalatlari: ")

# for davlat in sorted(davlatlar):
#     print(davlat.upper())
    
# print('\ndavlarlarning poytaxtlari')
# for poytaxt in sorted(davlatlar.values()):
#     print(poytaxt.upper())
    
# country = input('qaysi davlatni bilishni istaysiz? ').lower()
# capital = davlatlar.get(country)
# if capital == None:
#     print('kechirasiz, bizda bu haqida ma\'lumot yo\'q')
# else:
#     print(f"{country.upper()}ning poytaxti {capital.title()} shahri.")
menu = {
        'osh': 15000,
        'sho\'rva': 12000,
        'shashlik': 10000,
        'monti': 80000,
        'lag\'mon': 11000,
        'dimlama': 15000,
        'somsa': 10000,
        'mastava': 11000
        }
print(' 3 ta taomga buyurtma bering.')
buyurtmalar = []
for n in range(3):
    buyurtmalar.append(input(f"{n+1}-taom:").lower())
for buyurtma in buyurtmalar:
    if buyurtma in menu:
        print(f"{buyurtma.title()} {menu[buyurtma]}so\'m")
    else:
        print(f"kechirasiz, bizda {buyurtma} yo\'q")
        
for n in menu:
    if n not in menu:
        print(f"iltimos {n} xam tayyorlaselar")