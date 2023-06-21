import random

class Dvojkostka:

    def __init__(self) -> None:
        self._dvojkostka = []

    def hodit(self) -> list:
        # procisteni hozenych hodnot
        self._dvojkostka.clear()
        hod1, hod2 = random.randint(1, 6), random.randint(1, 6)
        # kontrola hozenych hodnot
        if hod1 != hod2:
            self._dvojkostka.append(str(hod1))
            self._dvojkostka.append(str(hod2))
            return self._dvojkostka
        # pokud se cisla rovnaji, vrati se 4x
        else:
            for _ in range(4):
                self._dvojkostka.append(str(hod1))
            return self._dvojkostka
        
dvojkostka = Dvojkostka()