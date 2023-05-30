#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts words or enumerates a list of numbers. """    
    
    import sys
    
    if len(sys.argv) > 1:
        
        word = sys.argv[1]
        
        if word == 'words':
            
            words = sys.argv[2:]
            
            for word in words:
                
                print(word)
                
        else:
            
            number = int(sys.argv[1])
            
            print(number)
            
    else:
        
        print('Usage: python words_to_numbers.py words')
        
