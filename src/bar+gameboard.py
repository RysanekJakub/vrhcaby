class Bar:
    def __init__(self):
        self.board = [0] * 24
        self.bar = [0] * 2

    def add_to_bar(self, player, count=1):
        self.bar[player] += count

    def remove_from_bar(self, player, count=1):
        if self.bar[player] >= count:
            self.bar[player] -= count
            return True
        else:
            return False


def gameboard_final(self, values: list, spikes: list, command: str, cur_turn: int, p_turn: str) -> str:
    # dopocet chybejicich mezer kvuli formatovani
    # asi by to slo elegantneji... treba pozdeji :)
    if len(values) == 2:
        spaces = 166 * " "
    elif len(values) == 4:
        spaces = 160 * " "
    else:
        spaces = 170 * " "

    # tvorba cislovani spiku
    spike_row1 = ([str(_) for _ in range(1, 7)], [str(_) for _ in range(7, 10)], [str(_) for _ in range(10, 13)])
    spike_row2 = ([str(_) for _ in range(13, 19)], [str(_) for _ in range(19, 25)])

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
| {"".join(self.sektor_spiku_vrchni(0, self.spikes)[0])} | | {"".join(self.sektor_spiku_vrchni(1, self.spikes)[0])} |
| {"".join(self.sektor_spiku_vrchni(0, self.spikes)[1])} | | {"".join(self.sektor_spiku_vrchni(1, self.spikes)[1])} |
| {"".join(self.sektor_spiku_vrchni(0, self.spikes)[2])} | | {"".join(self.sektor_spiku_vrchni(1, self.spikes)[2])} |
| {"".join(self.sektor_spiku_vrchni(0, self.spikes)[3])} | | {"".join(self.sektor_spiku_vrchni(1, self.spikes)[3])} |
| {"".join(self.sektor_spiku_vrchni(0, self.spikes)[4])} | | {"".join(self.sektor_spiku_vrchni(1, self.spikes)[4])} |
| {"".join(self.sektor_spiku_vrchni(0, self.spikes)[5])} | | {"".join(self.sektor_spiku_vrchni(1, self.spikes)[5])} |
| {"".join(self.sektor_spiku_vrchni(0, self.spikes)[6])} | | {"".join(self.sektor_spiku_vrchni(1, self.spikes)[6])} |
|{" " * 92}| |{" " * 92}|
|{" " * 92}| |{" " * 92}|
|{" " * 92}| |{" " * 92}|
|{" " * 92}| |{" " * 92}|
|{" " * 92}| |{" " * 92}|
|{" " * 92}| |{" " * 92}|
| {"".join(self.sektor_spiku_spodni(2, self.spikes)[0])} | | {"".join(self.sektor_spiku_spodni(3, self.spikes)[0])} |
| {"".join(self.sektor_spiku_spodni(2, self.spikes)[1])} | | {"".join(self.sektor_spiku_spodni(3, self.spikes)[1])} |
| {"".join(self.sektor_spiku_spodni(2, self.spikes)[2])} | | {"".join(self.sektor_spiku_spodni(3, self.spikes)[2])} |
| {"".join(self.sektor_spiku_spodni(2, self.spikes)[3])} | | {"".join(self.sektor_spiku_spodni(3, self.spikes)[3])} |
| {"".join(self.sektor_spiku_spodni(2, self.spikes)[4])} | | {"".join(self.sektor_spiku_spodni(3, self.spikes)[4])} |
| {"".join(self.sektor_spiku_spodni(2, self.spikes)[5])} | | {"".join(self.sektor_spiku_spodni(3, self.spikes)[5])} |
| {"".join(self.sektor_spiku_spodni(2, self.spikes)[6])} | | {"".join(self.sektor_spiku_spodni(3, self.spikes)[6])} |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|{style.RED}       {"             ".join(spike_row2[0])}                   {"             ".join(spike_row2[1])}{style.WHITE}       |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|___________________________________________________________________________________________________________________________________________________________________________________________|
"""
    # vrati samotny gameboard s doplnenymi hodnotami
    return gameboard


def command_detection(self, command: str, cfg: str, p_turn: str) -> str:
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
    # seznamy kamenu
    hrac1_kameny = []
    hrac2_kameny = []
    ai_kameny = []

    def init(self, barva):
        self.barva = barva
        self.pamet = []  # seznam uspořádaných dvojic (přidávání pomocí appendu)

    # generovani kamenu


def generovanikamenu(seznam: list, barvahrace: str) -> None:
    for kamen in range(15):
        kamen = Kamen(barvahrace)
        seznam.append(kamen)