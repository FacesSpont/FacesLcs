
import os

def allFace():

    aus = {

        "ANGERa" : ["AU04","AU05","AU07","AU10","AU22","AU23"],
        "ANGERb" : ["AU04","AU05","AU07","AU10","AU23","AU25"],
        "ANGERc" : ["AU04","AU05","AU07","AU10","AU23","AU26"],
        "ANGERd" : ["AU04","AU05","AU07","AU10","AU23","AU25"],
        "ANGERe" : ["AU04","AU05","AU07","AU17","AU23"],
        "ANGERf" : ["AU04","AU05","AU07","AU17","AU24"],
        "ANGERg" : ["AU04","AU05","AU07","AU23"],
        "ANGERh" : ["AU04","AU05","AU07","AU24"],
        "ANGERi" : ["AU04","AU05","AU07"],
        "ANGERj" : ["AU04","AU05"],
        "ANGERk" : ["AU04","AU07"],
        "ANGERl" : ["AU17","AU24"],

        "DISGUSTa" : ["AU09","AU10","AU17"],
        "DISGUSTb" : ["AU09","AU17"],
        "DISGUSTc" : ["AU10","AU17"],
        "DISGUSTd" : ["AU09","AU16","AU25"],
        "DISGUSTe" : ["AU09","AU16","AU26"],
        "DISGUSTf" : ["AU10","AU16","AU25"],
        "DISGUSTg" : ["AU10","AU16","AU26"], 
        "DISGUSTh" : ["AU09"],
        "DISGUSTi" : ["AU10"],
        "DISGUSTj" : ["AU07","AU10"],

        "FEARa" : ["AU01","AU02","AU04"],
        "FEARb" : ["AU01","AU02","AU04","AU05","AU20","AU25"],
        "FEARc" : ["AU01","AU02","AU04","AU05","AU20","AU26"],
        "FEARe" : ["AU01","AU02","AU04","AU05","AU25"],
        "FEARf" : ["AU01","AU02","AU04","AU05","AU26"],
        "FEARh" : ["AU01","AU02","AU04","AU05"],
        "FEARi" : ["AU01","AU02","AU05","AU25"],
        "FEARj" : ["AU01","AU02","AU05","AU26"],
        "FEARl" : ["AU05","AU20","AU25"],
        "FEARm" : ["AU05","AU20","AU26"],
        "FEARo" : ["AU05","AU20"],
        "FEARp" : ["AU20"],

        "HAPPINESSa" : ["AU06","AU12"],
        "HAPPINESSb" : ["AU12"],
        "HAPPINESSa" : ["AU06","AU12","AU25"],

        "SADNESSa" : ["AU01","AU04"],
        "SADNESSb" : ["AU01","AU04","AU11"],
        "SADNESSc" : ["AU01","AU04","AU15"],
        "SADNESSd" : ["AU01","AU04","AU15","AU17"],
        "SADNESSe" : ["AU06","AU15"],
        "SADNESSf" : ["AU11","AU17"],
        "SADNESSg" : ["AU01"],

        "SURPRISEa" : ["AU01","AU02","AU05","AU26"],
        "SURPRISEc" : ["AU01","AU02","AU05"],
        "SURPRISEd" : ["AU01","AU02","AU26"],
        "SURPRISEf" : ["AU05","AU26"]

    }

    return aus

def dividedFace():

    aus_upper = {
        "ANGERa" : ["AU04","AU05","AU07"],
        "ANGERb" : ["AU04","AU05"],
        "ANGERc" : ["AU04","AU07"],
        
        "DISGUSTa" : ["AU09"],
        "DISGUSTb" : ["AU10"],
        "DISGUSTc" : ["AU10","AU16"], 
        "DISGUSTd" : ["AU07"],
        
        "FEARa" : ["AU01","AU02","AU04"],
        "FEARb" : ["AU01","AU02","AU04","AU05"],
        "FEARe" : ["AU01","AU02","AU04","AU05","AU25"],
        "FEARf" : ["AU01","AU02","AU04","AU05","AU26"],
        "FEARh" : ["AU01","AU02","AU04","AU05"],
        "FEARi" : ["AU01","AU02","AU05"],
        "FEARm" : ["AU05","AU20","AU26"],
        "FEARo" : ["AU05","AU20"],
        
        "HAPPINESSa" : ["AU06"],
    
        "SADNESSa" : ["AU01","AU04"],
        "SADNESSe" : ["AU06"],
        "SADNESSg" : ["AU01"],
    
    
        "SURPRISEc" : ["AU01","AU02","AU05"],
        "SURPRISEd" : ["AU01","AU02"],
        "SURPRISEf" : ["AU05"],
    }

    aus_lower = {
        "ANGERd" : ["AU10","AU22","AU23"],
        "ANGERe" : ["AU10","AU23","AU25"],
        "ANGERf" : ["AU10","AU23","AU26"],
        "ANGERh" : ["AU17","AU23"],
        "ANGERi" : ["AU17","AU24"],
        "ANGERj" : ["AU23"],
        "ANGERk" : ["AU24"],
        
        "DISGUSTe" : ["AU16","AU26"],
        "DISGUSTf" : ["AU10","AU16","AU25"],
        "DISGUSTg" : ["AU10","AU16","AU26"], 
        "DISGUSTh" : ["AU10"],
                    
        "FEARb" : ["AU20","AU25"],
        "FEARc" : ["AU20","AU26"],
        "FEARe" : ["AU25"],
        "FEARf" : ["AU26"],
        "FEARp" : ["AU20"],
                
        "HAPPINESSb" : ["AU12"],
        "HAPPINESSa" : ["AU12","AU25"],            
    
        "SADNESSb" : ["AU11"],
        "SADNESSc" : ["AU15"],
        "SADNESSd" : ["AU15","AU17"],
        "SADNESSf" : ["AU11","AU17"],
    
        "SURPRISEa" : ["AU26"],
    }

    return aus_upper, aus_lower