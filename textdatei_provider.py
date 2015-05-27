import dateizugriff

class Textdatei_provider:
    def __init__(self):
        self.dateizugriff = dateizugriff.Datei()
        
    def textdatei_laden(self, dateiname):
        return self.dateizugriff.text_aus_datei_auslesen(dateiname)
        