g=input("ФИО:")
a=g.split()
h=len(g.replace(" ", ""))+2
print("Инициалы:",(a[0][0]+a[1][0]+a[2][0]).upper()+'.')
print("Длина(символов)",h)