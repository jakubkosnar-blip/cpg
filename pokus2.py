#if __name__ == "__main__":
    #vstup = input("Zadej cislo")
    # print(type(vstup))
    # vstup = int(vstup)
    # vysledek = vstup +1
    # print(type(vstup))
    # print(vysledek)
def faktorial(x):
    #vypocet faktorialu x! = x * (x-1) * (x-2)...
    if x == 1:
        return 1
    vysledek = x * faktorial(x - 1)
    return vysledek


if __name__ == "__main__":
        vysledek = faktorial(9)
        print(vysledek)