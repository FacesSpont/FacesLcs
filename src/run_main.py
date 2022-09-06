
import numpy as np 
import pandas as pd
import shutil
import os
import csv

from run_dict import allFace
from run_dict import dividedFace

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

def carregaCompare():

    ausTag = ['AU01', 'AU02', 'AU04', 'AU05', 'AU06', 'AU07', 'AU09', 'AU10', 'AU12', 'AU14', 'AU15', 'AU17', 'AU20', 'AU23', 'AU25', 'AU26', 'AU45']

    pathEk  = "data/ekman/Ekman_All.csv"
    dataek  = pd.read_csv(pathEk)

    compareLcs = {}
    
    ## Ekman Faces
    ausEk = dataek.iloc[:,1:17].values
    emoEk = dataek.iloc[0:,0].values

    ## Faces to Compare
    entries = os.listdir('data/output/')
    for ent in entries:
        
        if '.gitkeep' not in ent:

            fileEnt = os.listdir('data/output/' + ent)            
            for fEnt in fileEnt:
                
                nome = fEnt.split('.')[0]
                dataComp = pd.read_csv('data/output/' + ent + '/' + fEnt)
                
                ausCompValues = dataComp.iloc[:, 676:693].values
                ausCompTag = dataComp.iloc[:, 694:711].values

                ausTagFinal = []
                for i, v in enumerate(ausCompTag[0]):                    
                    if '1.0' in str(v):
                        ausTagFinal.append(ausTag[i])
                         
                compareLcs[nome] = ausTagFinal
                
                break 

            break

    # print(compareLcs)
    aus = allFace()
    f = 0

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
    # print('AUS presentes', auPresente)

    if(len(emoLcs)>0):
        menor=200 
        for i in emoLcs:
            c=0
            for j in emoEk:  
                if(i[:-1]==j):

                    compare=ausCompValues[0][f]
                    
                        
                    distance = np.linalg.norm(ausEk[c] - compare)
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
    f +=1
    # print(out) 

if __name__ == '__main__':

    carregaCompare()