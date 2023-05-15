impimport json
impimport os
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
        self._player_turn = player1  # defaultni hodnota
        self._player1 = player1
        self._player1_barva = ""
        self._player2 = player2
        self._player2_barva = ""
        self._last_command = ""
        self._game_mod = ""  # game_mod se nastavi v gamesetup

        # TENHLE SEZNAM JE TU JEN DOCASNE
        # BUDE VYMENEN VE CHVILI KDY BUDE DOKONCENA IMPLEMENTACE TRIDY SPIKU
        # seznam necham takto rozbaleny kvuli co mozna nejlepsi citelnosti
        self._spikes = [[[] for _ in range(6)] for _ in range(4)]  # default kdyby se neco pokazilo
        # formatovani hry by se jinak rozbilo - takhle to aspon neni tak hrozny

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

    @property
    def spikes(self):
        return self._spikes

    @spikes.setter
    def spikes(self, value):
        self._spikes = value

    def next_turn(self, p_turn: int) -> int:
        self.turn += 1
        if p_turn == self.player1:
            self.player_turn = self.player2
        else:
            self.player_turn = self.player1

    @staticmethod
    def throw_dice(dice: list) -> list:
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

    def sektor_spiku_vrchni(self, sektor: int, spikes_lists: list) -> list:
        rows = []  # zde jsou vsechny radky pro vybrany sektor po formatovani
        for i in range(
                7):  # defaultni vyska radku, pozdeji jeste bude potreba upravit pro pripady, kdy se na spike dostane vice nez 7 kamenu
            row = []  # seznamy radku po jednom
            for spike in spikes_lists[
                sektor]:  # zde se ze seznamu sektoru vybere pozadovany sektor, ktery obsahuje seznamy vsech spiku
                default_mezery = " " * (6 - i)  # dopocet mezer uvnitr spiku kvuli formatovani
                vypln = " " * i  # dopocet mezer okolo spiku kvuli formatovani
                if i < len(
                        spike):  # pokud je *i* mensi nez delka seznamu spiku, kterym se zrovna prochazi, znamena to, ze tam bude kamen
                    row.append(
                        f"{vypln}\{default_mezery}O{default_mezery}/{vypln}")  # cely radek se po spojeni zapise do seznamu *row*
                else:
                    row.append(
                        f"{vypln}\{default_mezery} {default_mezery}/{vypln}")  # pokud je *i* vetsi nez delka seznamu spiku, znamena to, ze uz tam neni dalsi kamen a tak se zapise mezera
            rows.append(row)
        return rows

    def sektor_spiku_spodni(self, sektor: int, spikes_lists: list) -> list:
        # postup pri vykresleni kamenu je trochu komplikovanejsi kvuli tomu, ze se tentokrat musi kameny vypisovat odspoda nahoru
        # udelal jsem to tak, ze se vezme list kazdeho spiku a podle poctu kamenu (delky seznamu spiku) se zapisou mezery pred kameny
        # vypada-li seznam spiku takto: [1,1,1]
        # tak po teto uprave bude vypadat takto: [" "," "," "," ", 1,1,1]
        nove_listy = []
        for sektor_list in spikes_lists[sektor]:  # loop, ktery vytahne seznamy jednotlivych spiku
            missing = [" " for _ in range(
                7 - len(sektor_list))]  # zde se zapisuji mezery podle poctu kamenu na spiku do noveho seznamu
            nove_listy.append(
                missing + sektor_list)  # spojeni seznamu *missing* s mezerami a jiz existujicim seznamem spiku

        # zde uz je postup skoro stejny jako u funkce *sektor_spiku_vrchni*
        rows = []
        for i in range(7):
            row = []
            for spike in nove_listy:
                default_mezery = " " * i
                vypln = " " * (6 - i)
                if spike[i] != " ":  # pokud se i nerovna mezere, zapise se kamen
                    row.append(f"{vypln}/{default_mezery}O{default_mezery}\{vypln}")
                else:
                    row.append(f"{vypln}/{default_mezery} {default_mezery}\{vypln}")

            rows.append(row)
        return rows