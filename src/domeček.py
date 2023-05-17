class Domecek:
    def __init__(self):
        self.pocet_kamenu = 0
        self.barva = None

    def pridej_kamen(self, barva): #přidání kamene do domečku a nastavení barvy, pokud j domeček prázdný
        if self.pocet_kamenu == 0:
            self.barva = barva
        self.pocet_kamenu += 1

    def odeber_kamen(self): #odebrání kamene z domečku a v případě, že je domeček prázdný, vynulování barvy  barvu.
        if self.pocet_kamenu > 0:
            self.pocet_kamenu -= 1
            if self.pocet_kamenu == 0:
                self.barva = None

    def je_prazdny(self):
        return self.pocet_kamenu == 0

    def je_pro_hrace(self, barva):
        return self.barva == barva


# Příklad použití
domecek = Domecek()
domecek.pridej_kamen("bila")  # Přidáme jeden bílý kámen
print(domecek.pocet_kamenu)  # Vypíše: 1
print(domecek.je_pro_hrace("bila"))  # Vypíše: True
print(domecek.je_pro_hrace("cerna"))  # Vypíše: False
domecek.odeber_kamen()  # Odebere jeden kámen
print(domecek.je_prazdny())  # Vypíše: True
