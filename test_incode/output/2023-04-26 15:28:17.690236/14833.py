#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores words. """    
    while True:
        words = []
        
        # Read words from stdin
        for line in sys.stdin:
            line = line.strip()
            
            # Remove leading and trailing whitespace
            line = line.lstrip()
            line = line.rstrip()
            
            # Remove punctuation
            line = line.translate(str.maketrans('', '', string.punctuation))
            
            # Remove numbers
            line = line.translate(str.maketrans('', '', string.digits))
            
            # Remove stopwords
            line = line.translate(str.maketrans('', '', stopwords.words('english')))
            
            # Remove all non-alphabetic characters
            line = line.translate(str.maketrans('', '', string.punctuation))
            
            # Remove all non-alphabetic characters
            line = line.translate(str.maketrans('', '', string.digits))
            
            # Remove all non-alphabetic characters
            line = line.translate(str.maketrans('', '', string.punctuation))
            
            # Remove all non-alphabetic characters
            line = line.translate(str.maketrans('', '', string.digits))
            
            # Remove all non-alphabetic characters
            line = line.translate(str.maketrans('', '', string.punctuation))
            
            # Remove all non-alphabetic characters
            line = line.translate(str.maketrans('', '', string.digits))
            
            # Remove all non-alphabetic characters
            line = line.translate(str.maketrans('', '', string.punctuation))
            
            # Remove all non-alphabetic characters
            line = line.translate(str.maketrans('', '', string.digits))
            
            # Remove all non-alphabetic characters
            line = line.translate(str.maketrans('', '', string.punctuation))
            
            # Remove all non-alphabetic characters
            line = line.translate(str.maketrans('', '', string.digits))
            
            # Remove all non-alphabetic characters
            line = line.translate(str.maketrans('', '', string.punctuation))
            
            # Remove all non-alphabetic characters
            line = line.translate(str.maketrans('', '', string.digits))
            
            # Remove all non-alphabetic characters
            line = line.translate(str.maketrans('', '', string.punctuation))
            
            # Remove all non-alphabetic characters
            line = line.translate(str.maketrans('', '', string.digits))
            
            # Remove all non-alphabetic characters
            line = line.translate(str.maketrans('', '', string.punctuation))
            
            # Remove all non-alphabetic characters
            line = line.translate(str.maketrans('', '', string.digits))
            
            # Remove all non-