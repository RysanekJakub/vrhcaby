
import json

import random

import os

# zajistuje barvy textu
os.system("")


class style:

class style():

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
    def clear():
        os.system("cls")



class Game:


print(style.YELLOW + "Vítejte ve hře Vrhcáby" + style.RESET)

class Game:
    

    def __init__(self, gameboard, pozice, player1, player2) -> None:
        # herni pole
        self._gameboard = gameboard
        # dvojkostka
        self._doubledice = []

        self._spikes = [[] for _ in range(24)]

        self._spikes = [[] for j in range(24)]

        # bar
        self._bar = ...
        self._stone = pozice
        self._turn = 0
        self._player_turn = "player1"
        self._player1 = player1
        self._player2 = player2

        self._last_command = ""

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

    def next_turn(self, current_turn, player_turn):
        """
        Funkce bude přičítat kola a měnit hráče na tahu.
        """

        ...

    @staticmethod
    def throw_dice(dice:list) -> list:


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

    def throw_dice(self, dice) -> None:

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


    @staticmethod
    def spike_occupancy(spike_list:list) -> str:


    
    def spike_occupancy(self, spike_list:list) -> str:
        

        # nedokonceny system
        # vypisuje obsazenost spiku a zajistuje formatovani
        if 0 <= len(spike_list) < 10:
            remaining_spaces = " " * 5 # <-- doplneni mezer
        else:                          #    |
            remaining_spaces = " " * 4 # <--|
        return f"[{len(spike_list)}]{remaining_spaces}"



    def gameboard_final(self, values:list, spikes:list, command:str) -> str:

    def gameboard_final(self, values:list, spikes:list) -> str:

        s = spikes
        # dopocet chybejicich mezer kvuli formatovani
        if len(values) == 2:
            spaces = 156*" "
        else:
            spaces = 150*" "



        

        # tvorba cislovani spiku
        spike_row1 = ([str(_) for _ in range(1,7)], [str(_) for _ in range(7,10)], [str(_) for _ in range(10,13)])
        spike_row2 = ([str(_) for _ in range(13,19)], [str(_) for _ in range(19, 25)])

        # zatim je v tom bordel, pochopitelne to neni ani zdaleka finalni
        gameboard = f"""
             _________________________________________________________________________________________________________________________________________________________________________________

            | Poslední příkaz: {command}
            |---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|


            | Kolo: {self._turn}                                                                                                                                                                         |
            | Hraje: {self._player_turn}                                                                                                                                                                  |
            |---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
            | Hozené hodnoty: {style.LIGHT_BLUE}{"  ".join(values)}{style.RESET}{spaces}| 
            |---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
            |{style.RED}       {"             ".join(spike_row1[0])}                    {"             ".join(spike_row1[1])}             {"            ".join(spike_row1[2])}{style.RESET}       |
            |---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
            | \    {self.spike_occupancy(s[0])}/\     {s[1]}     /\     {s[2]}     /\     {s[3]}     /\     {s[4]}     /\     {s[5]}     /  | |  \            /\            /\            /\            /\            /\            / |
            |  \          /  \          /  \          /  \          /  \          /  \          /   | |   \          /  \          /  \          /  \          /  \          /  \          /  |
            |   \        /    \        /    \        /    \        /    \        /    \        /    | |    \        /    \        /    \        /    \        /    \        /    \        /   |
            |    \      /      \      /      \      /      \      /      \      /      \      /     | |     \      /      \      /      \      /      \      /      \      /      \      /    |
            |     \    /        \    /        \    /        \    /        \    /        \    /      | |      \    /        \    /        \    /        \    /        \    /        \    /     |
            |      \  /          \  /          \  /          \  /          \  /          \  /       | |       \  /          \  /          \  /          \  /          \  /          \  /      |
            |       \/            \/            \/            \/            \/            \/        | |        \/            \/            \/            \/            \/            \/       |
            |                                                                                       | |                                                                                       |
            |                                                                                       | |                                                                                       |
            |                                                                                       | |                                                                                       |
            |                                                                                       | |                                                                                       |
            |                                                                                       | |                                                                                       |
            |                                                                                       | |                                                                                       |
            |       /\            /\            /\            /\            /\            /\        | |        /\            /\            /\            /\            /\            /\       |
            |      /  \          /  \          /  \          /  \          /  \          /  \       | |       /  \          /  \          /  \          /  \          /  \          /  \      |
            |     /    \        /    \        /    \        /    \        /    \        /    \      | |      /    \        /    \        /    \        /    \        /    \        /    \     |
            |    /      \      /      \      /      \      /      \      /      \      /      \     | |     /      \      /      \      /      \      /      \      /      \      /      \    |
            |   /        \    /        \    /        \    /        \    /        \    /        \    | |    /        \    /        \    /        \    /        \    /        \    /        \   |
            |  /          \  /          \  /          \  /          \  /          \  /          \   | |   /          \  /          \  /          \  /          \  /          \  /          \  |
            | /            \/            \/            \/            \/            \/            \  | |  /            \/            \/            \/            \/            \/            \ |
            |---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
            |{style.RED}       {"            ".join(spike_row2[0])}                   {"            ".join(spike_row2[1])}{style.WHITE}       |
            |---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
            |_________________________________________________________________________________________________________________________________________________________________________________|
            """
        # vrati samotny gameboard s doplnenymi hodnotami
        return gameboard


    def command_detection(self, command:str, cfg:str) -> str:
        command = command.lower()
        with open(cfg, 'r') as config_file:
            all_commands = json.load(config_file)['commands']

        if command in all_commands:
            if command == "presun":
                command = f"{style.CYAN}Prikaz \'{command}\' zatím nemá zatím implementovanou funkci{style.RESET}"
            elif command == "hod":
                self.throw_dice(self.doubledice)
            command = f"{style.GREEN}{command}{style.RESET}"
        else:
            command = f"{style.RED}Prikaz {command} nenalezen{style.RESET}"
        self.last_command = command

