import math
# x = float(input("Birinchi sonni kiriting: "))
# y = float(input("Ikkinchi sonni kiriting: "))
# a = x + y
# b = math.pow(y, 2)
# c = b + 2
# d = x + math.pow(x, 3) / 5
# e = math.exp(y + 2)
# c1 = a / (b + math.fabs(c / d)) + e
# print(c1)

# a = float(input("Birinchi sonni kiriting: "))
# b = float(input("Ikkinchi sonni kiriting: "))
# c = math.pow(a, 1 / 5)
# d = (a + b) * b
# e = 2 * b + a * b
# f = math.pow(a, 2) + math.pow(b, 2) + 2
# t = c + math.pow(d / e, 1 / 4) * f
# print("%.2f" % t)
# print("%.2f" % 15.7861527239)

# a = int(input("Birinchi sonni kiriting: "))
# b = int(input("Ikkinchi sonni kiriting: "))
# c = int(input("Uchinchi sonni kiriting: "))
# x = float(input("To'rtinchi sonni kiriting: "))
# e = a / 4 + b / 3 + c / 2 + 1
# f = math.fabs(math.pow(x, 3) + 3 * x)
# d = math.cos(x - 2)
# t = 8.2 * math.pow(x, 2)
# w1 = 0.75 + (t + math.sqrt(f + d)) / e
# print("%.2f" % w1)

x = float(input("Birinchi sonni kiriting"))
y = float(input("Ikkinchi sonni kiriting"))
a = math.pow(x, 2) + 1
b = x * y + math.pow(y , 2)
c = y + x * y
d = math.fabs(x * y) + 5
e = a / (math.pow(x, 2) + b / (math.pow(y, 2) + c / d))
f = 1 / (1 + math.cos(x) + 1 / math.sin(math.fabs(x)))
t11 = e + f
print("%.2f" % t11)