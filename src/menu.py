import random
import json

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


    def quit_game(self):
        quit()

     ## návrh pro implementování událostí
    # Inicializace herní desky
    board = [[0] * 24 for _ in range(2)]

    # Funkce pro vhození kamene do hry
    def enter_piece(player, point, board=None):
        board[player][point] += 1
        print(f"Hráč {player} vhozen kámen na pozici {point}")

    # Funkce pro vyhození kamene z hry
    def remove_piece(player, point, board=None):
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
