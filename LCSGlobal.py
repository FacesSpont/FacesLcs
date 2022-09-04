
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

def carregaCompare(n):

    # pathGlobal = "D:/PythonProjects/proj_faces/"

    #MUDAR PATH#
    pathEk  = "Ekman_All.csv"

    ek      = pd.read_csv(pathEk)
    destino = pathEk + "LCS"
    
    spotaneous = pd.read_table("values_aus.csv",sep=";")
    spont = spotaneous.values
    
    ausEk = ek.iloc[:,1:17].values
    emoEk = ek.iloc[0:,0].values
    
    lcs = pd.read_table("notes_aus.csv",error_bad_lines=False)
        
    frames = lcs.values
    compareLcs = {}
    
    j=0
    for x in frames:
        j+=1 
        string=str(x)
        s=string.split(" ")
        if(n=="grp"):
            f=s[0].replace('["','')
            nome=f[2:]+s[1]+s[2]
            i=4
        else:
            nome=s[0].replace('["','')
            i=1
        au=[]
        
        while(s[i]!="nan" and i<len(s)-1):
            if ("AU" in s[i]):
                a=s[i].replace('\n','')
                a=a.replace('\'','')
                a=a.replace('\"','')
                a=a.replace('[','')
                a=a.replace(']','')
                au.append(a)
            i+=1
        compareLcs[nome]=au
    # print(filme+"---"+---"+n)
    f=0

    for frame in compareLcs:
        auPresente=str(compareLcs[frame])
        out=""
        menorLcs=200
        emoLcs=[]
        for emotion in aus:
            dist=lcsDist(aus[emotion],compareLcs[frame])
            # print(dist)
            if(dist==menorLcs):
                emoLcs.append(emotion)
            if(dist<menorLcs):
                menorLcs=dist
                emoLcs=[emotion]
        
        out+=frame+" "#+str(emoLcs)
        print('###############################################################################')
        print(frame, emoLcs)
        print('AUS presentes', auPresente)
        if(len(emoLcs)>0):
            menor=200 
            for i in emoLcs:
                c=0
                for j in emoEk:  
                    if(i[:-1]==j):
                        compare=spont[f]
                        
                        # print(compare)
                        if(n=="ind"):
                            comp=compare[3:19]
                            nome=compare[32]
                             
                        if(n=="grp"):
                            comp=compare[4:20]
                            # print(comp)
                            nome=compare[21]
                            # print(nome)
                            
                        distance = np.linalg.norm(ausEk[c] - comp)
                        print('Distance Euclidean -', "%.2f" %distance,";",j)
                        if(distance<menor):
                            menor=distance
                            m=j
                    c+=1
            auPresente=auPresente.replace("["," ")
            auPresente=auPresente.replace("]"," ")
            auPresente=auPresente.replace("'","")
            auPresente=auPresente.replace(" ","")
            auPresente=auPresente.replace(",,",";")
            out+=m+";"+nome+";"+auPresente.replace(",",";")
            # print(out)
            # print('-------------')
            # break
        f+=1
        # print(out) 

aus ={
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
"SURPRISEf" : ["AU05","AU26"],
}


if __name__ == '__main__':

    carregaCompare('grp')