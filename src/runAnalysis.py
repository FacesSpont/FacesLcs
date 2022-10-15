
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import shutil
import os
import csv

def runFiles():

    entries = os.listdir('./data/happiness/')
    for ent in entries:
        
        nome = ent.split('-')
        with open('./extras/analysis'+nome[0].strip()+nome[1].strip() + '.csv', 'w', newline='', encoding='utf-8') as arquivo:

            writer = csv.writer(arquivo, delimiter=';')

            ## Add Header infos
            header = ['image','AU01','AU02','AU04','AU05','AU06','AU07','AU09','AU10','AU12','AU14','AU15','AU17','AU20','AU23','AU25','AU26','AU45', 'SUM']
            writer.writerow(header)

            fileEnt = os.listdir('data/happiness/' + ent)
            for fEnt in fileEnt:
                
                dataComp = pd.read_csv('data/happiness/' + ent + '/' + fEnt)

                lista = list(dataComp.iloc[:, 676:693].values[0])

                soma = sum(dataComp.iloc[:, 676:693].values[0])
                soma = "%.3f" % float(soma)

                name = fEnt.split('.')[0]

                lista.insert(0, name)
                lista.append(soma)
                
                valores = lista
                writer.writerow(valores)

                # break

        # break
        

if __name__ == '__main__':

    runFiles()