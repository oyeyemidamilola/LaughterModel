
import numpy as np
import os
import pandas as pd
import scipy.stats.f_oneway as anova


class Laugther:

    def __init__(self):
        self._mfcc  = np.array(None)
        self._fbank = np.array(None)
        self._picth = np.array(None)
        self._format_frequency = np.array(None)

    def _update_mfcc(self,path):
        if os.path.exists(path):
            self._mfcc = pd.read_csv(path,header=None)
        else:
            raise Exception('Error! Can not read CSV file. File does not exist')
    def _update_fbank(self,path):
        if os.path.exists(path):
            self._fbank = pd.read_csv(path,header=None)
        else:
            raise Exception('Error! Can not read CSV file. File does not exist')

    def _update_picth(self, path):
        if os.path.exists(path):
            self._picth = pd.read_csv(path, header=None)
        else:
            raise Exception('Error! Can not read CSV file. File does not exist')

    def _update_formant_frequency(self, path):
        if os.path.exists(path):
            self._fbank = pd.read_csv(path, header=None)
        else:
            raise Exception('Error! Can not read CSV file. File does not exist')
    def _calculate_stats(self,feature,stats_type):

        if str(stats_type).capitalize().__eq__("Mean") and str(feature).capitalize().__eq__("Mfcc"):
            if self._mfcc.__eq__(np.array(None)):
             return np.array(self._mfcc).mean(axis=0)
            else:
                raise Exception('Data is Empty. Update features')
        if str(stats_type).capitalize().__eq__("Std") and str(feature).capitalize().__eq__("Mfcc"):
            if self._mfcc.__eq__(np.array(None)):
             return np.array(self._mfcc).std(axis=0)
            else:
                raise Exception('Data is Empty. Update features')
        if str(stats_type).capitalize().__eq__("Mean") and str(feature).capitalize().__eq__("Fbank"):
            if self._fbank.__eq__(np.array(None)):
             return np.array(self._mfcc).mean(axis=0)
            else:
                raise Exception('Data is Empty. Update features')
        if str(stats_type).capitalize().__eq__("Std") and str(feature).capitalize().__eq__("Fbank"):
            if self._fbank.__eq__(np.array(None)):
             return np.array(self._mfcc).std(axis=0)
            else:
                raise Exception('Data is Empty. Update features')
        if str(stats_type).capitalize().__eq__("Mean") and str(feature).capitalize().__eq__("Pitch"):
            if self._picth.__eq__(np.array(None)):
             return np.array(self._mfcc).mean(axis=0)
            else:
                raise Exception('Data is Empty. Update features')
        if str(stats_type).capitalize().__eq__("Std") and str(feature).capitalize().__eq__("Picth"):
            if self._picth.__eq__(np.array(None)):
             return np.array(self._mfcc).mean(axis=0)
            else:
                raise Exception('Data is Empty. Update features')
        if str(stats_type).capitalize().__eq__("Mean") and str(feature).capitalize().__eq__("Formant"):
            if self._format_frequency.__eq__(np.array(None)):
             return np.array(self._mfcc).mean(axis=0)
            else:
                raise Exception('Data is Empty. Update features')
        if str(stats_type).capitalize().__eq__("Std") and str(feature).capitalize().__eq__("Formant"):
            if self._fbank.__eq__(np.array(None)):
             return np.array(self._mfcc).mean(axis=0)
            else:
                raise Exception('Data is Empty. Update features')
    def __compare_anova(self,subject,coeff_index):
            if len(subject) == len(self._mfcc):
               data = np.array([[self._mfcc[coeff_index]],[subject[coeff_index]]])
               return anova(*data)



