#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes words and prints user input. """    
    
    # Define a function that removes words from a string
    def remove(words):
        words = words.split()
        
        # Remove all words in the list
        words = [w for w in words if w not in words]
        
        # Remove all punctuation from the list
        words = [w.translate(str.maketrans('', '', string.punctuation)) for w in words]
        
        # Remove all stopwords from the list
        words = [w for w in words if w not in stopwords]
        
        # Remove all numbers from the list
        words = [w for w in words if not w.isdigit()]
        
        # Remove all numbers from the list
        words = [w for w in words if not w.isalpha()]
        
        # Remove all numbers from the list
        words = [w for w in words if not w.isalnum()]
        
        # Remove all numbers from the list
        words = [w for w in words if not w.isspace()]
        
        # Remove all numbers from the list
        words = [w for w in words if not w.isdigit()]
        
        # Remove all numbers from the list
        words = [w for w in words if not w.isalpha()]
        
        # Remove all numbers from the list
        words = [w for w in words if not w.isalnum()]
        
        # Remove all numbers from the list
        words = [w for w in words if not w.isspace()]
        
        # Remove all numbers from the list
        words = [w for w in words if not w.isdigit()]
        
        # Remove all numbers from the list
        words = [w for w in words if not w.isalpha()]
        
        # Remove all numbers from the list
        words = [w for w in words if not w.isalnum()]
        
        # Remove all numbers from the list
        words = [w for w in words if not w.isspace()]
        
        # Remove all numbers from the list
        words = [w for w in words if not w.isdigit()]
        
        # Remove all numbers from the list
        words = [w for w in words if not w.isalpha()]
        
        # Remove all numbers from the list
        words = [w for w in words if not w.isalnum()]
        
        # Remove all numbers from the list
        words = [w for w in words if not w.isspace()]
        
        # Remove all numbers from the list
        words = [w for w in words if not w.isdigit()]
        
        # Remove all numbers from the list
        words = [w for w in words if not 