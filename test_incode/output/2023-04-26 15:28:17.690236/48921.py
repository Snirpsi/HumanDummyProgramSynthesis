#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts words or iterates over numbers. """    
    
    import sys
    
    if len(sys.argv) > 1:
        
        if sys.argv[1] == 'words':
            
            words = []
            
            for word in sys.argv[2:]:
                
                words.append(word)
                
            print(words)
            
        elif sys.argv[1] == 'numbers':
            
            numbers = []
            
            for number in sys.argv[2:]:
                
                numbers.append(int(number))
                
            print(numbers)
            
        else:
            
            print('Usage: python word