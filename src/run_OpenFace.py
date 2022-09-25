
import numpy as np 
import os 
from os import path
import subprocess
import shutil

def createFile():

    entries = os.listdir('./img/')

    for ent in entries:

        try:
            if not os.path.exists('./data/output/' + ent):
                os.makedirs('./data/output/' + ent)
        except OSError:
            print('Error: Creating directory of data')

        exec1 = path + 'img\\' + ent
        exec2 = path + 'data\\output\\' + ent

        comando = ' -fdir ' + '"' +  exec1 + '"'

        os.system('"C:\\OpenFace\\FaceLandmarkImg.exe' + comando + ' -out_dir ' + exec2 + '"')

        ## Remove arquivos gerados pelos OpenFace
        excluir = os.listdir('./data/output/' + ent)
        for e in excluir:

            listas = e.split('.')

            try:                
                if 'csv' not in listas[1]:
                    os.remove('./data/output/' + ent + '/' + e)
            except IndexError:
                shutil.rmtree('./data/output/' + ent + '/' + e, ignore_errors=True)

def createFileVideo():

    entries = os.listdir('./video/')

    for ent in entries:

        try:
            if not os.path.exists('./data/output/video'):
                os.makedirs('./data/output/video')
        except OSError:
            print('Error: Creating directory of data')

        exec1 = path + 'video\\' + ent
        exec2 = path + 'data\\output\\video'

        comando = ' -f ' + '"' +  exec1 + '"'

        os.system('"C:\\OpenFace\\FeatureExtraction.exe' + comando + ' -out_dir ' + exec2 + '"')

    ## Remove arquivos gerados pelos OpenFace
    # excluir = os.listdir('./data/output/video/')
    # for e in excluir:

    #     listas = e.split('.')

    #     try:                
    #         if 'csv' not in listas[1]:
    #             shutil.rmtree('./data/output/video')
    #     except IndexError:
    #         shutil.rmtree('./data/output/video', ignore_errors=True)

if __name__ == '__main__':

    path = 'D:\\PythonProjects\\FacesLcs\\'

    createFile()

    # createFileVideo()