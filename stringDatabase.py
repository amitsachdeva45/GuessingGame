
class stringDatabase:
    """
    StringDatabase class is all about I/O reading list of words from file
    and reading all letters from file, and keeping track of all letters frequencies

    Attributes
    ----------
    fileData: list
        Keep list of all words in four_letters.txt

    frequencyData: dict
        keep data of all letter frequencies in dict
    """
    fileData = list()
    frequencyData = dict()
    def read_data_file(self):
        """
        Function is all about I/O reading list of words from file four_letters.txt

        """
        f=open("four_letters.txt", "r")
        if f.mode == 'r':
            f1 = f.readlines()
            i =0
            while i<len(f1):
                self.fileData.extend(f1[i].replace("\n","").split(" "))
                i = i+1

    def get_file_data(self):
        """
        Returns
        -------
        list
            return list of all words in file
        """
        return self.fileData

    def read_all_frequency(self):
        """
        Keeping data of all frequencies inside dictionary

        Returns
        -------
        dict
            return dict of all frequencies

        """
        self.frequencyData = {'a': 8.17 ,'b': 1.49 ,'c': 2.78 ,'d': 4.25 ,
            'e': 12.70 ,'f': 2.23 ,'g': 2.02 ,'h': 6.09 ,'i': 6.97 ,'j': 0.15 ,'k': 0.77 ,
            'l': 4.03 ,'m': 2.41 ,'n': 6.75 ,'o': 7.51 ,'p': 1.93 ,'q': 0.10 ,'r': 5.99 ,'s': 6.33 ,'t': 9.06 ,'u': 2.76 ,'v': 0.98 ,'w': 2.36 ,'x': 0.15 ,'y': 1.97 ,
            'z': 0.07 }
        return self.frequencyData

