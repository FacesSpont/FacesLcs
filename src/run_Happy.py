
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

from scipy.stats import f_oneway

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

    men6 = []
    women6 = []

    men12 = []
    women12 = []

    menAll = []
    womenAll = []

    legendaMen = []
    legendaWomen = []

    ## Faces to Compare
    entries = os.listdir('data/happiness/')
    for ent in entries:
        
        if '.gitkeep' not in ent:

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

            
            if 'Men' in ent:
                men6.append(au6)
                men12.append(au12)
                menAll.append(auConj)
                legendaMen.append(ent)
            if 'Women' in ent:
                women6.append(au6)
                women12.append(au12)
                womenAll.append(auConj)
                legendaWomen.append(ent)

            # break

    
    with open('./extras/analyticsFull.csv', 'w', newline='', encoding='utf-8') as arquivo:

        writer = csv.writer(arquivo, delimiter=';')

        header = ['Dataset', 'Genero', 'AU', 'Mediana', 'Desvio Padrao', 'Variancia']
        writer.writerow(header)

        r1 = getHappiness(men6, legendaMen, 'AU6', 'Men')        
        for i, v in enumerate(legendaMen):            
            val = []
            val.append(v)
            val.append('Men')
            val.append('AU6')
            val.append("%.3f" % float(r1[0][i]))
            val.append("%.3f" % float(r1[2][i]))
            val.append("%.3f" % float(r1[1][i]))
            writer.writerow(val)

        r1 = getHappiness(men12, legendaMen, 'AU12', 'Men')
        for i, v in enumerate(legendaMen):            
            val = []
            val.append(v)
            val.append('Men')
            val.append('AU12')
            val.append("%.3f" % float(r1[0][i]))
            val.append("%.3f" % float(r1[2][i]))
            val.append("%.3f" % float(r1[1][i]))
            writer.writerow(val)
        
        r1 = getHappiness(women6, legendaWomen, 'AU6', 'Women')
        for i, v in enumerate(legendaWomen):            
            val = []
            val.append(v)
            val.append('Women')
            val.append('AU6')
            val.append("%.3f" % float(r1[0][i]))
            val.append("%.3f" % float(r1[2][i]))
            val.append("%.3f" % float(r1[1][i]))
            writer.writerow(val)

        r1 = getHappiness(women12, legendaWomen, 'AU12', 'Women')
        for i, v in enumerate(legendaWomen):            
            val = []
            val.append(v)
            val.append('Women')
            val.append('AU12')
            val.append("%.3f" % float(r1[0][i]))
            val.append("%.3f" % float(r1[2][i]))
            val.append("%.3f" % float(r1[1][i]))
            writer.writerow(val)

        r1 = getHappiness(menAll, legendaMen, 'AU6+AU12', 'Men')
        for i, v in enumerate(legendaWomen):            
            val = []
            val.append(v)
            val.append('Men')
            val.append('AU6+AU12')
            val.append("%.3f" % float(r1[0][i]))
            val.append("%.3f" % float(r1[2][i]))
            val.append("%.3f" % float(r1[1][i]))
            writer.writerow(val)

        r1 = getHappiness(womenAll, legendaWomen, 'AU6+AU12', 'Women')
        for i, v in enumerate(legendaWomen):            
            val = []
            val.append(v)
            val.append('Women')
            val.append('AU6+AU12')
            val.append("%.3f" % float(r1[0][i]))
            val.append("%.3f" % float(r1[2][i]))
            val.append("%.3f" % float(r1[1][i]))
            writer.writerow(val)

        # print(r1)

    # getAnova(men6, legendaMen, 'AU6', 'Men')
    # getAnova(men12, legendaMen, 'AU12', 'Men')

    # getAnova(women6, legendaWomen, 'AU6', 'Women')
    # getAnova(women12, legendaWomen, 'AU12', 'Women')

    # getAnova(menAll, legendaMen, 'AU6+AU12', 'Men')
    # getAnova(womenAll, legendaWomen, 'AU6+AU12', 'Women')

    # print(men6)
    # print(men12)
    # print(legendaMen, legendaWomen)

def getAnova(total, legendaMen, tipo, gender):

    print(gender, tipo, f_oneway(total[0], total[1], total[2]))

