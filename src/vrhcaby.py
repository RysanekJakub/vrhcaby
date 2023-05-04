import json
import os
import random
import platform

# zajistuje barvy textu
os.system("")

class style:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    LIGHT_BLUE = '\033[38;2;0;255;243m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

    # vycisti konzoli
    @staticmethod
    def clear() -> object:
        # pro zajisteni kompatibility s vice OS
        if platform.system() == "Windows":
            os.system("cls")
        elif platform.system() == "Linux" or platform.system() == "Darwin":
            os.system("clear")

class Game:
    
    def __init__(self, gameboard, pozice, player1, player2) -> None:
        # herni pole
        self._gameboard = gameboard
        # dvojkostka
        self._doubledice = []
        self._bar = ...
        self._stone = pozice
        self._turn = 0
        self._player_turn = player1     # defaultni hodnota
        self._player1 = player1
        self._player1_barva = ""
        self._player2 = player2
        self._player2_barva = ""
        self._last_command = ""
        self._game_mod = ""              # game_mod se nastavi v gamesetup
        
        # TENHLE SEZNAM JE TU JEN DOCASNE
        # BUDE VYMENEN VE CHVILI KDY BUDE DOKONCENA IMPLEMENTACE TRIDY SPIKU
        # seznam necham takto rozbaleny kvuli co mozna nejlepsi citelnosti
        self._spikes = [[    
                [1,1,1],
                ["O"],
                ["O", "O"],
                ["O", "O", "O"],
                ["O"],
                []
            ],
            [    
                [1,1,1],
                ["O"],
                ["O"],
                ["O", "O", "O", "O", "O", "O", "O"],
                ["O"],
                ["O", "O"]
            ],
            [    
                [1,1,1],
                ["O"],
                [1,1,1,1,1],
                ["O", "O"],
                ["O"],
                [1,1]
            ],
            [    
                [1,1],
                ["O"],
                [],
                ["O"],
                [],
                [1,1]
            ],
        ]

    @property
    def doubledice(self):
        return self._doubledice

    @doubledice.setter
    def doubledice(self, value):
        self._doubledice = value
    
    @property
    def gameboard(self):
        return self._gameboard
    
    @property
    def spikes(self):
        return self._spikes
    
    @property
    def last_command(self):
        return self._last_command
    
    @last_command.setter
    def last_command(self, value):
        self._last_command = value

    @property
    def turn(self):
        return self._turn
    
    @turn.setter
    def turn(self, value):
        self._turn = value

    @property
    def player_turn(self):
        return self._player_turn
    
    @player_turn.setter
    def player_turn(self, value):
        self._player_turn = value
    
    @property
    def player1(self):
        return self._player1
    
    @property
    def player2(self):
        return self._player2


    def next_turn(self, p_turn:int) -> int:
        self.turn += 1
        if p_turn == self.player1:
            self.player_turn = self.player2
        else:
            self.player_turn = self.player1


    @staticmethod
    def throw_dice(dice:list) -> list:
        dice.clear()
        hod1, hod2 = random.randint(1, 6), random.randint(1, 6)
        # kontrola hozenych hodnot
        if hod1 != hod2:
            dice.append(str(hod1))
            dice.append(str(hod2))
            return dice
        # pokud se cisla rovnaji, vrati se 4x
        else:
            for _ in range(4):
                dice.append(str(hod1))
            return dice
    

    def sektor_spiku_vrchni(self, sektor:int, spikes_lists:list) -> list:
        rows = []   # zde jsou vsechny radky pro vybrany sektor po formatovani
        for i in range(7):  # defaultni vyska radku, pozdeji jeste bude potreba upravit pro pripady, kdy se na spike dostane vice nez 7 kamenu
            row = []    # seznamy radku po jednom
            for spike in spikes_lists[sektor]:  # zde se ze seznamu sektoru vybere pozadovany sektor, ktery obsahuje seznamy vsech spiku
                default_mezery = " "*(6-i)  # dopocet mezer uvnitr spiku kvuli formatovani
                vypln = " "*i   # dopocet mezer okolo spiku kvuli formatovani
                if i < len(spike):  # pokud je *i* mensi nez delka seznamu spiku, kterym se zrovna prochazi, znamena to, ze tam bude kamen
                    row.append(f"{vypln}\{default_mezery}O{default_mezery}/{vypln}")    # cely radek se po spojeni zapise do seznamu *row*
                else:
                    row.append(f"{vypln}\{default_mezery} {default_mezery}/{vypln}")    # pokud je *i* vetsi nez delka seznamu spiku, znamena to, ze uz tam neni dalsi kamen a tak se zapise mezera
            rows.append(row)
        return rows


    def sektor_spiku_spodni(self, sektor:int, spikes_lists:list) -> list:
        # postup pri vykresleni kamenu je trochu komplikovanejsi kvuli tomu, ze se tentokrat musi kameny vypisovat odspoda nahoru
        # udelal jsem to tak, ze se vezme list kazdeho spiku a podle poctu kamenu (delky seznamu spiku) se zapisou mezery pred kameny
        # vypada-li seznam spiku takto: [1,1,1]
        # tak po teto uprave bude vypadat takto: [" "," "," "," ", 1,1,1]
        nove_listy = []
        for sektor_list in spikes_lists[sektor]:    # loop, ktery vytahne seznamy jednotlivych spiku
            missing = [" " for _ in range(7-len(sektor_list))]  # zde se zapisuji mezery podle poctu kamenu na spiku do noveho seznamu
            nove_listy.append(missing+sektor_list)  # spojeni seznamu *missing* s mezerami a jiz existujicim seznamem spiku

        # zde uz je postup skoro stejny jako u funkce *sektor_spiku_vrchni*
        rows = []
        for i in range(7):
            row = []
            for spike in nove_listy:
                default_mezery = " "*i
                vypln = " "*(6-i)
                if spike[i] != " ": # pokud se i nerovna mezere, zapise se kamen
                    row.append(f"{vypln}/{default_mezery}O{default_mezery}\{vypln}")
                else:
                    row.append(f"{vypln}/{default_mezery} {default_mezery}\{vypln}")

            rows.append(row)
        return rows
    

    def gameboard_final(self, values:list, spikes:list, command:str, cur_turn: int, p_turn: str) -> str:
        # dopocet chybejicich mezer kvuli formatovani
        # asi by to slo elegantneji... treba pozdeji :)
        if len(values) == 2:
            spaces = 166*" "
        elif len(values) == 4:
            spaces = 160*" "
        else:
            spaces = 170*" "
        
        # tvorba cislovani spiku
        spike_row1 = ([str(_) for _ in range(1,7)], [str(_) for _ in range(7,10)], [str(_) for _ in range(10,13)])
        spike_row2 = ([str(_) for _ in range(13,19)], [str(_) for _ in range(19, 25)])

        # zatim je v tom bordel, pochopitelne to neni ani zdaleka finalni
        gameboard = f"""
 ____________________________________________________________________________________________________________________________________________________________________________________________
|                                                                                          {style.BLUE}VRHCABY{style.RESET}                                                                                          |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Poslední příkaz: {command}
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Kolo: {cur_turn}                                                                                                                                                                               
| Hraje: {p_turn}                                                                                                                                                                             
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Hozené hodnoty: {style.LIGHT_BLUE}{"  ".join(values)}{style.RESET}{spaces}| 
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|{style.RED}        {"              ".join(spike_row1[0])}                   {"              ".join(spike_row1[1])}             {"             ".join(spike_row1[2])}{style.RESET}        |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| {"".join(self.sektor_spiku_vrchni(0,self.spikes)[0])} | | {"".join(self.sektor_spiku_vrchni(1,self.spikes)[0])} |
| {"".join(self.sektor_spiku_vrchni(0,self.spikes)[1])} | | {"".join(self.sektor_spiku_vrchni(1,self.spikes)[1])} |
| {"".join(self.sektor_spiku_vrchni(0,self.spikes)[2])} | | {"".join(self.sektor_spiku_vrchni(1,self.spikes)[2])} |
| {"".join(self.sektor_spiku_vrchni(0,self.spikes)[3])} | | {"".join(self.sektor_spiku_vrchni(1,self.spikes)[3])} |
| {"".join(self.sektor_spiku_vrchni(0,self.spikes)[4])} | | {"".join(self.sektor_spiku_vrchni(1,self.spikes)[4])} |
| {"".join(self.sektor_spiku_vrchni(0,self.spikes)[5])} | | {"".join(self.sektor_spiku_vrchni(1,self.spikes)[5])} |
| {"".join(self.sektor_spiku_vrchni(0,self.spikes)[6])} | | {"".join(self.sektor_spiku_vrchni(1,self.spikes)[6])} |
|{" "*92}| |{" "*92}|
|{" "*92}| |{" "*92}|
|{" "*92}| |{" "*92}|
|{" "*92}| |{" "*92}|
|{" "*92}| |{" "*92}|
|{" "*92}| |{" "*92}|
| {"".join(self.sektor_spiku_spodni(2,self.spikes)[0])} | | {"".join(self.sektor_spiku_spodni(3,self.spikes)[0])} |
| {"".join(self.sektor_spiku_spodni(2,self.spikes)[1])} | | {"".join(self.sektor_spiku_spodni(3,self.spikes)[1])} |
| {"".join(self.sektor_spiku_spodni(2,self.spikes)[2])} | | {"".join(self.sektor_spiku_spodni(3,self.spikes)[2])} |
| {"".join(self.sektor_spiku_spodni(2,self.spikes)[3])} | | {"".join(self.sektor_spiku_spodni(3,self.spikes)[3])} |
| {"".join(self.sektor_spiku_spodni(2,self.spikes)[4])} | | {"".join(self.sektor_spiku_spodni(3,self.spikes)[4])} |
| {"".join(self.sektor_spiku_spodni(2,self.spikes)[5])} | | {"".join(self.sektor_spiku_spodni(3,self.spikes)[5])} |
| {"".join(self.sektor_spiku_spodni(2,self.spikes)[6])} | | {"".join(self.sektor_spiku_spodni(3,self.spikes)[6])} |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|{style.RED}       {"             ".join(spike_row2[0])}                   {"             ".join(spike_row2[1])}{style.WHITE}       |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|___________________________________________________________________________________________________________________________________________________________________________________________|
"""
        # vrati samotny gameboard s doplnenymi hodnotami
        return gameboard
    

    def command_detection(self, command:str, cfg:str, p_turn:str) -> str:
        command = command.lower()
        with open(cfg, 'r') as config_file:
            all_commands = json.load(config_file)['commands']
        
        if command in all_commands:
            if command == "presun":
                command = f"{style.CYAN}Prikaz \'{command}\' zatím nemá zatím implementovanou funkci{style.RESET}"
            elif command == "hod":
                self.throw_dice(self.doubledice)
            command = f"{style.GREEN}{command}{style.RESET}"
            self.next_turn(p_turn)
        else:
            command = f"{style.RED}Prikaz {command} nenalezen{style.RESET}"
        self.last_command = command

