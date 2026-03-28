# Amaliyot
# 1. 
# def tugilgan_yil_hisoblang(ism, yosh):
#     """Foydalanuvchining ismi va yoshini qabul qilib, 
#     uning tug'ilgan yilini hisoblaydigan funksiya"""
#     yil = 2026 - yosh
#     print(f"{ism}, siz {yil}-yilda tug'ilgansiz.")

# name = input("Ismingizni kiriting: ")
# age = int(input("Yoshingizni kiriting: "))
# tugilgan_yil_hisoblang(name, age)

# 2.
# def kvadrat_kub_hisobla(son):
#     kvadrat = son ** 2
#     kub = son ** 3
#     print(f"{son} ning kvadrati: {kvadrat}, kubi: {kub}")

# son = int(input("Son kiriting: "))
# kvadrat_kub_hisobla(son) 
# 3
# def juft_toq(n):
#     if n % 2 == 0:
#         print(f"{n} juft son.")
#     else:      
#          print(f"{n} toq son.")

# son = int(input("Son kiriting: "))
# juft_toq(son)

# 4
# def katta_kichik(a, b):
#     if a > b:
#         print(f"{a} katta, {b} kichik.")
#     elif a < b:
#         print(f"{b} katta, {a} kichik.")
#     else:
#         print("Ikkala son teng.")

# son1 = int(input("Birinchi sonni kiriting: "))
# son2 = int(input("Ikkinchi sonni kiriting: "))
# katta_kichik(son1, son2)

# 5 va 6
# def darajani_hisoblash(x, y=2):
#     print(f"{x} ning {y} darajasi: {x ** y}")

# x = int(input("Asos sonni kiriting: "))
# y = int(input("Daraja sonini kiriting: "))
# darajani_hisoblash(x,y)

# 7.
def bolinishni_hisobla(n):
    for i in range(2, 11):
        if n % i == 0:
            print(f"{n} soni {i} ga bo'linadi.")   
son = int(input("Son kiriting: "))
bolinishni_hisobla(son)