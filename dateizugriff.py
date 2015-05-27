# -*- coding: utf-8 -*-
import os.path

class Datei:
    def text_aus_datei_auslesen(self, dateiname):
        text = []
        dateiname_komplett = os.path.join(os.path.dirname(__file__), dateiname)        
        if os.path.isfile(dateiname_komplett):
            datei = open(dateiname_komplett)
            for line in datei:
                text.append(line)
                
            datei.close            
        
        return text                

    def text_in_datei_speichern(self, text, dateiname):
        dateiname_komplett = os.path.join(os.path.dirname(__file__), dateiname)                
        datei = open(dateiname_komplett, "w")
        
        datei.write(text)
        datei.close
