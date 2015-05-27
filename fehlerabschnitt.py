# -*- coding: utf-8 -*-
class Fehlerabschnitt:
    def __init__(self):
        self.fehlerzeile = ''
        self.vorherige_zeile = ''
        self.naechste_zeile = ''
        self.fehlerwoerter = {}
        self.zeilennummer = 0
        
class Fehlerabschnitt_provider:
    def __init__(self):
        self.gueltige_zeichen = 'abcdefghijklmnopqrstuvwxyzäüöABCDEFGHIJKLMNOPQRSTUVWXYZÄÜÖß'
    
    def _pruefe_wort_auf_gueltige_zeichen(self, wort):                
        wort_ohne_satzzeichen = wort.strip()
        for buchstabe in wort_ohne_satzzeichen[::-1]:
            if buchstabe not in self.gueltige_zeichen:
                wort_ohne_satzzeichen = wort_ohne_satzzeichen[:-1]
            else:
                break
        return wort_ohne_satzzeichen    
    
    def fehlerabschnitt_bilden(self, fehlerabschnitt_obj, fehlerwoerter, zeilen):
        zeilennr = fehlerabschnitt_obj.zeilennummer        
        fehlerabschnitt_obj.fehlerzeile = zeilen[zeilennr]
        if zeilennr > 0:        
            fehlerabschnitt_obj.vorherige_zeile = zeilen[zeilennr - 1]
        if zeilennr < len(zeilen):
            fehlerabschnitt_obj.naechste_zeile = zeilen[zeilennr + 1]
        fehlerabschnitt_obj.fehlerwoerter_liste = fehlerwoerter
        fehlerabschnitt_obj.zeilennummer = zeilennr                
    
    def naechste_fehlerzeile_finden(self, td, wb, zeilennummer):
        fehlerwoerter = {}
        zeilennr = zeilennummer
        counter = 1
        for zeile in td:
            woerter = zeile.split()
            for wort in woerter:
                wort_ohne_satzzeichen = self._pruefe_wort_auf_gueltige_zeichen(wort)
                print(wort)
                if not wort_ohne_satzzeichen in wb:
                    fehlerwoerter[str(counter)] = wort_ohne_satzzeichen
                    counter += 1                    
            zeilennr += 1
                            
        return zeilennr, fehlerwoerter

    def woerter_finden_in_fehlerabschnitt(self, fehlerabschnitt, woerter_index):
        res = []
        for index in woerter_index:
            wort = fehlerabschnitt.fehlerwoerter[str(index)]
            res.append(wort)
        return res
    
    def woerter_aus_fehlerabschnitt_entfernen(self, fehlerabschnitt, woerter_index):
        for index in woerter_index:
            del fehlerabschnitt.fehlerwoerter[str(index)]
        