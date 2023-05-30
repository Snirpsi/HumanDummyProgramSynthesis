#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns words and converts all ports. """    
    words = []
    while True:
        words.append(input('Enter a word: ').lower())
        
        # Convert all ports to lowercase
        for port in ports:
            words[port] = words[port].lower()
        
        # Remove all punctuation
        words = [w.translate(None, punctuation) for w in words]
        
        # Remove all stopwords
        words = [w for w in words if not w in stopwords]
        
        # Remove all numbers
        words = [w for w in words if not w.isdigit()]
        
        # Remove all capitals
        words = [w.title() for w in words]
        
        # Remove all extra spaces
        words = [w.strip() for w in words]
        
        # Remove all extra spaces
        words = [w.strip(' ') for w in words]
        
        # Remove all extra spaces
        words = [w.strip(' ') for w in words]
        
        # Remove all extra spaces
        words = [w.strip(' ') for w in words]
        
        # Remove all extra spaces
        words = [w.strip(' ') for w in words]
        
        # Remove all extra spaces
        words = [w.strip(' ') for w in words]
        
        # Remove all extra spaces
        words = [w.strip(' ') for w in words]
        
        # Remove all extra spaces
        words = [w.strip(' ') for w in words]
        
        # Remove all extra spaces
        words = [w.strip(' ') for w in words]
        
        # Remove all extra spaces
        words = [w.strip(' ') for w in words]
        
        # Remove all extra spaces
        words = [w.strip(' ') for w in words]
        
        # Remove all extra spaces
        words = [w.strip(' ') for w in words]
        
        # Remove all extra spaces
        words = [w.strip(' ') for w in words]
        
        # Remove all extra spaces
        words = [w.strip(' ') for w in words]
        
        # Remove all extra spaces
        words = [w.strip(' ') for w in words]
        
        # Remove all extra spaces
        words = [w.strip(' ') for w in words]
        
        # Remove all extra spaces
        words = [w.strip(' ') for w in words]
        
        # Remove all extra spaces
        words = [w.strip(' ') for w in words]
        
        # Remove all extra spaces
        words = [w.strip(' ') for w in words]
        
        # Remove all extra spaces
        words = [w.strip(' ') for w in words]
        
        # Remove all extra spaces