class Menu:
    def __init__(self, options, config) -> None:
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


class Menu:
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
    def game_setup(self):

        # volba PVP, PVE
        print(" VITEJTE VE HRE VRHCABY! \n      MOZNOSTI HRY        \n       PvE    PvP\n")

        while True:
            volba = input("vase volba : ")
            volba.lower()


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
                max_delka: int = 10
                print(f"\nZadejte jmeno pro hrace ({i}) | delka jmena 3 - 10")
                vybrane_jmeno = input("Zvolene jmeno: ")


        
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


        
        def nastaveni_barvy(barvy: list, i: int):
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
            #self._player1_barvy = nastaveni_barvy(barvy, 1)
            self._player2 = zmena_jmena(2)
            #self._player2_barvy = nastaveni_barvy(barvy, 2)



        # volba jmen PvE
        if volba == "pve":


            
        
        # volba jmen PvE
        if volba == "pve":
            

            barvy = ["a", "b", "c", "d"]                          # zatim orientacne, jen potreba doplnit barvy
            self._player1 = zmena_jmena(1)
            #self._player1_barvy = nastaveni_barvy(barvy, 1)
            self._player2 = "AI"
            #self._player2_barvy = nastaveni_barvy(barvy, 2)


    def load(self):
        # v pripade vyberu moznosti nacist hru
        ...

    def play(self):
        # presun do dalsi casti menu, moznosti budou nova hra a nacit hru
        ...

    @staticmethod

    def load():
        # v pripade vyberu moznosti nacist hru
        ...

    def play():
        # presun do dalsi casti menu, moznosti budou nova hra a nacit hru
        ...


    def quit_game():
        quit()



# kostky
import random
class Dicebasket:
    def __init__(self, dicecount):
        self.dicecount = dicecount
        self. dicevalue = []

    def throw(self):
        for i in range(self.dicecount):
            self.dicevalue.append(random.randirt(1, 6))
        if len(set(self.dicevalue)) == 1:
            for i in range(self.dicecount):
                self.dicevalue.append(self.dicevalue[0])
    def __repr__(self):
        pass

    kostky = Dicebasket(2)
    kostky.throw()
    print(kostky.dicevalue)

    #gameboard(hrací deska)

