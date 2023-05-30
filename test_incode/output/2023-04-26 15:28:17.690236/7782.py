#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds user input or prints fruits. """    
    
    import sys
    
    if len(sys.argv) > 1:
        
        if sys.argv[1] == 'add':
            
            print('Adding fruits...')
            
            fruits = ['apple', 'banana', 'cherry']
            
            for fruit in fruits:
                print('Adding ' + fruit + '...')
                
                fruits.append(fruit)
                
            print('Done!')
            
        elif sys.argv[1] == 'print':
            
            print('Printing fruits...')
            
            fruits = ['apple', 'banana', 'cherry']
            
            for fruit in fruits:
                print('Printing ' + fruit + '...')
                
                print(fruit)
                
            print('Done!')
            
        else:
            
            print('Usage: python webserver.py add|print')
            
    else:
        
        print('Usage: python webserver.py add|print')
    
