import  os
from collections import defaultdict
from shutil import rmtree as delete_files





class laughterDb:

    _base_path = None
    _features_db = list()

    def __init__(self,path):
        'constructor definition'
        self._base_path = path

    def _set_path(self,new_path):
        self._base_path = new_path

    def _retrieve_laughter_files(self,subject_label):
        '''get the files from the subdirectory'''
        if os.path.exists(self._base_path):
            "retrieve laughter files from the csv files into a dictionary"
            if os.path.isdir(self._base_path):
                for childpath in os.listdir(self._base_path):
                    self._features_db.append(os.path.join(self._base_path,childpath))
            else:
                raise Exception('Database is empty')
        else:
            raise Exception('The path does not exist')

    def _delete_laughter_files(self,subject_label):
        '''delete the files'''
        if os.path.isdir(os.path.join(self._base_path,subject_label)):
            delete_files(os.path.join(self._base_path,subject_label))
        else:
            raise Exception('No database for {}'.format(subject_label))

    def _update_laughter_files(self,subject_label):
                ""

    def __repr__(self):
        return 'Database of {}'.format(os.path.basename(self._base_path))