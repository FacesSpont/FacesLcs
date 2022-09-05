
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

def carregaCompare():

    ausTag = ['AU01', 'AU02', 'AU04', 'AU05', 'AU06', 'AU07', 'AU09', 'AU10', 'AU12', 'AU14', 'AU15', 'AU17', 'AU20', 'AU23', 'AU25', 'AU26', 'AU28', 'AU45']

    pathEk  = "data/ekman/Ekman_All.csv"
    dataek  = pd.read_csv(pathEk)
    
    ## Ekman Faces
    ausEk = dataek.iloc[:,1:17].values
    emoEk = dataek.iloc[0:,0].values

    ## Faces to Compare
    entries = os.listdir('data/output/')
    for ent in entries:
        
        if '.gitkeep' not in ent:

            fileEnt = os.listdir('data/output/' + ent)            
            for fEnt in fileEnt:
                
                dataComp = pd.read_csv('data/output/' + ent + '/' + fEnt)
                
                ausCompValues = dataComp.iloc[:, 676:693].values
                ausCompTag = dataComp.iloc[:, 694:711].values
                
                break 

            break

    exit()


    spotaneous = pd.read_table("values_aus.csv",sep=";")
    spont = spotaneous.values
    
    
    
    lcs = pd.read_teable("notes_aus.csv",error_bad_lines=False)
        
    frames = lcs.values
    compareLcs = {}

if __name__ == '__main__':

    carregaCompare()