from persoane import *
print("\n1.Nastere\n")
print("2.Casatorie\n")
print("3.Divort\n")
print("4.Stare Civila\n")
print("5.Lista descendenti\n")
print("6.Grad rudenie\n")
print("7.Afisare persoane\n")
print(" '0' - iesire din meniu\n")
ch = str(input("Alegerea dumneavoastra : "))

# Se considera citirea datelor evenimentelor(nastere, casatorie, divort) ca fiind in ordine cronologica,
# altfel pot aparea divergente la determinarea unor grade de rudenie.

while ch != "0":
    if ch == "1":
        nume_mama = str(input("\nNume mama: "))
        prenume_mama = str(input("Prenume mama : "))
        nume_tata = str(input("Nume tata : "))
        prenume_tata = str(input("Prenume tata : "))
        prenume = str(input("Prenume copil : "))
        data_nasterii = str(input("Data nasterii (zz/ll/aa) : "))
        mama = cautare_persoana(nume_mama, prenume_mama)
        tata = cautare_persoana(nume_tata, prenume_tata)
        if mama is None:
            mama = Persoana(nume_mama, prenume_mama)
        if tata is None:
            tata = Persoana(nume_tata, prenume_tata)
        mama.nastere(tata, prenume, data_nasterii)
    if ch == "2":
        nume_sot = str(input("\nNume sot : "))
        prenume_sot = str(input("Prenume sot : "))
        nume_sotie = str(input("Nume sotie : "))
        prenume_sotie = str(input("Prenume sotie : "))
        data_casatorie = str(input("Data casatorie (zz/ll/aa) : "))
        sotie = cautare_persoana(nume_sotie, prenume_sotie)
        sot = cautare_persoana(nume_sot, prenume_sot)
        if sotie is None:
            sotie = Persoana(nume_sotie, prenume_sotie)
        if sot is None:
            sot = Persoana(nume_sot, prenume_sot)
        sot.casatorie(sotie, data_casatorie)
    if ch == "3":
        nume_familie = str(input("\nNume familie : "))
        prenume_sot = str(input("Prenumele sot : "))
        prenume_sotie = str(input("Prenume sotie : "))
        data_divort = str(input("Data divort (zz/ll/aa) : "))
        sotie = cautare_persoana(nume_familie, prenume_sotie)
        sot = cautare_persoana(nume_familie, prenume_sot)
        if sotie is not None and sot is not None:
            sot.divort(sotie, data_divort)
        else:
            print("\nFamilia nu exista.\n")
    if ch == "4":
        print("\nStarea civila a persoanei : \n")
        nume = str(input("Nume persoana : "))
        prenume = str(input("Prenume persoana : "))
        persoana = cautare_persoana(nume, prenume)
        if persoana is None:
            print("\nPersoana nu exista.\n")
        else:
            data_stare_civila = str(input("Data specificata (zz/ll/aa) : "))
            persoana.stare_civila(data_stare_civila)
    if ch == "5":
        nume = str(input("\nNume persoana : "))
        prenume = str(input("Prenume persoana : "))
        persoana = cautare_persoana(nume, prenume)
        if persoana is None:
            print("\nPersoana nu exista.\n")
        else:
            print("\nDescendentii lui {0} {1} :\n".format(nume, prenume))
            persoana.afisare_descendenti()
    if ch == "6":
        nume_persoana1 = str(input("\nNumele primei persoane : "))
        prenume_persoana1 = str(input("Prenume primei persoane : "))
        nume_persoana2 = str(input("Numele celei de-a doua persoane : "))
        prenume_persoana2 = str(input("Prenumele celei de-a doua persoane : "))
        persoana1 = cautare_persoana(nume_persoana1, prenume_persoana1)
        persoana2 = cautare_persoana(nume_persoana2, prenume_persoana2)
        if persoana1 is None or persoana2 is None:
            print("\nUna dintre persoane nu exista.\n")
        else:
            persoana1.grad_rudenie(persoana2)
    if ch == "7":
        print("\nLista persoane din localitate : \n")
        afisare_lista_persoane()

    print("\n1.Nastere\n")
    print("2.Casatorie\n")
    print("3.Divort\n")
    print("4.Stare Civila\n")
    print("5.Lista descendenti\n")
    print("6.Grad rudenie\n")
    print("7.Afisare persoane\n")
    print(" '0' - iesire din meniu\n")

    ch = str(input("Alegerea dumneavoastra : "))
