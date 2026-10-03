def secti(a,b,c):
    # funkce secte 3 cisla a,b,c8 a vrati vysledek pomoci return
    # moje řešení return (a+b+c)
    # lepší výsledek
    vysledek = a+b+c
    return vysledek

def je_delitelne_3(x):
    vysledek = x % 3
    if vysledek == 0:
        aa = True
    else:
        aa = False
    return aa

if __name__ == "__main__":
    #x = secti(1,2,3)
    #print("Vysledek:",x)

    x = je_delitelne_3(366)
    print("Je delitelne:",x)