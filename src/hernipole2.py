import random


class Kamen:
    
    def __init__(self, barva):
        self.barva = barva
        self.pamet = []
        
    def zmena(self, index):
        self.pamet.append(index)
        
        
class Hernipole:
    
    def __init__(self):
        self.spikes = []
    
    def nacteni_spiku(self):
        for i in range(23):
            self.spikes.append({"kameny": [], "barva": None})
            
            if i == 0:
                sutr = Kamen("cerna")
                sutr.zmena(i)
                for j in range(2):
                    self.spikes[i]["kameny"].append(sutr)
                    
                self.spikes[i]["barva"] = "cerna"
            
            if i == 5:
                sutr = Kamen("bila")
                sutr.zmena(i)
                for j in range(5):
                    self.spikes[i]["kameny"].append(sutr)
                
                self.spikes[i]["barva"] = "bila"
                    
            if i == 7:
                sutr = Kamen("bila")
                sutr.zmena(i)
                for j in range(3):
                    self.spikes[i]["kameny"].append(sutr)
                
                self.spikes[i]["barva"] = "bila"
            
            if i == 11:
                sutr = Kamen("cerna")
                sutr.zmena(i)
                for j in range(5):
                    self.spikes[i]["kameny"].append(sutr)
                
                self.spikes[i]["barva"] = "cerna"
            
            if i == 13:
                sutr = Kamen("bila")
                sutr.zmena(i)
                for j in range(5):
                    self.spikes[i]["kameny"].append(sutr)
                
                self.spikes[i]["barva"] = "bila"
                    
            if i == 16:
                sutr = Kamen("cerna")
                sutr.zmena(i)
                for j in range(3):
                    self.spikes[i]["kameny"].append(sutr)
                
                self.spikes[i]["barva"] = "cerna"
            
            if i == 19:
                sutr = Kamen("cerna")
                sutr.zmena(i)
                for j in range(5):
                    self.spikes[i]["kameny"].append(sutr)
                
                self.spikes[i]["barva"] = "cerna"
            
            if i == 23:
                sutr = Kamen("bila")
                sutr.zmena(i)
                for j in range(2):
                    self.spikes[i]["kameny"].append(sutr)
                
                self.spikes[i]["barva"] = "bila"
    
    def tah(self, id_hrace, hod_kostkou):
        
        # id_hrac = 1 ..... bila
        if id_hrace == 1:
            
            # zkoumani podezrelych tahu
            mozne_tahy = []
            for i in range(len(self.spikes)):
                if self.spikes[i]["barva"] == "bila" and self.spikes[i] != 23:               # spike s barvou hrace
                    
                    # spike na ktery presouvame nema barvu
                    if self.spikes[i-hod_kostkou]["barva"] == None:                        
                        mozne_tahy.append((i, i-hod_kostkou, "prazdno"))
                        
                    # spike na ktery presouvame ma barvu protivnika a je jen jeden kamen
                    if self.spikes[i-hod_kostkou]["barva"] == "cerna" and len(self.spikes[i-hod_kostkou]["kameny"]) == 1:
                        mozne_tahy.append((i, i-hod_kostkou, "vyhozeni"))
                        
                    # spike na ktery presouvame ma barvu hrace
                    if self.spikes[i-hod_kostkou]["barva"] == "bila" and len(self.spikes[i-hod_kostkou]["kameny"]) > 0:
                        mozne_tahy.append((i, i-hod_kostkou, "pridani"))
            
            # vyber z podezrelych tahu
            while True:
                i = 0
                print("--------------------------")
                print("VYBERTE SI TAH")
                print("--------------------------")
                for start, end, druh in mozne_tahy:
                    print(f"({i}) kamen z S{start} na S{end} - {druh}")
                    i += 1
                
                while True:
                    print("--------------------------")
                    volba = input("vyberte z voleb: ")
                    
                    if volba.isdigit() == True:
                        volba = int(volba)
                        
                        if volba >= 0 and volba <= i:
                            print("--------------------------")
                            print(f"vybrali jste: {volba}")
                            
                            klic = (mozne_tahy[volba][0], mozne_tahy[volba][1], mozne_tahy[volba][2])
                            
                            break
                        
                        else:
                            print("tato volba neni v moznostech")
                            
                    else:
                        print("zadejte cislo")
                
                break
            
            # indexy  start    end     druh
            #           0      1      2
            #
            # klic odkazuje na mozne_tahy .... lepsi prehlednost
            #
            # po presunu nezbyde kamen na start spiku
            if klic[2] == "prazdno" and len(self.spikes[start]["kameny"]) == 1:
                presouvany_kamen = self.spikes[start]["kameny"][-1]                   # vybrani presouvaneho kamene
                presouvany_kamen.pamet.append(end)                                    # pridani nove pozice do pameti
                del self.spikes[start]["kameny"][-1]                                  # smazani z puvodniho spiku
                self.spikes[end]["kameny"].append(presouvany_kamen)                   # pridani na novy spike
                self.spikes[start]["barva"] = None                                    # puvodni spike ma barvu None pro prehlednost
                
                self.spikes[end]["barva"] = "bila"                                    # nastaveni nove barvy
            
            # po presunu zbyde kamen na start spiku
            if klic[2] == "prazdno" and len(self.spikes[start]["kameny"]) > 1:
                presouvany_kamen = self.spikes[start]["kameny"][-1]                   # vybrani presouvaneho kamene
                presouvany_kamen.pamet.append(end)                                    # pridani nove pozice do pameti
                del self.spikes[start]["kameny"][-1]                                  # smazani z puvodniho spiku
                self.spikes[end]["kameny"].append(presouvany_kamen)                   # pridani na novy spike
                self.spikes[start]["barva"] = None                                    # puvodni spike ma barvu None pro prehlednost
                
                self.spikes[end]["barva"] = "bila"                                    # nastaveni nove barvy
                
            # po presunu vyhodim kamen protivnika a na startu nezbyde kamen
            if klic[2] == "vyhozeni" and len(self.spikes[start]["kameny"]) == 1:
                presouvany_kamen = self.spikes[start]["kameny"][-1]                  # vybrani presouvaneho kamene
                presouvany_kamen.pamet.append(end)                                   # pridani nove pozice do pameti
                del self.spikes[start]["kameny"][-1]                                 # smazani z puvodniho spiku
                self.spikes[end]["barva"] = None                                     # puvodni spike ma barvu None pro prehlednost
                
                
                del self.spikes[end]["kameny"][-1]                                   # smazani protivnikova kamene
                self.spikes[end]["kameny"].append(presouvany_kamen)                  # pridani na novy spike
                self.spikes[end]["barva"] = "bila"                                   # nastaveni nove barvy
            
            # po presunu vyhodim kamen protivnika a na startu zbyde kamen
            if klic[2] == "vyhozeni" and len(self.spikes["start"]["kameny"]) > 1:
                presouvany_kamen = self.spikes[start]["kameny"][-1]                  # vybrani presouvaneho kamene
                presouvany_kamen.pamet.append(end)                                   # pridani nove pozice do pameti
                del self.spikes[start]["kameny"][-1]                                 # smazani z puvodniho spiku
                
                del self.spikes[end]["kameny"][-1]                                   # smazani protivnikova kamene
                self.spikes[end]["kameny"].append(presouvany_kamen)                  # pridani na novy spike
                self.spikes[end]["barva"] = "bila"                                   # nastaveni nove barvy
                
                

hra = Hernipole()
hra.nacteni_spiku()
hra.tah(1,1)
print("hovno")
