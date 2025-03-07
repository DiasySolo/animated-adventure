import random

def hadani_cisla():
    cilove_cislo = random.randint(1, 100)
    pocet_pokusu = 0

    print("Hádej číslo mezi 1 a 100.")

    while True:
        pocet_pokusu += 1
        uzivatelske_cislo = int(input("Zadaj sve cislo: "))
        if uzivatelske_cislo < cilove_cislo:
            print("Cilove cislo je vetsi.")
        elif uzivatelske_cislo > cilove_cislo:
                print("Cilove cilso je mensi.")
        else:
            print(f"Gratulujeme! Uhodl jsi cílové číslo {cilove_cislo} po {pocet_pokusu} pokusech.")

hadani_cisla()
