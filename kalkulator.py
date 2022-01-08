
def suma(zmienna_x,zmienna_y):
    return(zmienna_x + zmienna_y)
print(suma(zmienna_x,zmienna_y))

def roznica(zmienna_x,zmienna_y):
    return(zmienna_x - zmienna_y)
print(roznica(zmienna_x,zmienna_y))

def iloczyn(zmienna_x,zmienna_y):
    return(zmienna_x * zmienna_y)
print(iloczyn(zmienna_x,zmienna_y))

def iloraz(zmienna_x,zmienna_y):
    return(zmienna_x / zmienna_y)
print(iloraz(zmienna_x,zmienna_y))

if __name__ == "__main__":
    zmienna_x = int(input("podaj zmienna_x: "))
    zmienna_y = int(input("podaj zmienna_y: "))
    dzialanie = input("""
Podaj liczbę aby wybrać odpowiednie działanie:
1 - Dodawanie
2 - Odejmowanie
3 - Mnozenie
4 - Dzielenie
""")   
   
    if dzialanie == 1:
        suma(zmienna_x,zmienna_y)
    if dzialanie == 2:
        roznica(zmienna_x,zmienna_y)
    if dzialanie == 3:
        iloczyn(zmienna_x,zmienna_y)
    if dzialanie == 4:
        iloraz(zmienna_x,zmienna_y)