class Kamen:
    def __init__(self, barva):
        self.barva = barva
        self.pamet = []  # seznam uspořádaných dvojic (přidávání pomocí appendu)
        self.id = 0

    def vypis(self):  # výpis možná bude řešit jiná třída
        if self.barva == 0:
            print("kamen je bily")
        else:
            print("kamen je cerny")
    
class HerniPole:
    
    spike_list = []
    
    def funkc_po_spust(self):
        for _ in range(24):
            self.spike_list.append({"kameny": [], "barva": None})
            
    def nahodne_rozmisteni(self): # provizorne
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
        podezrele_dostupne_tahy = []                                                     # index spiku .... S1....S2....S3....S4
        for i in range(len(self.spike_list)):
            if len(self.spike_list[i]["kameny"]) > 0 and self.spike_list[i]["barva"] == barva_hrace1:    # pokud v spiku je nejaky kamen a ma barvu hrace zapise se do moznych tahu
                podezrele_dostupne_tahy.append(i)                                                        # index dostupneho kamene ve spiku self.spike_list[i]
            
                # dostupne_tahy
                # kontrola spiku v pripade kdyby chtel hrac posunout sutr (aby na tomto spiku nebyl jiny hrac.... pokud by byl a mel by 1 sutr pak ho muze vyhodit)
            
        print(self.spike_list)
            
        tahy = [] # dvojce .... (Sx, Sy)
        
        if id_hrace == 1:
            for i in podezrele_dostupne_tahy:
                if i+hod_kostkou < 24:
                    
                    # kontrola poctu kamenu mozneho tahu.... pripsani na seznam dostupnych tahu
                    if len(self.spike_list[i+hod_kostkou]["kameny"]) == 0:
                                        # Sx , Sy
                        tahy.append((i,i+hod_kostkou))
                    
                    
                    if len(self.spike_list[i+hod_kostkou]["kameny"]) == 1 and self.spike_list[i+hod_kostkou]["barva"] == barva_hrace2:
                        tahy.append((i,i+hod_kostkou))
                    
                    if len(self.spike_list[i+hod_kostkou]["kameny"]) > 0 and len(self.spike_list[i+hod_kostkou]["kameny"]) < 5 and self.spike_list[i+hod_kostkou]["barva"] == barva_hrace1:
                        tahy.append((i,i+hod_kostkou))
        
        else: # id_hrace == 2 , id_hrace == 3
            for i in podezrele_dostupne_tahy:
                if i-hod_kostkou >= 0:
                    
                    # kontrola poctu kamenu mozneho tahu.... pripsani na seznam dostupnych tahu
                    if len(self.spike_list[i-hod_kostkou]["kameny"]) == 0:
                                    # Sx , Sy
                        tahy.append((i,i-hod_kostkou))
                    
                    
                    if len(self.spike_list[i-hod_kostkou]["kameny"]) == 1 and self.spike_list[i-hod_kostkou]["barva"] == barva_hrace2:
                        tahy.append((i,i-hod_kostkou))
                    
                    if len(self.spike_list[i-hod_kostkou]["kameny"]) > 0 and len(self.spike_list[i-hod_kostkou]["kameny"]) < 5 and self.spike_list[i-hod_kostkou]["barva"] == barva_hrace1:
                        tahy.append((i,i-hod_kostkou))
            
            
        # hracova volba tahu
            
        print(f"Hrac: {id_hrace}\nHodil kostkou: {hod_kostkou}")
        print(f"K posunuti jsou nasledujici kombinace:")
            
        kombinace = 1                                               # index zacina od 1 bude treba ho zmensit pokud se s nim bude pracovat jako s prvnim prvkem v seznamu
        platne_kombinace = []
        for sx, sy in tahy:
            print(f"({kombinace}) Kamen z S{sx} na S{sy}")
            platne_kombinace.append(kombinace)
            kombinace += 1
            
        # vyber
        
        if id_hrace == 1:    
            while True:
                volba = input("Pro posunuti zadejte cislo v zavorkach: ")
                
                spiky_k_presunuti = [tahy[int(volba)-1][0], tahy[int(volba)-1][1]]
                
                if volba.isnumeric() == True:
                    volba = int(volba)
                    if volba in platne_kombinace:
                        temp = volba-1              # zmensen o 1 aby se s nim dalo pocitat jako s opravdovym prvkem v seznamu.... len(x) != indexy x.... len(x) + 1 == indexy x
                    
                        print(f"Vybral jste kombinaci {volba} a posouvate S{tahy[temp][0]} na S{tahy[temp][1]}")
                        break
                    else:
                        print("Vase volba se nenachazi v moznostech")
                else:
                    print("zadejte cislo")
        
        else: # id_hrace == 2 , id_hrace == 3
            while True:
                volba = input("Pro posunuti zadejte cislo v zavorkach: ")
                
                spiky_k_presunuti = [tahy[int(volba)-1][0], tahy[int(volba)-1][1]]
                
                if volba.isnumeric() == True:
                    volba = int(volba)
                    if volba in platne_kombinace:
                        temp = volba-1              # zmensen o 1 aby se s nim dalo pocitat jako s opravdovym prvkem v seznamu.... len(x) != indexy x.... len(x) + 1 == indexy x
                        
                        print(f"Vybral jste kombinaci {volba} a posouvate S{tahy[temp][1]} na S{tahy[temp][0]}")
                        break
                    else:
                        print("Vase volba se nenachazi v moznostech")
                else:
                    print("zadejte cislo")
            
        ########
        # presunuti
            
        # presunuti na prazdny spike .... na puvodnim spiku zbyvaji kameny
            
        if len(self.spike_list[spiky_k_presunuti[1]]["kameny"]) == 0 and len(self.spike_list[spiky_k_presunuti[0]]["kameny"]) > 1:
            self.spike_list[spiky_k_presunuti[0]]["kameny"].remove("x")      # kamen se presouva, smazani z puvodniho spiku
            self.spike_list[spiky_k_presunuti[1]]["kameny"].append("x")      # kamen se pridal na novy spike
            self.spike_list[spiky_k_presunuti[1]]["barva"] = barva_hrace1    # barva se pridala na novy spike
            
        # presunuti na prazdny spike .... na puvodnim spiku nezbyvaji kameny
            
        if len(self.spike_list[spiky_k_presunuti[1]]["kameny"]) == 0 and len(self.spike_list[spiky_k_presunuti[0]]["kameny"]) == 1:
            self.spike_list[spiky_k_presunuti[0]]["kameny"].remove("x")      # kamen se presouva, smazani z puvodniho spiku
            self.spike_list[spiky_k_presunuti[0]]["barva"] = None            # barva puvodniho spiku se zmeni na None
            self.spike_list[spiky_k_presunuti[1]]["kameny"].append("x")      # kamen se pridal na novy spike
            self.spike_list[spiky_k_presunuti[1]]["barva"] = barva_hrace1    # barva se pridala na novy spike
                
        # presunuti na spike s jednim kamenem jine barvy .... na puvodnim spiku zbyvaji kameny
            
        if len(self.spike_list[spiky_k_presunuti[1]]["kameny"]) == 1 and len(self.spike_list[spiky_k_presunuti[0]]["kameny"]) > 1:
            self.spike_list[spiky_k_presunuti[0]]["kameny"].remove("x")      # kamen se presouva, smazani z puvodniho spiku
            self.spike_list[spiky_k_presunuti[1]]["barva"] = barva_hrace1
                
        # presunuti na spike s jednim kamenem jine barvy .... na puvodnim spiku nezbyvaji kameny
            
        if len(self.spike_list[spiky_k_presunuti[1]]["kameny"]) == 1 and len(self.spike_list[spiky_k_presunuti[0]]["kameny"]) == 1:
            self.spike_list[spiky_k_presunuti[0]]["kameny"].remove("x")      # kamen se presouva, smazani z puvodniho spiku
            self.spike_list[spiky_k_presunuti[0]]["barva"] = None            # barva puvodniho spiku se zmeni na None
            self.spike_list[spiky_k_presunuti[1]]["barva"] = barva_hrace1    # barva se prida na cilovy spike
            
        print(self.spike_list)
            
    
    def presun(self, id_hrace, hod_kostkou, barva_hrace1, barva_hrace2):  # id hrace pro smer, hod_kostkou pro dostupne tahy
                                                                          # hrac vs hrac (1,2) , hrac vs ai (1,3) .... (x,y) = (barva_hracex, barva_hracey)
        
        barva_hrace1 = "bila"
        barva_hrace2 = "cerna"
        barva_hrace3 = "cerna"
        
        # hraje hrac 1                                                  dulezite poradi
        if id_hrace == 1:                                             #            #
            self.provest_presun_pro_hrace(id_hrace, hod_kostkou, barva_hrace1, barva_hrace2)
        
        # hraje hrac 2
        if id_hrace == 2:                                            #             #
            self.provest_presun_pro_hrace(id_hrace, hod_kostkou, barva_hrace2, barva_hrace1)
        
        # hraje ai , pokud je hra s ai automaticky hraje jen hrac s id1 a ai
        if id_hrace == 3:
            
            # vypis kamenu (spiku), ktere jsou k dispozici
            podezrele_dostupne_tahy = []                                                     # index spiku .... S1....S2....S3....S4
            for i in range(len(self.spike_list)):
                if len(self.spike_list[i]["kameny"]) > 0 and self.spike_list[i]["barva"] == barva_hrace3:    # pokud v spiku je nejaky kamen a ma barvu hrace zapise se do moznych tahu
                    podezrele_dostupne_tahy.append(i)                                                        # index dostupneho kamene ve spiku self.spike_list[i]
            
                                                                                                             # dostupne_tahy
                                                                                                             # kontrola spiku v pripade kdyby chtel hrac posunout sutr (aby na tomto spiku nebyl jiny hrac.... pokud by byl a mel by 1 sutr pak ho muze vyhodit)
            
            print(self.spike_list)
            
            tahy = [] # dvojce .... (Sx, Sy)
            for i in podezrele_dostupne_tahy:
                if i-hod_kostkou >= 0:
                    
                       # kontrola poctu kamenu mozneho tahu.... pripsani na seznam dostupnych tahu
                    if len(self.spike_list[i-hod_kostkou]["kameny"]) == 0:
                                    # Sx , Sy
                        tahy.append((i,i-hod_kostkou))
                    
                    
                    if len(self.spike_list[i-hod_kostkou]["kameny"]) == 1 and self.spike_list[i-hod_kostkou]["barva"] == barva_hrace1:
                        tahy.append((i,i-hod_kostkou))
                    
                    if len(self.spike_list[i-hod_kostkou]["kameny"]) > 0 and len(self.spike_list[i-hod_kostkou]["kameny"]) < 5 and self.spike_list[i-hod_kostkou]["barva"] == barva_hrace3:
                        tahy.append((i,i-hod_kostkou))
            
            
            # ai vytvoreni voleb
            
            print(f"Hrac: {id_hrace}\nHodil kostkou: {hod_kostkou}")
                
            kombinace = 1                                                   # index zacina od 1 bude treba ho zmensit pokud se s nim bude pracovat jako s prvnim prvkem v seznamu
            platne_kombinace = []
            for sx, sy in tahy:
                print(f"({kombinace}) Kamen z S{sx} na S{sy}")
                platne_kombinace.append(kombinace)
                kombinace += 1
            
            # vyber
            
            
            volba = random.randint(1, len(platne_kombinace))
                
            spiky_k_presunuti = [tahy[volba-1][0], tahy[volba-1][1]]
                
            if volba in platne_kombinace:
                temp = volba-1              # zmensen o 1 aby se s nim dalo pocitat jako s opravdovym prvkem v seznamu.... len(x) != indexy x.... len(x) + 1 == indexy x
                        
                print(f"AI posouva kamen z S{tahy[temp][0]} na S{tahy[temp][1]}")
            
                
            #############################
            
            # presunuti
            
            # presunuti na prazdny spike .... na puvodnim spiku zbyvaji kameny
            
            if len(self.spike_list[spiky_k_presunuti[1]]["kameny"]) == 0 and len(self.spike_list[spiky_k_presunuti[0]]["kameny"]) > 1:
                self.spike_list[spiky_k_presunuti[0]]["kameny"].remove("x")      # kamen se presouva, smazani z puvodniho spiku
                self.spike_list[spiky_k_presunuti[1]]["kameny"].append("x")      # kamen se pridal na novy spike
                self.spike_list[spiky_k_presunuti[1]]["barva"] = barva_hrace3    # barva se pridala na novy spike
            
            # presunuti na prazdny spike .... na puvodnim spiku nezbyvaji kameny
            
            if len(self.spike_list[spiky_k_presunuti[1]]["kameny"]) == 0 and len(self.spike_list[spiky_k_presunuti[0]]["kameny"]) == 1:
                self.spike_list[spiky_k_presunuti[0]]["kameny"].remove("x")      # kamen se presouva, smazani z puvodniho spiku
                self.spike_list[spiky_k_presunuti[0]]["barva"] = None            # barva puvodniho spiku se zmeni na None
                self.spike_list[spiky_k_presunuti[1]]["kameny"].append("x")      # kamen se pridal na novy spike
                self.spike_list[spiky_k_presunuti[1]]["barva"] = barva_hrace3    # barva se pridala na novy spike
                
            # presunuti na spike s jednim kamenem jine barvy .... na puvodnim spiku zbyvaji kameny
            
            if len(self.spike_list[spiky_k_presunuti[1]]["kameny"]) == 1 and len(self.spike_list[spiky_k_presunuti[0]]["kameny"]) > 1:
                self.spike_list[spiky_k_presunuti[0]]["kameny"].remove("x")      # kamen se presouva, smazani z puvodniho spiku
                self.spike_list[spiky_k_presunuti[1]]["barva"] = barva_hrace3
                
            # presunuti na spike s jednim kamenem jine barvy .... na puvodnim spiku nezbyvaji kameny
            
            if len(self.spike_list[spiky_k_presunuti[1]]["kameny"]) == 1 and len(self.spike_list[spiky_k_presunuti[0]]["kameny"]) == 1:
                self.spike_list[spiky_k_presunuti[0]]["kameny"].remove("x")      # kamen se presouva, smazani z puvodniho spiku
                self.spike_list[spiky_k_presunuti[0]]["barva"] = None            # barva puvodniho spiku se zmeni na None
                self.spike_list[spiky_k_presunuti[1]]["barva"] = barva_hrace3    # barva se prida na cilovy spike
            
            print(self.spike_list) 


