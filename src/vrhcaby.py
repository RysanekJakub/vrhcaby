import json
import os
#import random
import platform

# import funkci z jinych souboru
from menu import *
from domecek import Domecek
from bar import bar
from hp_bar_domecek import hra
from dvojkostka import *

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
    
    def __init__(self, turn, player_turn, doubledice, player1, player2, game_mode, spikes, bar, save_nazev) -> None:
        self._turn = turn
        self._player_turn = player_turn     
        self._doubledice = doubledice
        self._player1 = player1
        self._player2 = player2
        self._last_command = ""
        self._game_mode = game_mode              # game_mod se nastavi v gamesetup
        self._spikes = spikes
        self._bar = bar
        self._save_nazev = save_nazev
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

    def kameny_to_json(self):
        spikes_info = []
        for idx, spike in enumerate(hra.spikes):
            if len(spike) > 0:
                for kamen in spike["kameny"]:
                    spikes_info.append((idx, kamen.barva, kamen.pamet))
        print(self._bar)
        self._spikes = spikes_info

    
    def next_turn(self, p_turn:int) -> int:
        self.turn += 1
        if p_turn == self.player1:
            self.player_turn = self.player2
        else:
            self.player_turn = self.player1
        
        # konvertovani informaci z objektu kamenu na ulozitelny format
        # funkce o par radku vys
        self.kameny_to_json()
        # po kazdem kole probehne ulozeni postupu
        menu.save((self.game_mode, self.turn, self.player_turn, self.doubledice, self._spikes, self._bar, self.player1, self.player2, self._save_nazev))
    

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

    def gameboard_final(self, values:list, command:str, cur_turn: int, hrac_tah: str, bar: list, spikes:list) -> str:
        # dopocet chybejicich mezer kvuli formatovani
        if len(values) == 2:
            spaces = 166*" "
        elif len(values) == 4:
            spaces = 160*" "
        else:
            spaces = 170*" "
        
        #dopocet mezer
        delka_tah = len(str(cur_turn))
        if delka_tah > 0:
            cur_turn = f"{cur_turn+1}{(179-delka_tah)*' '}"
        elif delka_tah > 1:
            cur_turn = f"{cur_turn+1}{(177-delka_tah)*' '}"

        # dopocitani mezer                                                   
        delka_jmena_hrace = len(hrac_tah)                       
        hrac_tah = f"{hrac_tah}{(178-delka_jmena_hrace)*' '}"     

        bily_domecek = ["O" for _ in range(len([i for i in spikes[0]["kameny"]]))]
        cerny_domecek = ["O" for _ in range(len([i for i in spikes[25]["kameny"]]))]

        # vykresleni poctu kamenu na baru
        bily_bar = 0
        cerny_bar = 0
        for kamen in bar:
            if kamen.barva == "bila":
                bily_bar += 1
            else:
                cerny_bar += 1

        # prevod na str, int nefunguje s joinem
        values = [str(value) for value in values]

        # tvorba cislovani spiku
        spike_row1 = ([str(_) for _ in range(6, 0, -1)], [str(_) for _ in range(9,6, -1)], [str(_) for _ in range(12, 9, -1)])
        spike_row2 = ([str(_) for _ in range(13,19)], [str(_) for _ in range(19, 25)])

        # popisky spiku (barvy)
        def center_value(value):
            if value is not None:
                return value.center(15, " ")
            else:
                return "prazdne".center(15, " ")

        sectors = [[center_value(barva["barva"]) for barva in spikes[i:i+6]] for i in range(0, 24, 6)]
        sektor1, sektor2, sektor3, sektor4 = sectors


        gameboard = f"""
 ____________________________________________________________________________________________________________________________________________________________________________________________
|                                                                                          {style.BLUE}VRHCABY{style.RESET}                                                                                          |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Poslední příkaz: {command} 
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Kolo: {cur_turn} |
| Hraje: {hrac_tah} |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Hozené hodnoty: {style.LIGHT_BLUE}{"  ".join(values)}{style.RESET}{spaces}| 
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| {" "*(154+(15-len(bily_domecek)))}Bily domecek: [{"".join(bily_domecek)}] |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|{style.RED}       {"             ".join(spike_row1[2])}              {"              ".join(spike_row1[1])}                   {"              ".join(spike_row1[0])}{style.RESET}        |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| {"".join(sektor2[::-1])} | | {"".join(sektor1[::-1])} |
| {"".join(self.sektor_spiku_vrchni(1,self.vykresleni_spikes)[0])} | | {"".join(self.sektor_spiku_vrchni(0,self.vykresleni_spikes)[0])} |
| {"".join(self.sektor_spiku_vrchni(1,self.vykresleni_spikes)[1])} | | {"".join(self.sektor_spiku_vrchni(0,self.vykresleni_spikes)[1])} |
| {"".join(self.sektor_spiku_vrchni(1,self.vykresleni_spikes)[2])} | | {"".join(self.sektor_spiku_vrchni(0,self.vykresleni_spikes)[2])} |
| {"".join(self.sektor_spiku_vrchni(1,self.vykresleni_spikes)[3])} | | {"".join(self.sektor_spiku_vrchni(0,self.vykresleni_spikes)[3])} |
| {"".join(self.sektor_spiku_vrchni(1,self.vykresleni_spikes)[4])} | | {"".join(self.sektor_spiku_vrchni(0,self.vykresleni_spikes)[4])} |
| {"".join(self.sektor_spiku_vrchni(1,self.vykresleni_spikes)[5])} | | {"".join(self.sektor_spiku_vrchni(0,self.vykresleni_spikes)[5])} |
| {"".join(self.sektor_spiku_vrchni(1,self.vykresleni_spikes)[6])} | | {"".join(self.sektor_spiku_vrchni(0,self.vykresleni_spikes)[6])} |
|{" "*92}|B|{" "*92}|
|{" "*92}|{bily_bar}|{" "*92}|
|{" "*92}| |{" "*92}|
|{" "*92}| |{" "*92}|
|{" "*92}|{cerny_bar}|{" "*92}|
|{" "*92}|C|{" "*92}|
| {"".join(self.sektor_spiku_spodni(2,self.vykresleni_spikes)[0])} | | {"".join(self.sektor_spiku_spodni(3,self.vykresleni_spikes)[0])} |
| {"".join(self.sektor_spiku_spodni(2,self.vykresleni_spikes)[1])} | | {"".join(self.sektor_spiku_spodni(3,self.vykresleni_spikes)[1])} |
| {"".join(self.sektor_spiku_spodni(2,self.vykresleni_spikes)[2])} | | {"".join(self.sektor_spiku_spodni(3,self.vykresleni_spikes)[2])} |
| {"".join(self.sektor_spiku_spodni(2,self.vykresleni_spikes)[3])} | | {"".join(self.sektor_spiku_spodni(3,self.vykresleni_spikes)[3])} |
| {"".join(self.sektor_spiku_spodni(2,self.vykresleni_spikes)[4])} | | {"".join(self.sektor_spiku_spodni(3,self.vykresleni_spikes)[4])} |
| {"".join(self.sektor_spiku_spodni(2,self.vykresleni_spikes)[5])} | | {"".join(self.sektor_spiku_spodni(3,self.vykresleni_spikes)[5])} |
| {"".join(self.sektor_spiku_spodni(2,self.vykresleni_spikes)[6])} | | {"".join(self.sektor_spiku_spodni(3,self.vykresleni_spikes)[6])} |
| {"".join(sektor3)} | | {"".join(sektor4)} |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|{style.RED}       {"             ".join(spike_row2[0])}                   {"             ".join(spike_row2[1])}{style.WHITE}       |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| {" "*(153+(15-len(cerny_domecek)))}Cerny domecek: [{"".join(cerny_domecek)}] |
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
                if int(tah) % 2 == 0:
                    hra.tah("bila", sum(self.doubledice), bar._kameny, self._player_turn)
                else:
                    hra.tah("cerna", sum(self.doubledice), bar._kameny, self._player_turn)
                self.next_turn(p_turn)
                self.doubledice = [str(i) for i in self.doubledice]
            elif command == "hod":
                
                self.doubledice = dvojkostka.hodit()
            command = f"{style.GREEN}{command}{style.RESET}"
        elif command == "q" or command == "quit":
            quit()
        else:
            command = f"{style.RED}Prikaz \'{command}\' nenalezen{style.RESET}"
        self.last_command = command



def main():
    config_file = './cfg.json'

    hra.vytvorit_pole(menu._spikes)
    
    game1 = Game(menu._round, menu._player_turn, menu._last_dice, menu._player1, menu._player2, menu._game_mod, menu._spikes, menu._bar, menu._save_nazev)
    
    # ziskani informaci o spicich pro vykresleni => dulezite pro zjisteni delky seznamu ve funkci, ktera ridi vykresleni
    game1.vykresleni_spikes = [[i["kameny"] for i in hra.spikes[0:6]], [i["kameny"] for i in hra.spikes[6:12]], [i["kameny"] for i in hra.spikes[12:18]], [i["kameny"] for i in hra.spikes[18:24]]]
    
    # vypis hry do konzole
    style.clear()
    print(style.YELLOW + "Vítejte ve hře Vrhcáby" + style.RESET)
    while True:
        # cisteni konzole pri kazdem loopu
        style.clear()
        print(game1.gameboard_final(game1.doubledice, game1.last_command, game1.turn, game1.player_turn, bar._kameny, hra.spikes))
        print(style.GREEN + "Made by: Jakub Ryšánek, Ondřej Thomas, Jakub Kepič" + style.RESET)
        cmd_line = input("> ")
        try:
            game1.command_detection(cmd_line, config_file, game1.player_turn, game1.turn)
        except FileNotFoundError:                                               # terminal ve VS Codu ma oproti normalnimu cmd problem najit cfg soubor
            config_file = "src/cfg.json"                                        # proto tento odchyt vyjimky
            game1.command_detection(cmd_line, config_file, game1.player_turn, game1.turn)


if __name__ == "__main__":
    main()
