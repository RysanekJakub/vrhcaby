class Bar:

    def __init__(self) -> None:
        self._kameny = []         # kameny 

    @property 
    def kameny(self):
        return self._kameny

bar = Bar()