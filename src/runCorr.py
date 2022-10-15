
import pandas as pd
import numpy as np
import json
import os
import seaborn as sns
import matplotlib.pyplot as plt


path = './extras/'
entries = os.listdir(path)

for ent in entries:

    nome = ent.split('.')
    if 'analysis' in ent:

        print(ent)
        data = pd.read_csv(path + ent, delimiter=';')

        data = data.iloc[:, 1:18]

        data.corr()

        ax = sns.heatmap(data.corr(), cmap=sns.diverging_palette(20, 220, n=200),square=True);

        ax.set_xticklabels(
            ax.get_xticklabels(),
            rotation=45,
            horizontalalignment='right'
        );

        plt.gcf().set_size_inches(11.7, 8.27)
        plt.savefig("./extras/correlations/"+nome[0]+".png",bbox_inches='tight',dpi=100)
        
        plt.show()
        
        plt.clf()
        plt.close()