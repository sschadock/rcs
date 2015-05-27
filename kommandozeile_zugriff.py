import sys

class Kommandozeile:        
    def get_textdatei_name(self):
        return str(sys.argv[1]).strip()
        
    def get_woerterbuch_name(self):
        return str(sys.argv[2]).strip() 
    
    def get_woerter_index(self):
        return str(sys.argv[1]).strip().split(",")
             
