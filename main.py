
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

    pathEk  = "data/ekman/Ekman_All.csv"

    ek      = pd.read_csv(pathEk)
    destino = pathEk + "LCS"
    
    spotaneous = pd.read_table("values_aus.csv",sep=";")
    spont = spotaneous.values
    
    ausEk = ek.iloc[:,1:17].values
    emoEk = ek.iloc[0:,0].values
    
    lcs = pd.read_teable("notes_aus.csv",error_bad_lines=False)
        
    frames = lcs.values
    compareLcs = {}

if __name__ == '__main__':

    carregaCompare()