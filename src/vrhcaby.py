import json
import os
import random
import platform

from domecek import Domecek
from bar import Bar
from herni_pole import hra

# pro zajisteni barev v konzoli
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
        self._game_mode = "pvp"              # game_mod se nastavi v gamesetup
        self._vykresleni_spikes = [[[0]for _ in range(6)] for _ in range(4)]    # default kdyby se neco pokazilo
                                                                    # formatovani hry by se jinak rozbilo - takhle to aspon neni tak hrozny
        self._reversed = 0

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

    @property
    def vykresleni_spikes(self):
        return self._vykresleni_spikes
    
    @vykresleni_spikes.setter
    def vykresleni_spikes(self, value):
        self._vykresleni_spikes = value

    @property
    def game_mode(self):
        return self._game_mode


    def next_turn(self, p_turn:int) -> int:
        self.turn += 1
        if p_turn == self.player1:
            self.player_turn = self.player2
        else:
            self.player_turn = self.player1


    def throw_dice(self, dice:list) -> list:
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
            
            if self._reversed < 12:
                spikes_lists[sektor].reverse()
                self._reversed +=1
            else:
                pass
            #print(spikes_lists[sektor])
            #print(" ")
            for spike in spikes_lists[sektor]:  # zde se ze seznamu sektoru vybere pozadovany sektor, ktery obsahuje seznamy vsech spiku
                #print(spike)
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

    def gameboard_final(self, values:list, command:str, cur_turn: int, hrac_tah: str, domecky_kameny: list, bar: list) -> str:
        # dopocet chybejicich mezer kvuli formatovani
        # asi by to slo elegantneji... treba pozdeji :)
        if len(values) == 2:
            spaces = 166*" "
        elif len(values) == 4:
            spaces = 160*" "
        else:
            spaces = 170*" "
        
        # dopocitani mezer u radku s poslednim prikazem
        delka_prikazu = len(command)
        if delka_prikazu > 0:
            command = command + (177-delka_prikazu)*" "
        else:
            command = (168-delka_prikazu)*" "

        delka_tah = len(str(cur_turn))                              # -|
        if delka_tah > 0:                                           #  |
            cur_turn = f"{cur_turn}{(179-delka_tah)*' '}"         #  | nevim proc, ale tahle cast se pri vypisu do konzole buguje a je potřeba vzdy rucne upravit 
                                                                    #  | velikost okna konzole
        delka_jmena_hrace = len(hrac_tah)                           #  |
        hrac_tah = f"{hrac_tah}{(178-delka_jmena_hrace)*' '}"     # -|

        bily_domecek = ["O" for _ in range(len(domecky_kameny[0]))]
        cerny_domecek = ["O" for _ in range(len(domecky_kameny[1]))]

        # tvorba cislovani spiku
        spike_row1 = ([str(_) for _ in range(6, 0, -1)], [str(_) for _ in range(9,6, -1)], [str(_) for _ in range(12, 9, -1)])
        spike_row2 = ([str(_) for _ in range(13,19)], [str(_) for _ in range(19, 25)])

        # zatim je v tom bordel, pochopitelne to neni ani zdaleka finalni
        gameboard = f"""

 ____________________________________________________________________________________________________________________________________________________________________________________________
|                                                                                          {style.BLUE}VRHCABY{style.RESET}                                                                                          |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Poslední příkaz: {command} |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Kolo: {cur_turn} |
| Hraje: {hrac_tah} |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Hozené hodnoty: {style.LIGHT_BLUE}{"  ".join(values)}{style.RESET}{spaces}| 
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| {" "*(153+(15-len(cerny_domecek)))}Cerny domecek: [{"".join(cerny_domecek)}] |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|{style.RED}       {"             ".join(spike_row1[2])}              {"              ".join(spike_row1[1])}                   {"              ".join(spike_row1[0])}{style.RESET}        |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| {"".join(self.sektor_spiku_vrchni(1,self.vykresleni_spikes)[0])} | | {"".join(self.sektor_spiku_vrchni(0,self.vykresleni_spikes)[0])} |
| {"".join(self.sektor_spiku_vrchni(1,self.vykresleni_spikes)[1])} | | {"".join(self.sektor_spiku_vrchni(0,self.vykresleni_spikes)[1])} |
| {"".join(self.sektor_spiku_vrchni(1,self.vykresleni_spikes)[2])} | | {"".join(self.sektor_spiku_vrchni(0,self.vykresleni_spikes)[2])} |
| {"".join(self.sektor_spiku_vrchni(1,self.vykresleni_spikes)[3])} | | {"".join(self.sektor_spiku_vrchni(0,self.vykresleni_spikes)[3])} |
| {"".join(self.sektor_spiku_vrchni(1,self.vykresleni_spikes)[4])} | | {"".join(self.sektor_spiku_vrchni(0,self.vykresleni_spikes)[4])} |
| {"".join(self.sektor_spiku_vrchni(1,self.vykresleni_spikes)[5])} | | {"".join(self.sektor_spiku_vrchni(0,self.vykresleni_spikes)[5])} |
| {"".join(self.sektor_spiku_vrchni(1,self.vykresleni_spikes)[6])} | | {"".join(self.sektor_spiku_vrchni(0,self.vykresleni_spikes)[6])} |
|{" "*92}| |{" "*92}|
|{" "*92}|{len(bar[0])}|{" "*92}|
|{" "*92}| |{" "*92}|
|{" "*92}| |{" "*92}|
|{" "*92}|{len(bar[1])}|{" "*92}|
|{" "*92}| |{" "*92}|
| {"".join(self.sektor_spiku_spodni(2,self.vykresleni_spikes)[0])} | | {"".join(self.sektor_spiku_spodni(3,self.vykresleni_spikes)[0])} |
| {"".join(self.sektor_spiku_spodni(2,self.vykresleni_spikes)[1])} | | {"".join(self.sektor_spiku_spodni(3,self.vykresleni_spikes)[1])} |
| {"".join(self.sektor_spiku_spodni(2,self.vykresleni_spikes)[2])} | | {"".join(self.sektor_spiku_spodni(3,self.vykresleni_spikes)[2])} |
| {"".join(self.sektor_spiku_spodni(2,self.vykresleni_spikes)[3])} | | {"".join(self.sektor_spiku_spodni(3,self.vykresleni_spikes)[3])} |
| {"".join(self.sektor_spiku_spodni(2,self.vykresleni_spikes)[4])} | | {"".join(self.sektor_spiku_spodni(3,self.vykresleni_spikes)[4])} |
| {"".join(self.sektor_spiku_spodni(2,self.vykresleni_spikes)[5])} | | {"".join(self.sektor_spiku_spodni(3,self.vykresleni_spikes)[5])} |
| {"".join(self.sektor_spiku_spodni(2,self.vykresleni_spikes)[6])} | | {"".join(self.sektor_spiku_spodni(3,self.vykresleni_spikes)[6])} |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|{style.RED}       {"             ".join(spike_row2[0])}                   {"             ".join(spike_row2[1])}{style.WHITE}       |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| {" "*(154+(15-len(bily_domecek)))}Bily domecek: [{"".join(bily_domecek)}] |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|___________________________________________________________________________________________________________________________________________________________________________________________|

"""
        # vrati samotny gameboard s doplnenymi hodnotami
        return gameboard
    

    def command_detection(self, command:str, cfg:str, p_turn:str, tah:int) -> str:
        command = command.lower()
        with open(cfg, 'r') as config_file:
            all_commands = json.load(config_file)['commands']
        
        if command in all_commands:
            if command == "presun":
                command = f"{style.GREEN}{command}{style.RESET}"
                self.doubledice = [int(i) for i in self.doubledice]
                if int(tah) //2 == 0:
                    hra.tah(1, sum(self.doubledice))
                else:
                    hra.tah(2, sum(self.doubledice))
                self.next_turn(p_turn)
                self.doubledice = [str(i) for i in self.doubledice]
            elif command == "hod":
                self.throw_dice(self.doubledice)
            command = f"{style.GREEN}{command}{style.RESET}"
        else:
            command = f"{style.RED}Prikaz \'{command}\' nenalezen{style.RESET}"
        self.last_command = command



