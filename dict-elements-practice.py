# Amaliyot
# 1.
python_dict = {
    'boolean': "mantiqiy qiymat",
    'integer': "butun son",
    'float': "o'nlik son",
    'string': "matn",
    'list': "ro'yxat",
    'tuple': "o'zgarmas ro'yxat",
    'dictionary': "lug'at",
    'print': "chop etish",
    'input': "foydalanuvchi kiritishi",
    'if': "agar (tarmoqlanuvchi operator)",
    'else': "aks holda",
}
for key, value in sorted(python_dict.items()):
    print(f"{key.title()} - {value}")

# 2.
country_capitals = {
    'uzbekistan': 'tashkent',
    'russia': 'moscow',
    'usa': 'washington',
    'france': 'paris',
    'italy': 'rome',
    'germany': 'berlin',
    'spain': 'madrid',
    'china': 'beijing',
    'japan': 'tokyo',
    'india': 'new delhi',
}

print("Dunyo davlatlari: ")
for country in sorted(country_capitals.keys()):
    print(country.upper())

print("Dunyo davlatlari poytaxtlari: ")
for capital in sorted(country_capitals.values()):
    print(capital.title())

# 3.
key = input("Davlat nomini kiriting: ").lower()
if country_capitals.get(key) == None:
    print("Bunday davlat mavjud emas.")
else:    
    print(f"{key.title()}ning poytaxti {country_capitals[key].title()} shahri.")