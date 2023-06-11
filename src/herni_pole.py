


class Kamen:
    
    def __init__(self, barva):
        self.barva = barva
        self.pamet = []
        
    def zmena(self, index):
        self.pamet.append(index)
        
class Hernipole:
    
    def __init__(self):
        self.spikes = []
        
    def vytvorit_pole(self):
        for i in range(24):
            self.spikes.append({
                "kameny":[],
                "barva":None
            })
#                indx   barva   pocet
        rozdani = [(0, "cerna", 2), (5, "bila", 5), (7, "bila", 3), (11, "cerna", 5), (13, "bila", 5), (16, "cerna", 3), (19, "cerna", 5), (23, "bila", 2)]
        
        for indx, barva, pocet in rozdani:
            self.spikes[indx]["barva"] = barva
            for i in range(pocet):
                sutr = Kamen(barva)
                self.spikes[indx]["kameny"].append(sutr)
                
#                  bila   /   cerna
    def tah(self, barva_hrace, hod_kostkou):
        
        kameny_ze_hry = []
        
        if barva_hrace == "bila":
            parametr = -1
            
        if barva_hrace == "cerna":
            parametr = 1
            
        mozne_tahy = []
        
        for i in range(len(self.spikes)):
            
#                 spike s barvou hrace
            if self.spikes[i]["barva"] == barva_hrace and i+parametr*hod_kostkou >= 0:

#                 parametr udava smer
                budouci_pozice = i + parametr*hod_kostkou

#                    kontrola spiku
#
#                    budouci spike
#                    prazdny
                if self.spikes[budouci_pozice]["barva"] == None:
                    mozne_tahy.append((i, budouci_pozice))
                    
                if self.spikes[budouci_pozice]["barva"] != barva_hrace and len(self.spikes[budouci_pozice]["kameny"]) == 1:
                    mozne_tahy.append((i, budouci_pozice))
                    
                if self.spikes[budouci_pozice]["barva"] == barva_hrace:
                    mozne_tahy.append((i, budouci_pozice))
        
#                    VYBER TAHU
        while True:
            print("-------------------------------")
            print("VYBERTE SI TAH")
            print("-------------------------------")
            
#                    ODKAZUJICI NA INDEX V MOZNE_TAHY
            temp = 0
            for x1, x2 in mozne_tahy:
                print(f"({temp}) KAMEN Z S{x1} -> S{x2}")
                temp += 1
            
            volba = input("VOLIM : ")
            if volba.isdigit() == True:
                volba = int(volba)
                if volba >= 0 and volba <= temp:
                    klic = (mozne_tahy[volba][0], mozne_tahy[volba][1])
                    break
            else:
                print("neplatna volba")


#            start x1         end x2
#            klic[0]          klic[1]
#
#   presun na prazdny spike, nezbyde sutr na puvodnim
        if len(self.spikes[klic[1]]["kameny"]) == 0 and len(self.spikes[klic[0]]["kameny"]) == 1:#  
            presouvany_kamen = self.spikes[klic[0]]["kameny"][-1]#         presouvany kamen
            presouvany_kamen.pamet.append(klic[1])#                        pridani do pameti
            del self.spikes[klic[0]]["kameny"][-1]#                        smazani z puvodniho spiku
            self.spikes[klic[1]]["kameny"].append(presouvany_kamen)#       pridani na spike
            self.spikes[klic[1]]["barva"] = barva_hrace#                   pridani barvy na spike
            self.spikes[klic[0]]["barva"] = None#                          smazani barvy z puvodniho
            return
            
#   presun na prazdny spike, zbyde sutr na puvodnim
        if len(self.spikes[klic[1]]["kameny"]) == 0 and len(self.spikes[klic[0]]["kameny"]) > 1:#
            presouvany_kamen = self.spikes[klic[0]]["kameny"][-1]#         presouvany kamen
            presouvany_kamen.pamet.append(klic[1])#                        pridani do pameti
            del self.spikes[klic[0]]["kameny"][-1]#                        smazani z puvodniho spiku
            self.spikes[klic[1]]["kameny"].append(presouvany_kamen)#       pridani na spike
            self.spikes[klic[1]]["barva"] = barva_hrace#                   pridani barvy na spike
            return

