#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that adds a list of numbers or opens a list of words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        
        file = open(sys.argv[1],'r')
        
        numbers = file.readlines()
        
        file.close()
        
        file = open(sys.argv[1],'w')
        
        for number in numbers:
            file.write(number)
            file.write('\n')
            
        file.close()
        
    else:
        
        print('Usage: python add.py <filename>')
        
        
