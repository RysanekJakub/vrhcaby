import random
import json
import os
import platform

class Menu:
    def __init__(self) -> None:
        self._player1 = ""
        self._player2 = ""
        self._game_mod = ""
        self._round = 0
        self._player_turn = ""
        self._last_dice = []
        self._spikes = []
        self._bar = []
        self._domecky = []
        self._save_nazev = ""

    def game_setup(self):
        os.system("cls")
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
                print(f"\nZadejte jmeno pro hrace ({i}) | delka jmena 3 - 10")
                vybrane_jmeno = input("Zvolene jmeno: ")
                if len(vybrane_jmeno) < 3 or len(vybrane_jmeno) > 10:
                    print("Jmeno nesplnuje podminky!")

                else:
                    return vybrane_jmeno

        # volba jmen PVP
        if volba == "pvp":
            self._player1 = zmena_jmena(1)
            self._player2 = zmena_jmena(2)
            self._game_mod = "pvp"
            self._player_turn = self._player1

        # volba jmen PvE
        if volba == "pve":
            self._player1 = zmena_jmena(1)
            self._player2 = "AI"
            self._game_mod = "pve"
            self._player_turn = self._player1

        

    def save(self, save_data:list):
        # ulozeni dat do json souboru zpusobem prepsani
        # aktualni data
        if len(save_data) == 0:
            save_nazev = input("Zvolte nazev savu: ")
            self._save_nazev = save_nazev
        else:
            self._game_mod = save_data[0]
            self._round = save_data[1]
            self._player_turn = save_data[2]
            self._last_dice = save_data[3]
            self._spikes = save_data[4]
            self._bar = save_data[5]
            self._domecky = save_data[6]
            self._player1 = save_data[7]
            self._player2 = save_data[8]

        data = {
                "game_save":{
                    "game_stat":{
                        "game_mod": self._game_mod,
                        "round": self._round,
                        "player_turn": self._player_turn,
                        "last_dice": self._last_dice,
                        "spikes": self._spikes,
                        "bar": self._bar,
                        "domecky": self._domecky
                        },
                        "player1":{
                            "name": self._player1
                        },
                        "player2":{
                            "name": self._player2
                        }
                    }
                }

        # existujici soubor, ktery se prepise
        save_nazev = str(self._save_nazev)
        print(save_nazev)
        with open(f"saves/{save_nazev}.json", "w") as f:
            json.dump(data, f)

            
    def load(self, save_nazev):
        # nacteni informaci z json souboru
        print(save_nazev)
        with open(f"saves/{save_nazev}.json", "r") as f:
            data = json.load(f)
        
        # game_stat

        self._game_mod = data["game_save"]["game_stat"]["game_mod"]
        self._round = data["game_save"]["game_stat"]["round"]                           # provizorne
        self._player_turn = data["game_save"]["game_stat"]["player_turn"]          # ?
        self._last_dice = data["game_save"]["game_stat"]["last_dice"]                   # provizorne
        self._spikes = data["game_save"]["game_stat"]["spikes"]
        self._bar = data["game_save"]["game_stat"]["bar"]
        self._domecky = data["game_save"]["game_stat"]["domecky"]
        #player1
        self._player1 = data["game_save"]["player1"]["name"]
        #player2
        self._player2 = data["game_save"]["player2"]["name"]

    def quit_game(self):
        quit()


menu = Menu()
moznosti = ["NOVA HRA", "NACIST", "ODEJIT"]
vybrano_nacteni = False
while vybrano_nacteni == False:
    if platform.system() == "Windows":
        os.system("cls")
    elif platform.system() == "Linux" or platform.system() == "Darwin":
        os.system("clear")

    print(f"| {'VRHCÁBY'.center(187, ' ')} |")  
    for idx, moznost in enumerate(moznosti):    # vypis moznosti v menu
        moznost = f"{idx+1}) {moznost}"         
        print(f"| {moznost.center(187, ' ')} |")
    
    try:
        vyber = int(input(">"))
        # pokud je vyber 1, znamena to, ze hrac chce vytvorit novy save
        if vyber == 1:
            menu.game_setup()   # zavolani funkce pro ziskani hodnot k zapsani do savu
            menu.save([])       # prazdny list pri volani funkce == pouziti save templatu
        # pokud je vyber 2, znamena to, ze hrac chce nacist save
        elif vyber == 2:
            savy = [filename.split(".")[0] for filename in os.listdir('saves')] # nalezeni vsech savu ve slozce 'saves'
            for idx, nazev in enumerate(savy):                                  # uprava pro vypis do konzole
                print(f"{idx+1}) {nazev}")
            while True:
                y = int(input("vyber save: "))      # po vypsani savu ve slozce 'saves' se ziska chteny save
                if savy[y-1]:
                    menu.load(savy[y-1])
                    vybrano_nacteni = True          # tohle znamena, ze save se nacetl a kod while loop v 'menu.py' neni potreba
                    break                           
                else:
                    print(f"Save {y} neni ve vyberu")
        elif vyber == 3:
            menu.quit_game()                        
    except ValueError:
        print("zadana moznost neni cislo")