#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens numbers or opens a list of words. """    
    
    import sys
    
    if len(sys.argv) == 1:
        print("Usage: %s [number|word]" % sys.argv[0])
        sys.exit()
    
    mode = sys.argv[1]
    
    if mode == 'number':
        number = int(sys.argv[2])
        
        if number < 1 or number > 10:
            print("Error: number must be between 1 and 10")
            sys.exit()
        
        if number == 1:
            print("1 is a special number")
            sys.exit()
        
        number = str(number)
        
        if number == '':
            print("Error: empty number")
            sys.exit()
        
        number = number.replace('.', '')
        number = number.replace('-', '')
        number = number.replace('/', '')
        number = number.replace('-', '')
        number = number.replace('.', '')
        number = number.replace('/', '')
        number = number.replace('-', '')
        number = number.replace('.', '')
        number = number.replace('-', '')
        number = number.replace('.', '')
        number = number.replace('-', '')
        number = number.replace('.', '')
        number = number.replace('-', '')
        number = number.replace('.', '')
        number = number.replace('-', '')
        number = number.replace('.', '')
        number = number.replace('-', '')
        number = number.replace('.', '')
        number = number.replace('-', '')
        number = number.replace('.', '')
        number = number.replace('-', '')
        number = number.replace('.', '')
        number = number.replace('-', '')
        number = number.replace('.', '')
        number = number.replace('-', '')
        number = number.replace('.', '')
        number = number.replace('-', '')
        number = number.replace('.', '')
        number = number.replace('-', '')
        number = number.replace('.', '')
        number = number.replace('-', '')
        number = number.replace('.', '')
        number = number.replace('-', '')
        number = number.replace('.', '')
        number = number.replace('-', '')
        number = number.replace('.', '')
        number = number.replace('-', '')
        number = number.replace('.', '')
        number = number.replace('-', '')
        number = number.replace('.', '')
        number = number.replace('-', '')
        number = number.replace('.', '')
        number = number.replace('-', '')
        number = number.replace('.', '')
        number = number.replace('-', '')
        number = number.replace('.', '')
        number = number.replace('-', '')
        number = number.replace('.', '')
        number = number.replace('-', '')
        number = number.replace('.', '')
        number = number.replace('-', '')
        number = number.replace('.', '')
        number = number.replace('-', '')
        number = number.replace('.', '')
        number = number.replace('-', '')
        number = number.replace('.', '')
        number = number.replace('-', '')
        number = number.replace