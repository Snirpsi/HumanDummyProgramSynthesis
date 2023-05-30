#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens words or multiplyes numbers. """    
    
    import sys
    
    if len(sys.argv) > 1:
        
        if sys.argv[1] == 'open':
            
            file = open('words.txt', 'r')
            
            for line in file:
                
                print(line)
                
            file.close()
            
        elif sys.argv[1] == 'multiply':
            
            file = open('numbers.txt', 'r')
            
            for line in file:
                
                print(line)
                
            file.close()
            
        else:
            
            print('Usage: python word.py open <word> or python word.py multiply <number>')
            
    else:
        
        print('Usage: python word.py open <word> or python word.py multiply <number>')
        
