from datetime import datetime
lista_persoane = []  # o lista ce retine toate persoanele din localitate


def cautare_persoana(nume, prenume):
    # cauta o persoana in lista de persoane dupa nume si prenume
    for persoana in lista_persoane:
        if persoana.nume_persoana == nume and persoana.prenume_persoana == prenume:
            return persoana
    return None  # returneaza 'None' daca nu o gaseste


def afisare_lista_persoane():
    # afiseaza toate persoanele din localitate (nume, prenume)
    iterator = 1
    for persoana in lista_persoane:
        print(iterator, end='.')
        print(persoana)
        iterator += 1


class Persoana:

    def __init__(self, nume, prenume, data="01/01/1900"):
        # creeaza o persoana ca fiind  o persoana "straina" localitatii (nu se cunosc parintii)
        # sau "stramos" (radacina a unui arbore genealogic)
        #
        # nume - numele persoanei
        # prenume - prenumele persoanei
        # data - data nasterii, 01/01/1900 ca default

        self.__sot_sotie = None
        # un pointer catre o persoana, ce va reprezenta sotul/sotia lui self
        self.nume_persoana = nume
        self.prenume_persoana = prenume

        self.__mama = None
        self.__tata = None
        # pointeri catre persoane ce vor reprezenta mama si tatal lui self,
        # ajuta la parcurgerea bottom-up a arborelui

        self.__data_nasterii = data

        self.__lista_copii = []
        # lista de pointeri catre persoanele ce vor reprezenta copiii lui self

        self.__lista_stare_civila = []
        # o lista ce va contine informatii referitoare la casatorii si divoruri

        lista_persoane.append(self)
        # adaugam persoana in lista de persoane din localitate

    def __str__(self):
        return self.nume_persoana + " " + self.prenume_persoana + "\n"

    def get_sot_sotie(self):
        return self.__sot_sotie

    def set_sot_sotie(self, sot_sotie):
        self.__sot_sotie = sot_sotie

    def get_mama(self):
        return self.__mama

    def set_mama(self, mama):
        self.__mama = mama

    def get_tata(self):
        return self.__tata

    def set_tata(self, tata):
        self.__tata = tata

    def get_data_nasterii(self):
        return self.__data_nasterii

    def set_data_nasterii(self, data):
        self.__data_nasterii = data

    def get_lista_copii(self):
        return self.__lista_copii

    def add_lista_copii(self, copil):
        self.__lista_copii.append(copil)

    def get_lista_stare_civila(self):
        return self.__lista_stare_civila

    def add_lista_stare_civila(self, stare, persoana, data):
        self.__lista_stare_civila.append([stare, persoana, data])

    def casatorie(self, sotie, data):
        # sotie - un obiect de tip Persoana
        # data - data casatoriei

        self.__sot_sotie = sotie
        sotie.set_sot_sotie(self)
        # creeaza o dubla legatura de la sot->sotie si de la sotie->sot

        sotie.nume_persoana = self.nume_persoana
        # sotia va primi numele sotului

        self.__lista_stare_civila.append(["Casatorit/a", sotie, data])
        sotie.add_lista_stare_civila("Casatorit/a", self, data)
        # adauga informatii referitoare la casatorie in listele ambelor persoane

    def divort(self, sotie, data):
        # sotie - un obiect de tip Persoana
        # data - data divortuli

        self.__sot_sotie = None
        sotie.set_sot_sotie(None)
        # distruge legaturile sot->sotie si sotie->sot

        self.__lista_stare_civila.append(["Divortat/a", sotie, data])
        sotie.add_lista_stare_civila("Divortat/a", self, data)
        # adauga informatii referitoare la divort in listele ambelor persoane

    def nastere(self, tata, prenume_copil, data):
        # self - mama copilului
        # tata - tatal copilului
        # data - data nasterii

        copil = Persoana(tata.nume_persoana, prenume_copil, data)

        copil.set_mama(self)
        copil.set_tata(tata)
        # marcheaza legaturile de rudenie (tata, mama)

        self.__lista_copii.append(copil)
        tata.add_lista_copii(copil)

    def stare_civila(self, data):
        # afiseaza starea civila a unei persoane la o data specificata

        data_specificata = datetime.strptime(data, "%d/%m/%Y")

        if data_specificata < datetime.strptime(self.__data_nasterii, "%d/%m/%Y"):
            print("\nPersoana nu exista la data specificata.")
            return

        # parcurgerea listei de "stari civile"
        iterator = 0
        for stari in self.__lista_stare_civila:
            data_stare_civila = datetime.strptime(stari[2], "%d/%m/%Y")
            if data_specificata < data_stare_civila:
                break
            else:
                iterator += 1

        if iterator == 0:
            print("\nNecasatorit/a.")
        else:
            if self.__lista_stare_civila[iterator-1][0] == "Casatorit/a":
                print("\nCasatorit/a cu {0} {1}".format(self.__lista_stare_civila[iterator-1][1].nume_persoana,
                                                    self.__lista_stare_civila[iterator-1][1].prenume_persoana))
            else:
                print("\nNecasatorit/a.")  # persoana era divortata la data specificata

    def afisare_descendenti(self):
     # metoda recursiva ce afiseaza descendentii unei persoane

        if not self.__lista_copii:
            return
        for copil in self.__lista_copii:
            print("{0} {1}, copilul lui {2} {3}\n".format(copil.nume_persoana,
                                                          copil.prenume_persoana,
                                                          self.nume_persoana, self.prenume_persoana))
            copil.afisare_descendenti()

    def grad_rudenie(self, persoana):

        ruda = None  # presupunem ca persoanele nu sunt rude

        tata = persoana.get_tata()
        mama = persoana.get_mama()
        lista_copii = persoana.get_lista_copii()
        partener_self = self.__sot_sotie
        partener_persoana = persoana.get_sot_sotie()

        if partener_self is not None:
            partener_self_copii = partener_self.get_lista_copii()
        else:
            partener_self_copii = []
        if partener_persoana is not None:
            partener_persoana_copii = partener_persoana.get_lista_copii()
        else:
            partener_persoana_copii = []

        if persoana in self.__lista_copii:
            # verifica daca a doua persoana este copilul primei persoane
            print("{0} {1} este parintele lui {2} {3}\n".format(self.nume_persoana, self.prenume_persoana,
                                                                persoana.nume_persoana,
                                                                persoana.prenume_persoana))
            ruda = True

        if self in lista_copii:
            # verifica daca prima persoana este copilul primei persoane
            print("{0} {1} este copilul lui {2} {3}\n".format(self.nume_persoana, self.prenume_persoana,
                                                              persoana.nume_persoana,
                                                              persoana.prenume_persoana))
            ruda = True

        if tata is not None and mama is not None and self.__tata is not None and self.__mama is not None:

            if self.__tata == tata and self.__mama == mama:
                # persoanele au aceiasi parinti
                print("{0} {1} este fratele/sora lui {2} {3}\n".format(self.nume_persoana, self.prenume_persoana,
                                                                       persoana.nume_persoana,
                                                                       persoana.prenume_persoana))
                ruda = True

            if self.__mama == mama and self.__tata != tata:
                # persoanele nu au acelasi tata dar au aceiasi mama
                print("{0} {1} este frate/sora vitreg/vitrega cu {2} {3}\n".format(self.nume_persoana, self.prenume_persoana,
                                                                                   persoana.nume_persoana,
                                                                                   persoana.prenume_persoana))
                ruda = True

            if self.__mama != mama and self.__tata == tata:
                # persoanele nu au aceiasi mama dar au acelasi tata
                print("{0} {1} este frate/sora vitreg/vitrega cu {2} {3}\n".format(self.nume_persoana, self.prenume_persoana,
                                                                                   persoana.nume_persoana,
                                                                                   persoana.prenume_persoana))
                ruda = True

            # se considera doar verisorii de gradul I

            if mama.get_mama() is not None and mama.get_tata() is not None and self.__mama.get_mama() is not None and self.__mama.get_tata() is not None:
                # mamele persoanelor sunt surori
                if self.__mama.get_mama() == mama.get_mama() and self.__mama.get_tata() == mama.get_tata() and self.__mama != mama:

                    print("{0} {1} este varul/versioara lui {2} {3}\n".format(self.nume_persoana, self.prenume_persoana,
                                                                              persoana.nume_persoana,
                                                                              persoana.prenume_persoana))
                    ruda = True

            if tata.get_mama() is not None and tata.get_tata() is not None and self.__mama.get_mama() is not None and self.__mama.get_tata() is not None:
                # mama primei persoane este sora cu tatal celei de-a doua persoane
                if self.__mama.get_mama() == tata.get_mama() and self.__mama.get_tata() == tata.get_tata():
                    print("{0} {1} este varul/versioara lui {2} {3}\n".format(self.nume_persoana, self.prenume_persoana,
                                                                              persoana.nume_persoana,
                                                                              persoana.prenume_persoana))
                    ruda = True

            if mama.get_mama() is not None and mama.get_tata() is not None and self.__tata.get_mama() is not None and self.__tata.get_tata() is not None:
                # tatal primei persoane este frate cu mama celei de-a doua persoane
                if self.__tata.get_mama() == mama.get_mama() and self.__tata.get_tata() == mama.get_tata():
                    print("{0} {1} este varul/versioara lui {2} {3}\n".format(self.nume_persoana, self.prenume_persoana,
                                                                              persoana.nume_persoana,
                                                                              persoana.prenume_persoana))
                    ruda = True

            if tata.get_mama() is not None and tata.get_tata() is not None and self.__tata.get_mama() is not None and self.__tata.get_tata() is not None:
                # tatii persoanelor sunt frati
                if self.__tata.get_mama() == tata.get_mama() and self.__tata.get_tata() == tata.get_tata() and self.__tata != tata:
                    print("{0} {1} este varul/versioara lui {2} {3}\n".format(self.nume_persoana, self.prenume_persoana,
                                                                              persoana.nume_persoana,
                                                                              persoana.prenume_persoana))
                    ruda = True

            if self.__tata.get_mama() is not None and self.__tata.get_tata() is not None:
                # cea de-a doua persoana este frate/sora cu tatal primei persoane
                if self.__tata.get_mama() == mama and self.__tata.get_tata() == tata:
                    print("{0} {1} este nepotul/nepoata lui {2} {3}\n".format(self.nume_persoana, self.prenume_persoana,
                                                                             persoana.nume_persoana,
                                                                             persoana.prenume_persoana))
                    ruda = True

            if self.__mama.get_mama() is not None and self.__mama.get_tata() is not None:
                # cea de-a doua persoana este frate/sora cu mama primei persoane
                if self.__mama.get_mama() == mama and self.__mama.get_tata() == tata:
                    print("{0} {1} este nepotul/nepoata lui {2} {3}\n".format(self.nume_persoana, self.prenume_persoana,
                                                                             persoana.nume_persoana,
                                                                             persoana.prenume_persoana))
                    ruda = True

        if tata in self.__lista_copii or mama in self.__lista_copii:
            # tatal sau mama celei de-a doua persoane este copilul primei persoane
            print("{0} {1} este bunicul/bunica lui {2} {3}\n".format(self.nume_persoana, self.prenume_persoana,
                                                                     persoana.nume_persoana,
                                                                     persoana.prenume_persoana))
            ruda = True

        if self.__tata in lista_copii or self.__mama in lista_copii:
            # tatal sau mama primei persoane este copilul celei de-a doua persoane
            print("{0} {1} este nepotul/nepoata lui {2} {3}\n".format(self.nume_persoana, self.prenume_persoana,
                                                                      persoana.nume_persoana,
                                                                      persoana.prenume_persoana))
            ruda = True

        if persoana in partener_self_copii and persoana not in self.__lista_copii:
            # cea de-a doua persoana este copilul sotului/sotiei primei persoane
            print("{0} {1} este tatal/mama vitreg/vitrega al lui/a lui {2} {3}\n".format(self.nume_persoana, self.prenume_persoana,
                                                                                         persoana.nume_persoana,
                                                                                         persoana.prenume_persoana))
            ruda = True

        if self in partener_persoana_copii and self not in lista_copii:
            # prima persoana este copilul sotului/sotiei celei de-a doua persoane persoane
            print("{0} {1} este tatal/mama vitreg/vitrega al lui/a lui {2} {3}\n".format(persoana.nume_persoana,
                                                                                         persoana.prenume_persoana,
                                                                                         self.nume_persoana, self.prenume_persoana))
            ruda = True

        if partener_persoana is not None and self.__tata is not None and self.__mama is not None:
            if partener_persoana.get_tata() is not None and partener_persoana.get_mama() is not None:
                # sotul/sotia celei de-a doua persoane este frate/sora cu prima persoana
                if partener_persoana.get_tata() == self.__tata and partener_persoana.get_mama() == self.__mama:
                    print("{0} {1} este cumnatul/cumnata lui {2} {3}\n".format(self.nume_persoana,
                                                                               self.prenume_persoana,
                                                                               persoana.nume_persoana,
                                                                               persoana.prenume_persoana))
                    ruda = True

        if partener_self is not None and tata is not None and mama is not None:
            if partener_self.get_tata() is not None and partener_self.get_mama() is not None:
                # sotul/sotia primei persoane este frate/sora cu cea de-a doua persoana
                if partener_self.get_tata() == tata and partener_self.get_mama() == mama:
                    print("{0} {1} este cumnatul/cumnata lui {2} {3}\n".format(self.nume_persoana,
                                                                               self.prenume_persoana,
                                                                               persoana.nume_persoana,
                                                                               persoana.prenume_persoana))
                    ruda = True


        if ruda is None:
            # anterior nu a fost gasit niciun grad de rudenie
            print("Nu exista niciun grad de rudenie intre {0} {1} si {2} {3}\n".format(persoana.nume_persoana,
                                                                                       persoana.prenume_persoana,
                                                                                       self.nume_persoana, self.prenume_persoana))
