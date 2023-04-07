import random
import os

# zajistuje barvy textu
os.system("")

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

print(style.YELLOW + "Vítejte ve hře Vrhcáby" + style.RESET)

class Game:
    
    def __init__(self, gameboard, pozice, player1, player2) -> None:
        # herni pole
        self._gameboard = gameboard
        # dvojkostka
        self._doubledice = []
        self._spikes = [[] for j in range(24)]
        # bar
        self._bar = ...
        self._stone = pozice
        self._turn = 0
        self._player_turn = "player1"
        self._player1 = player1
        self._player2 = player2

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
    
    def spike_occupancy(self, spike_list:list) -> str:
        
        # nedokonceny system
        # vypisuje obsazenost spiku a zajistuje formatovani
        if 0 <= len(spike_list) < 10:
            remaining_spaces = " " * 5 # <-- doplneni mezer
        else:                          #    |
            remaining_spaces = " " * 4 # <--|
        return f"[{len(spike_list)}]{remaining_spaces}"


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

    def game_setup(self) -> str:
        # input -> jmena hracu, mozna i barva kamenu (tohle muzem udelat i pres random)
        # idealni by bylo vyprintovat nejakou pozitivni/negativni hlasku
        ...

    def load():
        # v pripade vyberu moznosti nacist hru
        ...

    def play():
        # presun do dalsi casti menu, moznosti budou nova hra a nacit hru
        ...

    def quit_game():
        quit()


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
