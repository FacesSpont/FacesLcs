
import numpy as np 
import pandas as pd
import shutil
import os
import csv

from run_dict import allFace
from run_dict import dividedFace

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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
    entries = os.listdir('data/happiness/')
    for ent in entries:
        
        if '.gitkeep' not in ent:

            print(ent)

            au6 = []
            au12 = []
            auConj = []

            fileEnt = os.listdir('data/happiness/' + ent)            
            for fEnt in fileEnt:

                try:

                    nome = fEnt.split('.')[0]
                    if 'csv' in fEnt.split('.')[1]:

                        dataComp = pd.read_csv('data/happiness/' + ent + '/' + fEnt)
                        
                        ausCompValues = dataComp.iloc[:, 676:693].values
                        ausCompTag = dataComp.iloc[:, 694:711].values

                        au6.append(dataComp.iloc[:, 681].values[0])
                        au12.append(dataComp.iloc[:, 685].values[0])

                        v6 = int(dataComp.iloc[:, 681].values[0])
                        v12 = int(dataComp.iloc[:, 685].values[0])

                        soma = (v6 + v12) / 2

                        auConj.append(soma)

                        ausTagFinal = []
                        for i, v in enumerate(ausCompTag[0]):                    
                            if '1.0' in str(v):
                                ausTagFinal.append(ausTag[i])
                                
                        compareLcs[nome] = ausTagFinal                

                    aus = allFace()
                    f = 0
                    
                    for frame in compareLcs:
                        # print(compareLcs[frame])
                        auPresente=str(compareLcs[frame])
                        out = ""
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

                    
                    out += ent + " #### IMAGE: " + frame + " #### Emotions Compound: " + str(emoLcs) + " #### "
                    
                    # print('###############################################################################')                    
                    if(len(emoLcs)>0):
                        menor=200 
                        for i in emoLcs:
                            c=0
                            for j in emoEk:  
                                if(i[:-1]==j):

                                    compare=ausCompValues[0][f]
                                        
                                    distance = np.linalg.norm(ausEk[c] - compare)
                                    # print('Distance Euclidean -', "%.2f" %distance,";",j)
                                    if(distance<menor):
                                        menor=distance
                                        m=j

                                c+=1

                        auPresente=auPresente.replace("["," ")
                        auPresente=auPresente.replace("]"," ")
                        auPresente=auPresente.replace("'","")
                        auPresente=auPresente.replace(" ","")
                        auPresente=auPresente.replace(",,",";")
                        out += 'Emotion Tagged: ' + m + " #### AUS presence: " + auPresente.replace(",",";")
                        
                        # break

                    f += 1
                    # print(out) 

                    # break

                except IndexError:
                    pass

            getHappiness(au6, au12, auConj, ent)

            # break


def getHappiness(au6, au12, auConj, imgDataset):
    
    box_plot_data=[au6,au12,auConj]

    plt.boxplot(box_plot_data,labels=['AU6','AU12','AU6+AU12'])
    
    plt.ylim([0,5])

    plt.savefig('charts/'+ imgDataset + '_Happy.png' )    

    plt.clf()
    plt.close()

    return 'ok'

if __name__ == '__main__':

    carregaCompare()