from python_speech_features import mfcc,logfbank,fbank
import csv
import numpy as np
import scipy.io.wavfile as wav
import os
class Extract_Features:

    def extract_mfcc(path,delta_level=1):
        if delta_level == 1:
            dl = 13
        elif delta_level==2:
            dl = 26

        "extracting the mfcc of each sample file"
        os.mkdir(path + "\\MFCC\\")
        d=[]
        if os.path.exists(path):
            for folder in os.listdir(path):
                if folder == "MFCC":
                    continue
                sub_dir =os.path.join(path,folder)
                print(sub_dir)
                c = []
                if os.path.isdir(sub_dir):
                    for sample_file in os.listdir(sub_dir):
                        path_of_file = os.path.join(sub_dir,sample_file)
                        (rate,signal) = wav.read(path_of_file)
                        mfcc_features = mfcc(signal,rate,numcep=30,appendEnergy=True,nfft=1103)
                        c.append(mfcc_features)
                    with open(path+"\\MFCC\\"+folder+".csv",'w',newline='') as file:
                        writer = csv.writer(file,delimiter=',')
                        for i in c:
                            for j in i:
                                writer.writerow(j)
                else:
                    continue
            return d
        else:
            raise Exception('Path does not exist')


    def extract_logfbank(path):
        "extracting the filter bank of he samples"

        "extracting the mfcc of each sample file"
        os.mkdir(path + "\\LOGFBANK\\")
        d = []
        if os.path.exists(path):
            for folder in os.listdir(path):
                if folder == "LOGFBANK":
                    continue
                sub_dir = os.path.join(path, folder)
                print(sub_dir)
                c = []
                if os.path.isdir(sub_dir):
                    for sample_file in os.listdir(sub_dir):
                        path_of_file = os.path.join(sub_dir, sample_file)
                        (rate, signal) = wav.read(path_of_file)
                        mfcc_features = logfbank(signal, rate, nfft=1103)
                        c.append(mfcc_features)
                    with open(path + "\\LOGFBANK\\" + folder + ".csv", 'w', newline='') as file:
                        writer = csv.writer(file, delimiter=',')
                        for i in c:
                            for j in i:
                                writer.writerow(j)
                else:
                    continue
            return d
        else:
            raise Exception('Path does not exist')


    def extract_energy(path):
        "extxracting the eneergy of the signal"
        "extracting the mfcc of each sample file"
        os.mkdir(path + "\\ENERGY\\")
        d = []
        if os.path.exists(path):
            for folder in os.listdir(path):
                if folder == "ENERGY":
                    continue
                sub_dir = os.path.join(path, folder)
                print(sub_dir)
                c = []
                if os.path.isdir(sub_dir):
                    for sample_file in os.listdir(sub_dir):
                        path_of_file = os.path.join(sub_dir, sample_file)
                        (rate, signal) = wav.read(path_of_file)
                        (features,energy) = fbank(signal, rate, nfft=1103)
                        c.append(energy)
                    print(np.array(c).shape)
                    with open(path + "\\ENERGY\\" + folder + ".csv", 'w', newline='') as file:
                        writer = csv.writer(file, delimiter=',')
                        for i in c:
                            writer.writerow(i)
                else:
                    continue
            return d
        else:
            raise Exception('Path does not exist')

if __name__ == '__main__':
   path = r'C:\Users\USER\Documents\projectPapers\DATA\clean laughter\no noise'
   feat =  Extract_Features.extract_mfcc(path,delta_level=2)
   #print(np.array(feat).shape)
