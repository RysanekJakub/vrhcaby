rom Figurka import Figurka
from Kostky_Kelimek import Kostky
from Pole import Pole
from Sachovnice import Sachovnice
from Bar import Bar
from Domecek import Domecek




domecek_X = Domecek()
domecek_O = Domecek()

domecek_X.domek = [0,5,4,3,2]

print(domecek_X.domek)
print(domecek_O.domek)


class Sachovnice:
    
    
    def __init__(self):
        self._sachovnice = []
     
    @property
    def sachovnice(self): #getter
            return self._sachovnice
    @sachovnice.setter
    def sachovnice(self, value):
            self._sachovnice = value
    
class Bar:
    
    
    def __init__(self):
        self._bar = []
     
    @property
    def bar(self): #getter
            return self._sachovnice
    @bar.setter
    def bar(self, value):
            self._bar = value

class Pole:
    
    def __init__(self, x, y):
        self._x = x
        self._y = y
     
    @property
    def x(self): #getter
            return self._x
    @x.setter
    def x(self, value):
            self._x = value
    @property
    def y(self): #getter
            return self._y
    @y.setter
    def y(self, value):
            self._y = value
class Domecek:
    
    
    def __init__(self):
        self._domek = []
     
    @property
    def domek(self): #getter
            return self._domek
    @domek.setter
    def domek(self, value):
            self._domek = value

class Figurka:
    
  def __init__(self, x, y, barva):
    self._barva = barva
    self._x = x
    self._y = y
    
    @property
    def barva(self): #getter
            return self._barva    
    @property
    def x(self): #getter
            return self._x
    @x.setter
    def x(self, value):
            self._x = value
    @property
    def y(self): #getter
            return self._y
    @y.setter
    def y(self, value):
            self._y = value
        
    def tahni(self, x, y):
        ...

class Kostky:
    
    def __init__(self, pocet_kostek):
        self._pocet = pocet_kostek
        
    def hod_kostky(self):
        ...