#   presun na spike s jednim kamenem protivnika, nezbyde sutr na puvodnim
        if len(self.spikes[klic[1]]["kameny"]) == 1 and self.spikes[klic[1]]["barva"] != barva_hrace and len(self.spikes[klic[0]]["kameny"]) == 1:#
            presouvany_kamen = self.spikes[klic[0]]["kameny"][-1]#         presouvany kamen
            presouvany_kamen.pamet.append(klic[1])#                        pridani do pameti
            del self.spikes[klic[0]]["kameny"][-1]#                        smazani z puvodniho spiku
            self.spikes[klic[0]]["barva"] = None#                          smazani barvy z puvodniho
            
            kameny_ze_hry.append(self.spikes[klic[1]]["kameny"][-1])#      pridani kamene vylouceneho ze hry do historie vyhozu
            del self.spikes[klic[1]]["kameny"][-1]#                        smazani protivnika
            self.spikes[klic[1]]["kameny"].append(presouvany_kamen)#       pridani na spike
            self.spikes[klic[1]]["barva"] = barva_hrace#                   pridani barvy na spike
            return
            
#   presun na spike s jednim kamenem protivnika, zbyde sutr na puvodnim
        if len(self.spikes[klic[1]]["kameny"]) == 1 and len(self.spikes[klic[0]]["kameny"]) > 1:#
            presouvany_kamen = self.spikes[klic[0]]["kameny"][-1]#         presouvany kamen
            presouvany_kamen.pamet.append(klic[1])#                        pridani do pameti
            del self.spikes[klic[0]]["kameny"][-1]#                        smazani z puvodniho spiku
            
            kameny_ze_hry.append(self.spikes[klic[1]]["kameny"][-1])#      pridani kamene vylouceneho ze hry do historie vyhozu
            del self.spikes[klic[1]]["kameny"][-1]#                        smazani protivnika
            self.spikes[klic[1]]["kameny"].append(presouvany_kamen)#       pridani na spike
            self.spikes[klic[1]]["barva"] = barva_hrace#                   pridani barvy na spike
            return
            
#   presun na spike se stejnou barvou, nezbyde sutr na puvodnim
        if len(self.spikes[klic[1]]["kameny"]) >= 1 and self.spikes[klic[1]]["barva"] == barva_hrace and len(self.spikes[klic[0]]["kameny"]) == 1:#  
            presouvany_kamen = self.spikes[klic[0]]["kameny"][-1]#         presouvany kamen
            presouvany_kamen.pamet.append(klic[1])#                        pridani do pameti
            del self.spikes[klic[0]]["kameny"][-1]#                        smazani z puvodniho spiku
            self.spikes[klic[1]]["kameny"].append(presouvany_kamen)#       pridani na spike
            self.spikes[klic[0]]["barva"] = None#                          smazani barvy z puvodniho
            return

#   presun na spike se stejnou barvou, zbyde sutr na puvodnim
        if len(self.spikes[klic[1]]["kameny"]) >= 1 and self.spikes[klic[1]]["barva"] == barva_hrace and len(self.spikes[klic[0]]["kameny"]) > 1:#  
            presouvany_kamen = self.spikes[klic[0]]["kameny"][-1]#         presouvany kamen
            presouvany_kamen.pamet.append(klic[1])#                        pridani do pameti
            del self.spikes[klic[0]]["kameny"][-1]#                        smazani z puvodniho spiku
            self.spikes[klic[1]]["kameny"].append(presouvany_kamen)#       pridani na spike
            return
            
hra1 = Hernipole()
hra1.vytvorit_pole()

indx = 0
for spike in hra1.spikes:
    print(spike, indx, len(spike["kameny"]))
    indx += 1

hra1.tah("bila", 7)

indx = 0
for spike in hra1.spikes:
    print(spike, indx, len(spike["kameny"]))
    indx += 1
