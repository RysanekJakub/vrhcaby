class Kamen:
    # seznamy kamenu
    hrac1_kameny = []
    hrac2_kameny = []
    ai_kameny = []

    def __init__(self):
        self.pamet = None
        self.barva = None

    def init(self, barva):
        self.barva = barva
        self.pamet = []  # seznam uspořádaných dvojic (přidávání pomocí appendu)

# generovani kamenu
def generovanikamenu(seznam: list, barvahrace: str) -> None:
    for kamen in range(15):
        kamen = Kamen(barvahrace)
        seznam.append(kamen)
        