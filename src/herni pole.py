class HerniPole:
    spike_list = []
    # pozdeji nebude podminka asi ani potreba
    if len(spike_list) != 0:
        Game.spikes = [spike_list[0:6], spike_list[6:13], spike_list[13:19], spike_list[19:23]]

    def funkc_po_spust(self):
        for _ in range(24):
            self.spike_list.append({"kameny": [], "barva": None})

    def nahodne_rozmisteni(self):  # provizorne
        barva_hrace1 = "bila"
        barva_hrace2 = "cerna"

        for i in range(len(self.spike_list)):
            if i % 2 == 0 and i != 4 and i != 8 and i != 2:
                self.spike_list[i]["kameny"].append("x")
                self.spike_list[i]["barva"] = barva_hrace1
            if i == 2:
                self.spike_list[i]["kameny"].append("x")
                self.spike_list[i]["barva"] = barva_hrace2

    def provest_presun_pro_hrace(self, id_hrace, hod_kostkou, barva_hrace1, barva_hrace2):

        # vypis kamenu (spiku), ktere jsou k dispozici
        podezrele_dostupne_tahy = []  # index spiku .... S1....S2....S3....S4
        for i in range(len(self.spike_list)):
            if len(self.spike_list[i]["kameny"]) > 0 and self.spike_list[i][
                "barva"] == barva_hrace1:  # pokud v spiku je nejaky kamen a ma barvu hrace zapise se do moznych tahu
                podezrele_dostupne_tahy.append(i)  # index dostupneho kamene ve spiku self.spike_list[i]

                # dostupne_tahy
                # kontrola spiku v pripade kdyby chtel hrac posunout sutr (aby na tomto spiku nebyl jiny hrac.... pokud by byl a mel by 1 sutr pak ho muze vyhodit)

        print(self.spike_list)

        tahy = []  # dvojce .... (Sx, Sy)

        if id_hrace == 1:
            for i in podezrele_dostupne_tahy:
                if i + hod_kostkou < 24:

                    # kontrola poctu kamenu mozneho tahu.... pripsani na seznam dostupnych tahu
                    if len(self.spike_list[i + hod_kostkou]["kameny"]) == 0:
                        # Sx , Sy
                        tahy.append((i, i + hod_kostkou))

                    if len(self.spike_list[i + hod_kostkou]["kameny"]) == 1 and self.spike_list[i + hod_kostkou][
                        "barva"] == barva_hrace2:
                        tahy.append((i, i + hod_kostkou))

                    if len(self.spike_list[i + hod_kostkou]["kameny"]) > 0 and len(
                            self.spike_list[i + hod_kostkou]["kameny"]) < 5 and self.spike_list[i + hod_kostkou][
                        "barva"] == barva_hrace1:
                        tahy.append((i, i + hod_kostkou))

        else:  # id_hrace == 2 , id_hrace == 3
            for i in podezrele_dostupne_tahy:
                if i - hod_kostkou >= 0:

                    # kontrola poctu kamenu mozneho tahu.... pripsani na seznam dostupnych tahu
                    if len(self.spike_list[i - hod_kostkou]["kameny"]) == 0:
                        # Sx , Sy
                        tahy.append((i, i - hod_kostkou))

                    if len(self.spike_list[i - hod_kostkou]["kameny"]) == 1 and self.spike_list[i - hod_kostkou][
                        "barva"] == barva_hrace2:
                        tahy.append((i, i - hod_kostkou))

                    if len(self.spike_list[i - hod_kostkou]["kameny"]) > 0 and len(
                            self.spike_list[i - hod_kostkou]["kameny"]) < 5 and self.spike_list[i - hod_kostkou][
                        "barva"] == barva_hrace1:
                        tahy.append((i, i - hod_kostkou))

        # hracova volba tahu

        print(f"Hrac: {id_hrace}\nHodil kostkou: {hod_kostkou}")
        print(f"K posunuti jsou nasledujici kombinace:")

        kombinace = 1  # index zacina od 1 bude treba ho zmensit pokud se s nim bude pracovat jako s prvnim prvkem v seznamu
        platne_kombinace = []
        for sx, sy in tahy:
            print(f"({kombinace}) Kamen z S{sx} na S{sy}")
            platne_kombinace.append(kombinace)
            kombinace += 1

        # vyber

        if id_hrace == 1:
            while True:
                volba = input("Pro posunuti zadejte cislo v zavorkach: ")

                spiky_k_presunuti = [tahy[int(volba) - 1][0], tahy[int(volba) - 1][1]]

                if volba.isnumeric() == True:
                    volba = int(volba)
                    if volba in platne_kombinace:
                        temp = volba - 1  # zmensen o 1 aby se s nim dalo pocitat jako s opravdovym prvkem v seznamu.... len(x) != indexy x.... len(x) + 1 == indexy x

                        print(f"Vybral jste kombinaci {volba} a posouvate S{tahy[temp][0]} na S{tahy[temp][1]}")
                        break
                    else:
                        print("Vase volba se nenachazi v moznostech")
                else:
                    print("zadejte cislo")

        else:  # id_hrace == 2 , id_hrace == 3
            while True:
                volba = input("Pro posunuti zadejte cislo v zavorkach: ")

                spiky_k_presunuti = [tahy[int(volba) - 1][0], tahy[int(volba) - 1][1]]

                if volba.isnumeric() == True:
                    volba = int(volba)
                    if volba in platne_kombinace:
                        temp = volba - 1  # zmensen o 1 aby se s nim dalo pocitat jako s opravdovym prvkem v seznamu.... len(x) != indexy x.... len(x) + 1 == indexy x

                        print(f"Vybral jste kombinaci {volba} a posouvate S{tahy[temp][1]} na S{tahy[temp][0]}")
                        break
                    else:
                        print("Vase volba se nenachazi v moznostech")
                else:
                    print("zadejte cislo")

        ########
        # presunuti

        # presunuti na prazdny spike .... na puvodnim spiku zbyvaji kameny

        if len(self.spike_list[spiky_k_presunuti[1]]["kameny"]) == 0 and len(
                self.spike_list[spiky_k_presunuti[0]]["kameny"]) > 1:
            self.spike_list[spiky_k_presunuti[0]]["kameny"].remove("x")  # kamen se presouva, smazani z puvodniho spiku
            self.spike_list[spiky_k_presunuti[1]]["kameny"].append("x")  # kamen se pridal na novy spike
            self.spike_list[spiky_k_presunuti[1]]["barva"] = barva_hrace1  # barva se pridala na novy spike

        # presunuti na prazdny spike .... na puvodnim spiku nezbyvaji kameny

        if len(self.spike_list[spiky_k_presunuti[1]]["kameny"]) == 0 and len(
                self.spike_list[spiky_k_presunuti[0]]["kameny"]) == 1:
            self.spike_list[spiky_k_presunuti[0]]["kameny"].remove("x")  # kamen se presouva, smazani z puvodniho spiku
            self.spike_list[spiky_k_presunuti[0]]["barva"] = None  # barva puvodniho spiku se zmeni na None
            self.spike_list[spiky_k_presunuti[1]]["kameny"].append("x")  # kamen se pridal na novy spike
            self.spike_list[spiky_k_presunuti[1]]["barva"] = barva_hrace1  # barva se pridala na novy spike

        # presunuti na spike s jednim kamenem jine barvy .... na puvodnim spiku zbyvaji kameny

        if len(self.spike_list[spiky_k_presunuti[1]]["kameny"]) == 1 and len(
                self.spike_list[spiky_k_presunuti[0]]["kameny"]) > 1:
            self.spike_list[spiky_k_presunuti[0]]["kameny"].remove("x")  # kamen se presouva, smazani z puvodniho spiku
            self.spike_list[spiky_k_presunuti[1]]["barva"] = barva_hrace1

        # presunuti na spike s jednim kamenem jine barvy .... na puvodnim spiku nezbyvaji kameny

        if len(self.spike_list[spiky_k_presunuti[1]]["kameny"]) == 1 and len(
                self.spike_list[spiky_k_presunuti[0]]["kameny"]) == 1:
            self.spike_list[spiky_k_presunuti[0]]["kameny"].remove("x")  # kamen se presouva, smazani z puvodniho spiku
            self.spike_list[spiky_k_presunuti[0]]["barva"] = None  # barva puvodniho spiku se zmeni na None
            self.spike_list[spiky_k_presunuti[1]]["barva"] = barva_hrace1  # barva se prida na cilovy spike

        print(self.spike_list)

    def presun(self, id_hrace, hod_kostkou, barva_hrace1,
               barva_hrace2):  # id hrace pro smer, hod_kostkou pro dostupne tahy
        # hrac vs hrac (1,2) , hrac vs ai (1,3) .... (x,y) = (barva_hracex, barva_hracey)

        barva_hrace1 = "bila"
        barva_hrace2 = "cerna"
        barva_hrace3 = "cerna"

        # hraje hrac 1                                                  dulezite poradi
        if id_hrace == 1:  # #
            self.provest_presun_pro_hrace(id_hrace, hod_kostkou, barva_hrace1, barva_hrace2)

        # hraje hrac 2
        if id_hrace == 2:  # #
            self.provest_presun_pro_hrace(id_hrace, hod_kostkou, barva_hrace2, barva_hrace1)

        # hraje ai , pokud je hra s ai automaticky hraje jen hrac s id1 a ai
        if id_hrace == 3:

            # vypis kamenu (spiku), ktere jsou k dispozici
            podezrele_dostupne_tahy = []  # index spiku .... S1....S2....S3....S4
            for i in range(len(self.spike_list)):
                if len(self.spike_list[i]["kameny"]) > 0 and self.spike_list[i][
                    "barva"] == barva_hrace3:  # pokud v spiku je nejaky kamen a ma barvu hrace zapise se do moznych tahu
                    podezrele_dostupne_tahy.append(i)  # index dostupneho kamene ve spiku self.spike_list[i]

                    # dostupne_tahy
                    # kontrola spiku v pripade kdyby chtel hrac posunout sutr (aby na tomto spiku nebyl jiny hrac.... pokud by byl a mel by 1 sutr pak ho muze vyhodit)

            print(self.spike_list)

            tahy = []  # dvojce .... (Sx, Sy)
            for i in podezrele_dostupne_tahy:
                if i - hod_kostkou >= 0:

                    # kontrola poctu kamenu mozneho tahu.... pripsani na seznam dostupnych tahu
                    if len(self.spike_list[i - hod_kostkou]["kameny"]) == 0:
                        # Sx , Sy
                        tahy.append((i, i - hod_kostkou))

                    if len(self.spike_list[i - hod_kostkou]["kameny"]) == 1 and self.spike_list[i - hod_kostkou][
                        "barva"] == barva_hrace1:
                        tahy.append((i, i - hod_kostkou))

                    if len(self.spike_list[i - hod_kostkou]["kameny"]) > 0 and len(
                            self.spike_list[i - hod_kostkou]["kameny"]) < 5 and self.spike_list[i - hod_kostkou][
                        "barva"] == barva_hrace3:
                        tahy.append((i, i - hod_kostkou))

            #######################################################################################################################################################################################
            # ai vytvoreni voleb

            print(f"Hrac: {id_hrace}\nHodil kostkou: {hod_kostkou}")

            kombinace = 1  # index zacina od 1 bude treba ho zmensit pokud se s nim bude pracovat jako s prvnim prvkem v seznamu
            platne_kombinace = []
            for sx, sy in tahy:
                print(f"({kombinace}) Kamen z S{sx} na S{sy}")
                platne_kombinace.append(kombinace)
                kombinace += 1

            # ai vyber vhodneho tahu
            # ai se podiva zda za nemuze vyhodit nekoho v okoli....
            # ai uprednostnuje:
            #                   1) ai se blizi cili
            #                   2) vyhozeni hrace, ktery je za pulkou (bliz k ai zakladne)
            #                   3) nenechavat kameny o samote (hrozi vyhozeni)

            for sx, sy in tahy:
                temp_dvojce = (sx, sy)  # ziskani
                print(temp_dvojce)
                if (sx, sy) in tahy:  # sx = aktualni pozice ,  sy = planovana pozice

                    if sy < 6:
                        volba = tahy.index((sx, sy))  # 1) priorita 1 blizi se k cili
                        break

                    elif sy < 12 and self.spike_list[sy]["barva"] != barva_hrace3:  # 2) priorita 2
                        volba = tahy.index((sx, sy))
                        break

                    elif sy < 12 and len(self.spike_list[sy]["kameny"]) == 1:  # 3) priorita 3
                        volba = tahy.index((sx, sy))
                        break

                    else:
                        volba = random.randint(1, len(platne_kombinace))  # 4) priorita 4 .... normalni

            #########################################################################################################################################################################################

            # uprava volby

            spiky_k_presunuti = [tahy[volba - 1][0], tahy[volba - 1][1]]

            if volba in platne_kombinace:
                temp = volba - 1  # zmensen o 1 aby se s nim dalo pocitat jako s opravdovym prvkem v seznamu.... len(x) != indexy x.... len(x) + 1 == indexy x

                print(f"AI posouva kamen z S{tahy[temp][0]} na S{tahy[temp][1]}")

            # presunuti na prazdny spike .... na puvodnim spiku zbyvaji kameny

            if len(self.spike_list[spiky_k_presunuti[1]]["kameny"]) == 0 and len(
                    self.spike_list[spiky_k_presunuti[0]]["kameny"]) > 1:
                self.spike_list[spiky_k_presunuti[0]]["kameny"].remove(
                    "x")  # kamen se presouva, smazani z puvodniho spiku
                self.spike_list[spiky_k_presunuti[1]]["kameny"].append("x")  # kamen se pridal na novy spike
                self.spike_list[spiky_k_presunuti[1]]["barva"] = barva_hrace3  # barva se pridala na novy spike

            # presunuti na prazdny spike .... na puvodnim spiku nezbyvaji kameny

            if len(self.spike_list[spiky_k_presunuti[1]]["kameny"]) == 0 and len(
                    self.spike_list[spiky_k_presunuti[0]]["kameny"]) == 1:
                self.spike_list[spiky_k_presunuti[0]]["kameny"].remove(
                    "x")  # kamen se presouva, smazani z puvodniho spiku
                self.spike_list[spiky_k_presunuti[0]]["barva"] = None  # barva puvodniho spiku se zmeni na None
                self.spike_list[spiky_k_presunuti[1]]["kameny"].append("x")  # kamen se pridal na novy spike
                self.spike_list[spiky_k_presunuti[1]]["barva"] = barva_hrace3  # barva se pridala na novy spike

            # presunuti na spike s jednim kamenem jine barvy .... na puvodnim spiku zbyvaji kameny

            if len(self.spike_list[spiky_k_presunuti[1]]["kameny"]) == 1 and len(
                    self.spike_list[spiky_k_presunuti[0]]["kameny"]) > 1:
                self.spike_list[spiky_k_presunuti[0]]["kameny"].remove(
                    "x")  # kamen se presouva, smazani z puvodniho spiku
                self.spike_list[spiky_k_presunuti[1]]["barva"] = barva_hrace3

            # presunuti na spike s jednim kamenem jine barvy .... na puvodnim spiku nezbyvaji kameny

            if len(self.spike_list[spiky_k_presunuti[1]]["kameny"]) == 1 and len(
                    self.spike_list[spiky_k_presunuti[0]]["kameny"]) == 1:
                self.spike_list[spiky_k_presunuti[0]]["kameny"].remove(
                    "x")  # kamen se presouva, smazani z puvodniho spiku
                self.spike_list[spiky_k_presunuti[0]]["barva"] = None  # barva puvodniho spiku se zmeni na None
                self.spike_list[spiky_k_presunuti[1]]["barva"] = barva_hrace3  # barva se prida na cilovy spike

            print(self.spike_list)

        # hra = HerniPole()


