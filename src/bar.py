class Bar:

    def __init__(self) -> None:
        self._hrac1_kameny = []         # kameny defaultne pro hrace s kameny bile barvy
        self._hrac2_kameny = []         # kameny defaultne pro hrace s kameny cerne barvy

    @property 
    def hrac1_kameny(self):
        return self._hrac1_kameny
    @property
    def hrac2_kameny(self):
        return self._hrac2_kameny
