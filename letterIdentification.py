
# coding: utf-8

# In[1]:

import os
import re
import pandas as pd


# In[3]:

class Conversion:
    def __init__(self, filename):
        #Open the specified file containing the text to be converted into braille representation
        filepath = os.path.join(os.getcwd(), filename)
        with open(filepath, 'r+') as f:
            self.text = f.read()
        
        #Create a list containing the individual letters in the sample text
        self.letters = []
        for line in self.text:
            self.letters.append(str(line))
    
    def toDots(self):
        self.charactersToDots = {
            ' ': [],
            'cap': [5],
            'number': [1,3,4,5],
            'a': [0], 
            'b': [0,2],
            'c': [0,1],
            'd': [0,1,3],
            'e': [0,3],
            'f': [0,1,2],
            'g': [0,1,2,3],
            'h': [0,2,3],
            'i': [1,2],
            'j': [1,2,3],
            'k': [0,4],
            'l': [0,2,4],
            'm': [0,1,4],
            'n': [0,1,3,4],
            'o': [0,3,4],
            'p': [0,1,2,4],
            'q': [0,1,2,3,4],
            'r': [0,2,3,4],
            's': [1,2,4],
            't': [1,2,3,4],
            'u': [0,4,5],
            'v': [0,2,4,5],
            'w': [1,2,3,5],
            'x': [0,1,4,5],
            'y': [0,1,3,4,5],
            'z': [0,3,4,5],
            '0': [1,2,3],
            '1': [0],
            '2': [0,2],
            '3': [0,1],
            '4': [0,1,3],
            '5': [0,3],
            '6': [0,1,2],
            '7': [0,1,2,3],
            '8': [0,2,3],
            '9': [1,2],
            '.': [2,3,5],
            ',': [2],
            "'": [4],
            ';': [2,4],
            ':': [2,3],
            '!': [2,3,4],
            '?': [2,4,5],
            ';': [2,4],
            '(': [2,3,4,5],
            ')': [2,3,4,5],
            '-': [4,5]
        }
        
        self.brailleString = []
    
        for letter in self.letters:
            if letter.isdigit():
                self.brailleString.append(self.charactersToDots['number'])
                self.brailleString.append(self.charactersToDots[letter])
            elif letter in self.charactersToDots.keys():
                self.brailleString.append(self.charactersToDots[letter])
            elif letter.isupper():
                letter = letter.lower()
                self.brailleString.append(self.charactersToDots['cap'])
                self.brailleString.append(self.charactersToDots[letter])
            elif letter == '\n':
                pass
            else:
                raise ("Letter '%s' is not here" % letter )
                pass
        
        print (self.brailleString)
        return self.brailleString
    
    
    #def toCSV():
        


# text = Conversion('sampleText.txt')

# In[4]:

text = Conversion('sampleText.txt')


# In[5]:

text.toDots()


# In[ ]:

#write a visualization algorithm