# hra.funkc_po_spust()
# hra.nahodne_rozmisteni()
#            - 3 - ai, 1 - hrac, 2 - hrac2
#           v
# hra.presun(3, 2, "cerna", "bila")


# kamen = Kamen(0)
# print(kamen.barva)
# kamen.vypis()

## popisy událostí co by se stalo
# Inicializace herní desky
board = [[0] * 24 for _ in range(2)]


# Funkce pro vhození kamene do hry
def enter_piece(player, point):
    board[player][point] += 1
    print(f"Hráč {player} vhozen kámen na pozici {point}")


# Funkce pro vyhození kamene z hry
def remove_piece(player, point):
    board[player][point] -= 1
    print(f"Hráč {player} vyhodil kámen z pozice {point}")


# Funkce pro opuštění hry
def leave_game(player):
    print(f"Hráč {player} opustil hru")


# Funkce pro zablokování hráče, který nemůže hrát
def block_player(player):
    print(f"Hráč {player} nemůže hrát")


# Příklady použití funkcí
enter_piece(0, 5)  # Hráč 0 vhozen kámen na pozici 5
remove_piece(1, 10)  # Hráč 1 vyhodil kámen z pozice 10
leave_game(0)  # Hráč 0 opustil hru
block_player(1)  # Hráč 1 nemůže hrát
