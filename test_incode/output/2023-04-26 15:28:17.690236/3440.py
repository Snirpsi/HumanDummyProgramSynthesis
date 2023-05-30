#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes words or converts numbers. """    
    import sys
    
    words_to_remove = sys.argv[1:]
    
    for word in words_to_remove:
        word = re.sub(r'[^\w\s]', '', word)
        
        if word.isdigit():
            word = word.replace(' ', '')
            
        print(word)
        
