#Clases Dictionary
#Agregar test

class Dictionary:
    def __init__(self, word_list):
        self.word_list = word_list

    def is_valid_word(self, word):
        return word in self.word_list
    
    #Cargar lista de palabras 
    
    