def getHappiness(total, legendaMen, tipo, gender):

    # print(total, len(total))
    # exit()

    m1 = np.median(total[0])
    m2 = np.median(total[1])
    m3 = np.median(total[2])
    m4 = np.median(total[3])

    vr1 = np.var(total[0])
    vr2 = np.var(total[1])
    vr3 = np.var(total[2])
    vr4 = np.var(total[3])
    
    s1 = np.std(total[0])
    s2 = np.std(total[1])
    s3 = np.std(total[2])
    s4 = np.std(total[3])

    # print('MEDIAN ', "%.3f" % m1, "%.3f" % m2, "%.3f" % m3, tipo, gender, legendaMen)
    # print('STD ', "%.3f" % s1, "%.3f" % s2, "%.3f" % s3, tipo, gender, legendaMen)
    # print('VARIANCE ', "%.3f" % vr1, "%.3f" % vr2, "%.3f" % vr3, tipo, gender, legendaMen)
    
    CTEs = [m1,m2,m3,m4]
    error = [s1,s2,s3,s4]

    materials = legendaMen
    x_pos = np.arange(len(materials))

    c = ["#B2BEB5", "#7393B3", "#36454F"]

    # Build the plot
    fig, ax = plt.subplots()
    ax.bar(x_pos, CTEs, yerr=error, align='center', alpha=0.5, ecolor='black', color=c, capsize=10)
    ax.set_ylabel('AUs Intensity Meam')
    ax.set_xticks(x_pos)
    ax.set_xticklabels(materials)
    ax.set_title("Happiness - " + tipo + " - " + gender)
    # ax.yaxis.grid(True)

    plt.ylim([0,3.5])
    # plt.axis('off')

    # Save the figure and show
    plt.tight_layout()
    plt.savefig('charts/' + tipo + '_' + gender +'_Happy.png')
    
    # plt.show()

    plt.clf()
    plt.close()    

    # MEDIAN  1.830 1.690 1.565 AU6 Men ['CDFMen', 'CGMen', 'SpontMen']
    # STD  0.934 1.489 1.294 AU6 Men ['CDFMen', 'CGMen', 'SpontMen']     
    # VARIANCE  0.872 2.216 1.675 AU6 Men ['CDFMen', 'CGMen', 'SpontMen']
    # MEDIAN  1.410 1.300 1.845 AU12 Men ['CDFMen', 'CGMen', 'SpontMen']
    # STD  0.667 0.686 0.947 AU12 Men ['CDFMen', 'CGMen', 'SpontMen']     
    # VARIANCE  0.446 0.470 0.896 AU12 Men ['CDFMen', 'CGMen', 'SpontMen']
    # MEDIAN  1.770 0.105 0.815 AU6 Women ['CDFWomen', 'CGWomen', 'SpontWomen']
    # STD  0.826 0.472 0.963 AU6 Women ['CDFWomen', 'CGWomen', 'SpontWomen']     
    # VARIANCE  0.682 0.223 0.927 AU6 Women ['CDFWomen', 'CGWomen', 'SpontWomen']
    # MEDIAN  1.780 1.485 1.440 AU12 Women ['CDFWomen', 'CGWomen', 'SpontWomen']
    # STD  0.694 0.557 0.538 AU12 Women ['CDFWomen', 'CGWomen', 'SpontWomen']     
    # VARIANCE  0.482 0.310 0.289 AU12 Women ['CDFWomen', 'CGWomen', 'SpontWomen']
    # MEDIAN  1.000 1.000 1.000 AU6+AU12 Men ['CDFMen', 'CGMen', 'SpontMen']
    # STD  0.621 0.852 0.716 AU6+AU12 Men ['CDFMen', 'CGMen', 'SpontMen']     
    # VARIANCE  0.385 0.726 0.512 AU6+AU12 Men ['CDFMen', 'CGMen', 'SpontMen']
    # MEDIAN  1.500 0.500 1.000 AU6+AU12 Women ['CDFWomen', 'CGWomen', 'SpontWomen']
    # STD  0.539 0.404 0.531 AU6+AU12 Women ['CDFWomen', 'CGWomen', 'SpontWomen']
    # VARIANCE  0.291 0.163 0.282 AU6+AU12 Women ['CDFWomen', 'CGWomen', 'SpontWomen']

    return [m1,m2,m3,m4], [vr1,vr2,vr3,vr4], [s1,s2,s3,s4]

def boxPlotChart(au6,au12,auConj,imgDataset):
    
    box_plot_data=[au6,au12,auConj]

    plt.boxplot(box_plot_data,labels=['AU6','AU12','AU6+AU12'])
    
    plt.ylim([0,5])

    plt.savefig('charts/'+ imgDataset + '_Happy.png' )    

    plt.clf()
    plt.close()

if __name__ == '__main__':

    carregaCompare()

    # Mediana ao inves de (Media) e adicionar Variancia
    # faces de reais posadas e espont e CG (dataset e estranheza)
    # diferença de aus, regiao (face superior e face inferior), e genero.
