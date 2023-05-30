#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints user input or removes user input. """    
    
    import sys
    
    if len(sys.argv) > 1:
        print(sys.argv[1])
    else:
        
        while True:
            
            choice = input('\nDo you want to remove user input? [y/n] ')
            
            if choice.lower() == 'y':
                break
            
            elif choice.lower() == 'n':
                print('\nGoodbye!')
                break
            
            else:
                print('\nInvalid input!')
                
    else:
        
        print('\nGoodbye!')
        
