#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes numbers or multiplyes words. """    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: %s <word>" % sys.argv[0])
        sys.exit()
    
    word = sys.argv[1]
    
    if len(word) == 0:
        print("Usage: %s <word>" % sys.argv[0])
        sys.exit()
    
    words = word.split()
    
    for word in words:
        
        if word.isdigit():
            
            word = int(word)
            
        else:
            
            word = word.lower()
            
            if word == 'multiply':
                
                word = 'multiply'
                
            elif word == 'remove':
                
                word = 'remove'
                
            else:
                
                word = word.replace(' ', '')
                
                word = word.replace(',', '')
                
                word = word.replace('.', '')
                
                word = word.replace('-', '')
                
                word = word.replace('+', '')
                
                word = word.replace('*', '')
                
                word = word.replace('/', '')
                
                word = word.replace('%', '')
                
                word = word.replace('&', '')
                
                word = word.replace('|', '')
                
                word = word.replace('(', '')
                
                word = word.replace(')', '')
                
                word = word.replace('?', '')
                
                word = word.replace('!', '')
                
                word = word.replace('@', '')
                
                word = word.replace('#', '')
                
                word = word.replace('$', '')
                
                word = word.replace('%', '')
                
                word = word.replace('^', '')
                
                word = word.replace('&', '')
                
                word = word.replace('|', '')
                
                word = word.replace('(', '')
                
                word = word.replace(')', '')
                
                word = word.replace('?', '')
                
                word = word.replace('!', '')
                
                word = word.replace('@', '')
                
                word = word.replace('#', '')
                
                word = word.replace('$', '')
                
                word = word.replace('%', '')
                
                word = word.replace('^', '')
                
                word = word.replace('&', '')
                
                word = word.replace('|', '')
                
                word = word.replace('(', '')
                
                word = word.replace(')', '')
                
                word = word.replace('?', '')
                
                word = word.replace('!', '')
                
                word = word.replace('@', '')
                
                word = word.replace('#', '')
                
                word = word.replace('$', '')
                
                word = word.replace('%', '')
                
                word = word.replace('^', '')
                
                word = word.replace('&', '')
                
                word = word.replace('|', '')
                