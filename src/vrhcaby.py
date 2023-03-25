import random
import os

# zajišťuje barvy textu
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
        self._gameboard = gameboard
        self._doubledice = []
        self._spikes = [[] for j in range(24)]
        # nevim co je myšlený továrnou
        self._tovarna = ...
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
        if hod1 != hod2:
            dice.append(str(hod1))
            dice.append(str(hod2))
            return dice
        else:
            for _ in range(4):
                dice.append(str(hod1))
            return dice
    
    def spike_occupancy(self, spike_list:list) -> str:
        if 0 <= len(spike_list) < 10:
            remaining_spaces = " " * 5
        else:
            remaining_spaces = " " * 4
        return f"[{len(spike_list)}]{remaining_spaces}"


    def gameboard_final(self, values:list, spikes:list) -> str:
        s = spikes
        
        
        
        # dopočet chybějících mezer kvůli formátování
        if len(values) == 2:
            spaces = 156*" "
        else:
            spaces = 150*" "
        
        spike_row1 = ([str(_) for _ in range(1,7)], [str(_) for _ in range(7,10)], [str(_) for _ in range(10,13)])
        spike_row2 = ([str(_) for _ in range(13,19)], [str(_) for _ in range(19, 25)])

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
        return gameboard
        
def main():  
    game1 = Game(1,1, "hrac1", "hrac2")
    
    game1.doubledice = game1.throw_dice(game1.doubledice)
    print(game1.gameboard_final(game1.doubledice, game1.spikes))
    print(style.GREEN + "Made by: Jakub Ryšánek, Ondřej Thomas, Jakub Kepič" + style.RESET)
if __name__ == "__main__":
    main()