def main() -> object:
    config_file = './cfg.json'
    #menu1 = Menu('', 'cfg.json')
    #menu1.game_setup()
    
    game1 = Game(1,1, "hrac1", "hrac2")
    """
    # generovani kamenu
    generovani_kamenu(Kamen.hrac1_kameny, "bila")       # hrac1 je vzdy pritomen, neni co kontrolovat
    if game1.game_mode == "pvp":                        # druhy hrac je urceny vybranym modem
        generovani_kamenu(Kamen.hrac2_kameny, "cerna")  # pokud je pritmen skutecny hrac, vygeneruji se kameny do jeho seznamu kamenu
    else:
        generovani_kamenu(Kamen.ai_kameny, "cerna")     # jinak se kameny vygeneruji kameny do seznamu pro ai
                                                        # duvod pro tuto implementaci je, ze manipulace s kameny se pro ai lisi od normalni manipulace
    """
    # generovani domecku
    hrac1_domecek = Domecek("bila")
    hrac2_domecek = Domecek("cerna")

    bar = Bar()

    game1.vykresleni_spikes = [[i["kameny"] for i in hra.spikes[0:6]], [i["kameny"] for i in hra.spikes[6:12]], [i["kameny"] for i in hra.spikes[12:18]], [i["kameny"] for i in hra.spikes[18:24]]]
    

    # vypis hry do konzole
    style.clear()
    print(style.YELLOW + "Vítejte ve hře Vrhcáby" + style.RESET)
    while True:
        style.clear()
        print(game1.gameboard_final(game1.doubledice, game1.last_command, game1.turn, game1.player_turn, (hrac1_domecek.kameny, hrac2_domecek.kameny), (bar.hrac1_kameny, bar.hrac2_kameny)))
        print(style.GREEN + "Made by: Jakub Ryšánek, Ondřej Thomas, Jakub Kepič" + style.RESET)
        cmd_line = input("> ")
        try:
            game1.command_detection(cmd_line, config_file, game1.player_turn, game1.turn)
        except FileNotFoundError:                                               # terminal ve VS Codu ma oproti normalnimu cmd problem najit cfg soubor
            config_file = "src/cfg.json"                                        # proto tento odchyt vyjimky
            game1.command_detection(cmd_line, config_file, game1.player_turn, game1.turn)


if __name__ == "__main__":
    main()
