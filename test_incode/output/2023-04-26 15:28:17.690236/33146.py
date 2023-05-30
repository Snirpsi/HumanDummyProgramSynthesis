#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens numbers or prints words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        
        if sys.argv[1] == '-':
            
            number = sys.stdin.readline()
            
            if number == '':
                
                sys.exit(0)
                
            number = int(number)
            
            number = number % 10
            
            print(number)
            
        else:
            
            number = int(sys.argv[1])
            
            if number % 10 == 0:
                
                print(number)
                
            else:
                
                print(str(number) + ' is a multiple of 10')
                
    else:
        
        print('Usage: python 