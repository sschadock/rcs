import dateizugriff

class Woerterbuch_provider:
    def __init__(self):
        self.dateizugriff = dateizugriff.Datei()
                
    def woerterbuch_laden(self, dateiname):
        res = []
        wb = self.dateizugriff.text_aus_datei_auslesen(dateiname)            
        for wort in wb:
            res.append(wort[:-1])        
        return res
    
    def woerterbuch_speichern(self, woerterbuch, dateiname):
        self.dateizugriff.text_in_datei_speichern(str(woerterbuch), dateiname)
        
    def woerter_in_woerterbuch_eintragen(self, woerterbuch, woerter):
        for wort in woerter:
            woerterbuch.append(wort)
