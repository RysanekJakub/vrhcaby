


class Kamen:
    
    def __init__(self, barva):
        self.barva = barva
        self.pamet = []
        
    def zmena(self, index):
        self.pamet.append(index)
        
class Hernipole:
    
    def __init__(self):
        self.spikes = []
        #                                             0 - DOMECEK          25 - DOMECEK
    def vytvorit_pole(self):
        for i in range(26):
            self.spikes.append({
                "kameny":[],
                "barva":None
            })
#                indx   barva   pocet
        rozdani = [(1, "cerna", 2), (6, "bila", 5), (8, "bila", 3), (12, "cerna", 5), (14, "bila", 5), (17, "cerna", 3), (20, "cerna", 5), (24, "bila", 2)]
        
        for indx, barva, pocet in rozdani:
            self.spikes[indx]["barva"] = barva
            for i in range(pocet):
                sutr = Kamen(barva)
                self.spikes[indx]["kameny"].append(sutr)
                
#                  1   /   2
    def tah(self, barva_hrace, hod_kostkou, bar):
        
        if len(self.spikes[25]["kameny"]) == 15:
            return print("hrac cerna vyhra")
        if len(self.spikes[0]["kameny"]) == 15:
            return print("hrac bila vyhra")
        
        if barva_hrace == "bila":
            parametr = -1
            
        if barva_hrace == "cerna":
            parametr = 1
            
        mozne_tahy = []


#                  zkontrolovani baru
        for i in range(len(bar)):
#                  spike s barvou hrace
            if bar[i].barva == barva_hrace and i+parametr*-1*hod_kostkou >= 0 and i+parametr*-1*hod_kostkou <= 24:
                budouci_pozice = i+parametr*-1*hod_kostkou
                presouvany_kamen = bar[i]

                if self.spikes[budouci_pozice]["barva"] == None:
                    bar[i].pamet.append(budouci_pozice)
                    self.spikes[budouci_pozice]["kameny"].append(presouvany_kamen)
                    self.spikes[budouci_pozice]["barva"] = bar[i].barva
                    del bar[i]
                    return
                elif self.spikes[budouci_pozice]["barva"] == bar[i].barva:
                    bar[i].pamet.append(budouci_pozice)
                    self.spikes[budouci_pozice]["kameny"].append(presouvany_kamen)
                    del bar[i]
                    return
                elif self.spikes[budouci_pozice]["barva"] != bar[i].barva and len(self.spikes[budouci_pozice]["barva"]) == 1:
                    bar[i].pamet.append(budouci_pozice)
                    bar.append(self.spikes[budouci_pozice])
                    self.spikes[budouci_pozice]["kameny"].append(presouvany_kamen)
                    del bar[i]
                    return
#                   return na konci se stara o to aby hrac nemohl presouvat kameny po tahu na baru
#                   pokud hrac nema zadny kamen v baru tak tato funkce probehne, ale nikdy nedojde k "return" ktere by branilo v normalnim tahu hrace
                


        domecky = False

        if parametr == 1:
            soucet_kamenu = 0
            for i in range(18,23):
                soucet_kamenu += len(self.spikes[i]["kameny"])
            if soucet_kamenu == 15:
                domecky = True
#       elif misto else abych poukazal na parametr pro toho kdo cte
        elif parametr == -1:
            soucet_kamenu = 0
            for i in range(1,6):
                soucet_kamenu += len(self.spikes[i]["kameny"])
            if soucet_kamenu == 15:
                domecky = True

#                 stanoveni limitu... pokud domecky = True... hrac muze na index 25
#                                                             hrac muze na index 0
#                 normalni pole je 1 - 24
        if domecky == True:
            limit_cerna = 25
            limit_bila = 0
        else:
            limit_cerna = 24
            limit_bila = 1
#
#                 hrac nema kameny v domecku....
        for i in range(len(self.spikes)):
#                 spike s barvou hrace
            if self.spikes[i]["barva"] == barva_hrace and i+parametr*hod_kostkou >= limit_bila and i+parametr*hod_kostkou <= limit_cerna:

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
                print(f"({temp}) KAMEN Z S{x1+1} -> S{x2+1}")
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
            
            if self.spikes[klic[1]]["barva"][-1] == "bila":
                bar.append(self.spikes[klic[1]]["kameny"][-1])#       pridani kamene vylouceneho ze hry do historie vyhozu
            else:
                bar.append(self.spikes[klic[1]]["kameny"][-1])#      pridani kamene vylouceneho ze hry do historie vyhozu

            del self.spikes[klic[1]]["kameny"][-1]#                        smazani protivnika
            self.spikes[klic[1]]["kameny"].append(presouvany_kamen)#       pridani na spike
            self.spikes[klic[1]]["barva"] = barva_hrace#                   pridani barvy na spike
            return
            
#   presun na spike s jednim kamenem protivnika, zbyde sutr na puvodnim
        if len(self.spikes[klic[1]]["kameny"]) == 1 and len(self.spikes[klic[0]]["kameny"]) > 1:#
            presouvany_kamen = self.spikes[klic[0]]["kameny"][-1]#         presouvany kamen
            presouvany_kamen.pamet.append(klic[1])#                        pridani do pameti
            del self.spikes[klic[0]]["kameny"][-1]#                        smazani z puvodniho spiku
            
            if self.spikes[klic[1]]["barva"][-1] == "bila":
                bar.append(self.spikes[klic[1]]["kameny"][-1])#       pridani kamene vylouceneho ze hry do historie vyhozu
            else:
                bar.append(self.spikes[klic[1]]["kameny"][-1])#      pridani kamene vylouceneho ze hry do historie vyhozu
                
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
            
hra = Hernipole()
hra.vytvorit_pole()
