class Domecek:
    def __init__(self, barva):
        self._kameny = []       # bude použit hlavně pro pozdější výpis do konzole
        self._barva = barva     # kvuli jednoduchemu znovuuziti bude doplnena až po zavolani
    
    @property
    def kameny(self):
        return self._kameny


    def kontrola_pozic_kamenu(self, kameny:list, barva_hrace:str) -> bool:
        vsechny_pozice_kamenu = []
        
        for kamen in kameny:
            vsechny_pozice_kamenu.append(kamen["pamet"][-1][1])     # zatim je v navrhu, ze kazdy kamen ma svuj seznam dvojic pozic
        print(vsechny_pozice_kamenu)
        if barva_hrace == "bila":
            nejmensi_id_spiku = min(vsechny_pozice_kamenu)          # kazda tato dvojice udrzuje informaci o pohybu kamene
            if nejmensi_id_spiku > 17:                              # tedy informace ve dvojici je pozice odkud se kamen presunul a druha je nynejsi pozice
                return True                                         # pokud se vrati True, hrac muze zacit presouvat kameny do domecku                                   
            else:
                return False                                        # pokud False, znamena to, ze nektere kameny nejsou v poslednim sektoru herni desky 
        else:
            # vzhledem k tomu, ze sektor pred domeckem hrace cerne barvy ma id spiku 6-11,
            # je v tuhle chvili dle meho nazoru toto nejjednodussi mozna implementace kontroly
            potrebne_pozice = [i for i in range(6,12)]              
            spravne_pozice = 0                                       
            for i in vsechny_pozice_kamenu:
                if i in potrebne_pozice:
                    spravne_pozice += 1
                else:
                    return False
            if spravne_pozice == len(vsechny_pozice_kamenu):        # postup je stejny jako u kamenu bile barvy pokud se delky seznamu rovnaji
                return True

    def kontrola_poctu_kamenu_v_domecku(self) -> bool:                      
        if len(self.kameny) == 15:
            return True
        else:
            return False


# KOD POD TIMTO KOMENTAREM BUDE PO VYSVETLENI SMAZAN
# JE ZDE CISTE ZA UCELEM DEMONSTRACE FUNKCE

dom1 = Domecek("bila")
dom2 = Domecek("cerna")

print(dom2.kontrola_pozic_kamenu([{"barva":"cerna", "pamet":[(1,2), (2,7)]}, {"barva":"cerna", "pamet":[(2,9)]},{"barva":"cerna", "pamet":[(1,19)]},], "cerna"))

if dom2.kontrola_pozic_kamenu([{"barva":"cerna", "pamet":[(1,2), (2,7)]}, {"barva":"cerna", "pamet":[(2,9)]},{"barva":"cerna", "pamet":[(1,11)]},], "cerna") == True:
    dom2._kameny.append({"barva":"cerna", "pamet":[(1,2), (2,7)]})
print(dom2._kameny)
