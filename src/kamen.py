class Kamen:
    # seznamy kamenu
    hrac1_kameny = []
    hrac2_kameny = []
    ai_kameny = []

    def __init__(self, barva):
        self.barva = barva
        self.pamet = []  # seznam uspořádaných dvojic (přidávání pomocí appendu)

# generovani kamenu
def generovani_kamenu(seznam: list, barvahrace: str) -> None:
    for _ in range(15):
        kamen = Kamen(barvahrace)
        seznam.append(kamen)