# kamen = Kamen(0)
# print(kamen.barva)
# kamen.vypis()



class Menu:
    def __init__(self, options, config) -> None:
        self._player2_barvy = None
        self._player1_barvy = None
        self._player1 = None
        self._player2 = None
        self._options = options
        self._conf = config

    @property
    def self_options(self):
        return self._options
    
    @property
    def self_conf(self):
        return self._conf

    def __init__(self, options, config) -> None:
        self._options = options
        self._conf = config

    """
        Predstava funkce menu:
            -> uzivatel vybere moznost PLAY:
                -> podle vyberu herniho modu se pokracuje
                    PvE:
                    - zatim nic
                    PvP:
                    - pokud pote vybere moznost nacist, hra pres load() vezme data z configu a pokracuje se ve hre
                    - pokud vybere moznost Nova hra, spusti se funkce game_setup(), 
                        data se ulozi/prepisou do configu a nasledne se spusti funkce load()
            -> uzivatel vybere moznost QUIT:
                - cela hra se vypne 
    """
    @property
    def herni_nastaveni(self):
        pass

    @property
    def game_setup(self):

        # volba PVP, PVE
        print(" VITEJTE VE HRE VRHCABY! \n      MOZNOSTI HRY        \n       PvE    PvP\n")

        while True:
            volba = input("vase volba : ")
            volba.lower()

            if volba not in ["pve", "pvp"]:
                print("Tento mod neni v nabidce.")
            else:
                print(f"Vybrali jste mod : {volba}\n")
                break

        # zmena jmena
        def zmena_jmena(i: int):

            while True:
                max_delka = 10
                print(f"\nZadejte jmeno pro hrace ({i}) | delka jmena 3 - 10")
                vybrane_jmeno = input("Zvolene jmeno: ")

                if len(vybrane_jmeno) < 3 or len(vybrane_jmeno) > 10:
                    print("Jmeno nesplnuje podminky!")

                else:
                    return vybrane_jmeno

        def nastaveni_barvy(barvy: list):
            while True:
                print(f"\nVyberte barvu z nasledujicich: {barvy}")
                vybrana_barva = input("Zvolena barva: ")

                if vybrana_barva in barvy:
                    barvy.remove(vybrana_barva)
                    return vybrana_barva, barvy

                else:
                    print("Tato barva se nenachazi v moznostech!")


        # volba jmen PVP
        if volba == "pvp":
            barvy = ["a", "b", "c", "d"]                          # zatim orientacne, jen potreba doplnit barvy

            self._player1 = zmena_jmena(1)
            self._player1_barvy = nastaveni_barvy(barvy)
            self._player2 = zmena_jmena(2)
            self._player2_barvy = nastaveni_barvy(barvy)
            self._game_mod = "pvp"
            

        # volba jmen PvE
        if volba == "pve":

            barvy = ["a", "b", "c", "d"]                          # zatim orientacne, jen potreba doplnit barvy
            self._player1 = zmena_jmena(1)
            self._player1_barvy = nastaveni_barvy(barvy)
            self._player2 = "AI"
            self._player2_barvy = random.choice(barvy)
            self._game_mod = "pve"


    def save(self):
        # ulozeni dat do json souboru zpusobem prepsani
        # aktualni data
        data = {
            "menu_options": ["PLAY (AI)", "PLAY (PvP)", "QUIT"],
            "commands": ["hod"],

            "game_save": {

                "game_stat":
                    {
                    "round": 0,                           # provizorne
                    "player_turn": "?",                   # ?
                    "last_dice": []                       # provizorne
                    },

                "player1":
                    {
                    "name": self.player1,
                    "color": self._player1_barvy,
                    "score": "",                         # provizorne
                    },

                "player2":
                    {
                    "name": self.player2,
                    "color": self._player2_barvy,
                    "score": "",                         # provizorne
                    }
                }
            }

        # existujici soubor, ktery se prepise
        with open("cfg.json", "w") as f:
            json.dump(data, f)

            
    def load(self):
        # nacteni informaci z json souboru
        
        with open("cfg.json", "r") as f:
            data = json.load(f)
        
        # game_stat
        round = data["game_save"]["game_stat"]["round"]                           # provizorne
        self.player_turn = data["game_save"]["game_stat"]["player_turn"]          # ?
        last_dice = data["game_save"]["game_stat"]["last_dice"]                   # provizorne
        
        #player1
        self.player1 = data["game_save"]["player1"]["name"]
        self._player1_barvy = data["game_save"]["player1"]["color"]
        #self.player_1.score = data["game_save"]["player1"]["score"]              # zatim provizorne, nejsem si jistej k cemu priradit score
        
        #player2
        self.player2 = data["game_save"]["player2"]["name"]
        self._player2_barvy = data["game_save"]["player2"]["color"]
        #self.player_2.score = data["game_save"]["player2"]["score"]              # zatim provizorne, nejsem si jistej k cemu priradit score

    @staticmethod
    def quit_game():
        quit()


def main() -> object:
    config_file = './cfg.json'
    #menu1 = Menu('', 'cfg.json')
    #menu1.game_setup()
    game1 = Game(1,1, "hrac1", "hrac2")
    # vypis hry do konzole
    style.clear()
    print(style.YELLOW + "Vítejte ve hře Vrhcáby" + style.RESET)
    while True:
        style.clear()
        print(game1.gameboard_final(game1.doubledice, game1.spikes, game1.last_command, game1.turn, game1.player_turn))
        print(style.GREEN + "Made by: Jakub Ryšánek, Ondřej Thomas, Jakub Kepič" + style.RESET)
        cmd_line = input("> ")
        try:
            game1.command_detection(cmd_line, config_file, game1.player_turn)
        except FileNotFoundError:                                               # terminal ve VS Codu ma oproti normalnimu cmd problem najit cfg soubor
            config_file = "src/cfg.json"                                        # proto tento odchyt vyjimky
            game1.command_detection(cmd_line, config_file, game1.player_turn)


if __name__ == "__main__":
    main()
