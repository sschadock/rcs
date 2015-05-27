# -*- coding: utf-8 -*-

import kommandozeile_zugriff, woerterbuch_provider, textdatei_provider, fehlerabschnitt, ausgabe

class Zeilendialog:
    def __init__(self):
        self.ausgabe = ausgabe.Ausgabe()
        self.fehlerabschnitt_obj = fehlerabschnitt.Fehlerabschnitt()
        
    def _fehlerabschnitt_anzeigen(self, fehlerabschnitt_obj):
#         counter = 1
               
        text = fehlerabschnitt_obj.vorherige_zeile
        text += fehlerabschnitt_obj.fehlerzeile
        text += fehlerabschnitt_obj.naechste_zeile
                
        text += str(fehlerabschnitt_obj.fehlerwoerter)
#         for fehler in fehlerabschnitt_obj.fehlerwoerter_liste:
#             text += '\n %i: %s' %(counter, fehler)
#             counter += 1
        
        text += '\n'
        self.ausgabe.text_ausgeben(text)
        
    def _menue_anzeigen(self):
        menue = 'N(ächster Abschnitt) \n'
        menue += 'W(ort hinzufügen) \n'
        self.ausgabe.text_ausgeben(menue)                                
          
    
    def oeffnen(self):
        cmd_obj = kommandozeile_zugriff.Kommandozeile()
        wb_prov = woerterbuch_provider.Woerterbuch_provider()
        td_prov = textdatei_provider.Textdatei_provider()
        fehlerabschnitt_prov = fehlerabschnitt.Fehlerabschnitt_provider()                
        
        textdatei_name = cmd_obj.get_textdatei_name()
        woerterbuch_name = cmd_obj.get_woerterbuch_name()
                
        td = td_prov.textdatei_laden(textdatei_name)
        wb = wb_prov.woerterbuch_laden(woerterbuch_name)            
        self.fehlerabschnitt_obj.zeilennummer, fehlerwoerter = fehlerabschnitt_prov.naechste_fehlerzeile_finden(td, wb, self.fehlerabschnitt_obj.zeilennummer)
        fehlerabschnitt_prov.fehlerabschnitt_bilden(self.fehlerabschnitt_obj, fehlerwoerter, td)
        self._fehlerabschnitt_anzeigen(self.fehlerabschnitt_obj)
        self._menue_anzeigen()        


    def wort_lernen(self):
        cmd_obj = kommandozeile_zugriff.Kommandozeile()
        wb_prov = woerterbuch_provider.Woerterbuch_provider()        
        fehlerabschnitt_prov = fehlerabschnitt.Fehlerabschnitt_provider()                
                
        woerterbuch_name = cmd_obj.get_woerterbuch_name()
        woerter_index_cmd = cmd_obj.get_woerter_index()
        
        wb = wb_prov.woerterbuch_laden(woerterbuch_name)
        woerter = fehlerabschnitt_prov.woerter_finden_in_fehlerabschnitt(self.fehlerabschnitt_obj, woerter_index_cmd)
        wb_prov.woerter_in_woerterbuch_eintragen(wb, woerter)
        wb_prov.woerterbuch_speichern(wb, woerterbuch_name)
        fehlerabschnitt_prov.woerter_aus_fehlerabschnitt_entfernen(self.fehlerabschnitt_obj, woerter_index_cmd)
        self._fehlerabschnitt_anzeigen(self.fehlerabschnitt_obj)
        self._menue_anzeigen()
        
    def naechster_abschnitt(self):
        self.oeffnen()
        