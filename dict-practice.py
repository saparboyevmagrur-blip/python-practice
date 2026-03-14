otam = {'ismi':'mavlutdin', 'tyil':1954,'viloyat':'samarqand'}
tyil = otam['tyil']
vil = otam['viloyat']
print(f"Otamning ismi {otam['ismi'].title()}, {tyil}-yilda, {vil.title()} viloyatida tug'ilgan")

taomlar = {
    'ali':'osh',
    'vali':'shashlik',
    'hasan':"lag'mon",
    'husan':"mastava",
    'olim':"somsa"
    }

taom = taomlar['ali']
print(f"Alining sevimli taomi {taom}")

python_izohli_lugati = {
    'integer':"Butun son",
    'float':"O'nlik son",
    'string':"Matn",
    'list':"Ro'yxat",
    'tuple':"O'zgarmas ro'yxat"}
# print(python_izohli_lugati['tuple'])

kalit = input("Kalit so'z kiriting:").lower()
print(python_izohli_lugati.get(kalit,"Bunday so'z mavjud emas"))

kalit = input("Kalit so'z kiriting:").lower()
tarjima = python_izohli_lugati.get(kalit)
if tarjima==None:
    print("Bunday so'z mavjud emas")
else:
    print(f"{kalit.title()} so'zi {tarjima} deb tarjima qilinadi")

# Dictionary ga yangi element qo'shish
print("\n--- Yangi element qo'shish ---")
talaba = {'ismi': 'Ali', 'yoshi': 20}
talaba['kurs'] = 2
talaba['fakultet'] = 'Informatika'
print(talaba)

# Dictionary elementini o'zgartirish
print("\n--- Elementni o'zgartirish ---")
talaba['yoshi'] = 21
print(talaba)

# Dictionary dan element o'chirish
print("\n--- Element o'chirish ---")
del talaba['kurs']
print(talaba)

# pop() metodi bilan o'chirish
yosh = talaba.pop('yoshi')
print(f"O'chirilgan yosh: {yosh}")
print(talaba)

# Dictionary bo'ylab takrorlash
print("\n--- Dictionary bo'ylab takrorlash ---")
for kalit in talaba:
    print(f"{kalit}: {talaba[kalit]}")

# keys(), values(), items() metodlari
print("\n--- Kalitlar ---")
print(talaba.keys())
print("\n--- Qiymatlar ---")
print(talaba.values())
print("\n--- Juftliklar ---")
print(talaba.items())

# Ichki dictionary (nested dictionary)
print("\n--- Ichki dictionary ---")
sinf = {
    'talaba1': {'ismi': 'Ali', 'ball': 85},
    'talaba2': {'ismi': 'Vali', 'ball': 90},
    'talaba3': {'ismi': 'Hasan', 'ball': 78}
}
print(sinf)
print(f"Talaba1 ning ismi: {sinf['talaba1']['ismi']}")

# Dictionary comprehension
print("\n--- Dictionary comprehension ---")
kvadratlar = {x: x**2 for x in range(1, 6)}
print(kvadratlar)

# Kalit mavjudligini tekshirish
print("\n--- Kalit mavjudligini tekshirish ---")
if 'ismi' in talaba:
    print("Ismi kaliti mavjud")
else:
    print("Ismi kaliti yo'q")

# get() metodi bilan xavfsiz kirish
print("\n--- get() metodi ---")
manzil = talaba.get('manzil', 'Noma\'lum')
print(f"Manzil: {manzil}")

# Dictionary ni tozalash
print("\n--- Dictionary ni tozalash ---")
talaba_copy = talaba.copy()
talaba_copy.clear()
print(f"Toza dictionary: {talaba_copy}")
print(f"Asl dictionary: {talaba}")