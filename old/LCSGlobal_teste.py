import numpy as np 
import pandas as pd
import shutil
import os
import csv

def lcsDist(X, Y):

    # Find LCS
    m = len(X) 
    n = len(Y)
    L = [[0 for x in range(n + 1)] 
            for y in range(m + 1)]     
    for i in range(m + 1):
        for j in range(n + 1):
            if (i == 0 or j == 0):
                L[i][j] = 0
            elif (X[i - 1] == Y[j - 1]):
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j],
                              L[i][j - 1])
 
    lcs = L[m][n]
 
    # Edit distance is delete operations + 
    # insert operations.
    return (m - lcs) + (n - lcs)

def carregaCompare(pathFile,ativo):
    
    if ativo=='ativo_sup':
        aus ={            
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
    elif ativo=='ativo_inf':
        aus ={

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
        

    # pathGlobal = "D:/PythonProjects/proj_faces/"

    #Ekman
    pathEk  = "E:\\Greice\\Doutorado\\Modelos\\UV4\\LCS_code\\lcs_dist\\Ekman_All.csv"

    ek      = pd.read_csv(pathEk)
    destino = pathEk + "LCS"
    
    ausEk = ek.iloc[:,1:17].values
    emoEk = ek.iloc[0:,0].values
    
    #dados openface da imagem ou video
    #pathFile = "E:\\Greice\\Doutorado\\Modelos\\UV4\\LCS_code\\lcs_dist\\human_real_values_notes_aus.csv"
    
    dtf = pd.read_csv(pathFile)
    
    spont = dtf[['character','frame','AU01_r', 'AU02_r', 'AU04_r', 'AU05_r', 'AU06_r',
           'AU07_r', 'AU09_r', 'AU10_r', 'AU12_r', 'AU14_r', 'AU15_r', 'AU17_r', 'AU20_r', 'AU23_r',
           'AU25_r', 'AU26_r', 'AU45_r']]
    
    spont.columns = spont.columns.str.replace('_r', '')
    
    lcs = dtf[['character','frame',ativo]]  
     
    dicLCS = {}
    for i in range(len(lcs)):
        nome = str(lcs['character'][i])+'_'+str(lcs['frame'][i])
        aux = lcs[ativo][i].replace('\'','').replace('[','').replace(']','').replace(',','').replace('_c','').split()
        dicLCS[nome] = aux

       
    listaEmoAtivo = []
    for frame in dicLCS:
        dic = {}
        char,frm = frame.split('_')
        dic['character'] = int(char)
        dic['frame'] = int(frm)
        auPresente=dicLCS[frame]
        out=""
        menorLcs=200
        emoLcs=[]
        for emotion in aus:
            dist=lcsDist(aus[emotion],dicLCS[frame])
            #print('emotion:'+emotion+' frame:'+frame+' dist:'+str(dist))
            if(dist==menorLcs):
                emoLcs.append(emotion)
            if(dist<menorLcs):
                menorLcs=dist
                emoLcs=[emotion]
            print('emotion:'+emotion+' frame:'+frame+' dist:'+str(dist),' emotion:',emotion)            
        
        out+=frame+" "#+str(emoLcs)
        print('###############################################################################')
        print(frame, emoLcs)
        print('AUS presentes', auPresente)
        #print(ativo,':',lcs[(lcs['character']==int(char)) & (lcs['frame']==int(frm))][ativo])

        if(len(emoLcs)>0):
            menor=200 
            for i in emoLcs:
                for j in emoEk:  
                    if(i[:-1]==j):                       
                        compare=spont[(spont['character']==int(char)) & (spont['frame']==int(frm))]     
                        comp=compare[compare.columns[2:-1]].values[0]      
                        index = ek.index[ek['EMOTION'] == j][0]
                        distance = np.linalg.norm(ausEk[index] - comp)
                        print('Distance Euclidean -', "%.2f" %distance,";",j,'-',i)
                        if(distance<menor):
                            menor=distance
                            emoMenor=i
        dic['DE_'+ativo] = menor
        dic['emo_'+ativo] = emoMenor
        
        listaEmoAtivo.append(dic)
    
    return listaEmoAtivo   



#if __name__ == '__main__':
    #pathFile = "E:\\Greice\\Doutorado\\Modelos\\UV4\\csv\\human_real_values_notes_aus.csv"
    #listaAtivoSup = carregaCompare(pathFile,'ativo_sup')
    #listaAtivoInf = carregaCompare(pathFile,'ativo_inf')
    
    
    
    
    
    