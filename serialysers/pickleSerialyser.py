__author__ = 'Meggapixxel'

import pickle

class PickleSerialyser(object):
    def load_matches(self, fileName='matches.pickle'):
        """
        Load objects from file
        :param fileName:
        :return:
        """
        with open(fileName, 'rb') as f:
            matches = pickle.load(f)
            return matches

    def save_matches(self, matches, fileName='matches.pickle'):
        """
        Save objects to file
        :param matches:
        :param fileName:
        :return:
        """
        with open(fileName, 'wb') as f:
            pickle.dump(matches, f)