import Queue_class
class Gameboard:
    def __init__(self):
        self.gameboard1 = Queue_class.Zasobnik(None)
        self.gameboard2 = Queue_class.Zasobnik(None)
        self.gameboard3 = Queue_class.Zasobnik(None)
        self.gameboard4 = Queue_class.Zasobnik(None)
        self.gameboard5 = Queue_class.Zasobnik(None)
        self.gameboard6 = Queue_class.Zasobnik(None)
        self.gameboard7 = Queue_class.Zasobnik(None)
        self.gameboard8 = Queue_class.Zasobnik(None)
        self.gameboard9 = Queue_class.Zasobnik(None)
        self.gameboard10 = Queue_class.Zasobnik(None)
        self.gameboard11 = Queue_class.Zasobnik(None)
        self.gameboard12 = Queue_class.Zasobnik(None)
        self.gameboard13 = Queue_class.Zasobnik(None)
        self.gameboard14 = Queue_class.Zasobnik(None)
        self.gameboard15 = Queue_class.Zasobnik(None)
        self.gameboard16 = Queue_class.Zasobnik(None)
        self.gameboard17 = Queue_class.Zasobnik(None)
        self.gameboard18 = Queue_class.Zasobnik(None)
        self.gameboard19 = Queue_class.Zasobnik(None)
        self.gameboard20 = Queue_class.Zasobnik(None)
        self.gameboard21 = Queue_class.Zasobnik(None)
        self.gameboard22 = Queue_class.Zasobnik(None)
        self.gameboard23 = Queue_class.Zasobnik(None)
        self.gameboard24 = Queue_class.Zasobnik(None)
        self.whitebar = Queue_class.Zasobnik(None)
        self.blackbar = Queue_class.Zasobnik(None)
        self.whitehouse = Queue_class.Zasobnik(None)
        self.blackhouse = Queue_class.Zasobnik(None)

        self.gameboard_directionary = {
            0: self.gameboard1,
            1: self.gameboard2,
            2: self.gameboard3,
            3: self.gameboard4,
            4: self.gameboard5,
            5: self.gameboard6,
            6: self.gameboard7,
            7: self.gameboard8,
            8: self.gameboard9,
            9: self.gameboard10,
            10: self.gameboard11,
            11: self.gameboard12,
            12: self.gameboard13,
            13: self.gameboard14,
            14: self.gameboard15,
            15: self.gameboard16,
            16: self.gameboard17,
            17: self.gameboard18,
            18: self.gameboard19,
            19: self.gameboard20,
            20: self.gameboard21,
            21: self.gameboard22,
            22: self.gameboard23,
            23: self.gameboard24,
            24: self.whitebar,
            25: self.blackbar,
            26: self.whitehouse,
            27: self.blackhouse
        }
        for i in range(5):
            self.gameboard_dictioanary[5].add_item("O")
            self.gameboard_dictioanary[12].add_item("O")
            self.gameboard_dictioanary[11].add_item("X")
            self.gameboard_dictioanary[18].add_item("X")
        for i in range(2):
            self.gameboard_dictioanary[0].add_item("X")
            self.gameboard_dictioanary[23].add_item("O")
        for i in range(3):
            self.gameboard_dictioanary[7].add_item("O")
            self.gameboard_dictioanary[16].add_item("X")
    def print_current_state(self):
        for key in self.gameboard_directionary.keys():
            print("pole", key+1, ": ", self.gameboard_directionary[key])
    def __repr__(self):
        pass
    def move_stone(self, frompos, topos):
        pass
    def get_position(self):
        pass

pole = Gameboard()
print(pole.print_current_state())




def main():
    config_file = './cfg.json'
    #menu1 = Menu('', 'cfg.json')
    #menu1.game_setup()
    game1 = Game(1,1, "hrac1", "hrac2")
    # hod kostkami
    #game1.doubledice = game1.throw_dice(game1.doubledice)
    # vypis hry do konzole
    style.clear()
    print(style.YELLOW + "Vítejte ve hře Vrhcáby" + style.RESET)
    while True:
        style.clear()
        print(game1.gameboard_final(game1.doubledice, game1.spikes, game1.last_command))
        print(style.GREEN + "Made by: Jakub Ryšánek, Ondřej Thomas, Jakub Kepič" + style.RESET)
        cmd_line = input("> ")
        game1.command_detection(cmd_line, config_file)




if __name__ == "__main__":
    main()

def main():
    menu = ()
    game1 = Game(1,1, "hrac1", "hrac2")
    # hod kostkami
    game1.doubledice = game1.throw_dice(game1.doubledice)
    # vypis hry do konzole
    print(game1.gameboard_final(game1.doubledice, game1.spikes))
    
    print(style.GREEN + "Made by: Jakub Ryšánek, Ondřej Thomas, Jakub Kepič" + style.RESET)

if __name__ == "__main__":
    main()

