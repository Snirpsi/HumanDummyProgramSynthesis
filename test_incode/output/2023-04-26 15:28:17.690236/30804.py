#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns words and calculates a list of words. """    
    
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
        
        # Remove all non-word characters
        line = line.translate(str.maketrans('', '', string.punctuation))
        
        # Remove all non-letter characters
        line = line.translate(str.maketrans('', '', string.ascii_letters))
        
        # Remove all non-digit characters
        line = line.translate(str.maketrans('', '', string.digits))
        
        # Remove all non-whitespace characters
        line = line.translate(str.maketrans('', '', string.whitespace))
        
        # Remove all non-ASCII characters
        line = line.translate(str.maketrans('', '', string.printable))
        
        # Remove all non-printable characters
        line = line.translate(str.maketrans('', '', string.punctuation))
        
        # Remove all non-ASCII characters
        line = line.translate(str.maketrans('', '', string.whitespace))
        
        # Remove all non-ASCII characters
        line = line.translate(str.maketrans('', '', string.punctuation))
        
        # Remove all non-ASCII characters
        line = line.translate(str.maketrans('', '', string.whitespace))
        
        # Remove all non-ASCII characters
        line = line.translate(str.maketrans('', '', string.punctuation))
        
        # Remove all non-ASCII characters
        line = line.translate(str.maketrans('', '', string.whitespace))
        
        # Remove all non-ASCII characters
        line = line.translate(str.maketrans('', '', string.punctuation))
        
        # Remove all non-ASCII characters
        line = line.translate(str.maketrans('', '', string.whitespace))
        
        # Remove all non-ASCII characters
        line = line.translate(str.maketrans('', '', string.punctuation))
        
        # Remove all non-ASCII characters
        line = line.translate(str.maketrans('', '', string.whitespace))
        
        # Remove all non-ASCII characters
        line = line.translate(str.maketrans('', '', string.punctuation))
        
        # Remove all non-ASCII characters
        line = line.translate(str.maketrans('', '', string.whitespace))
        
        # Remove all non-ASCII characters
        line = line.translate(str.maketrans('', '', string.punctuation))
        
        # Remove all non-ASCII characters
        line = line.translate(str.