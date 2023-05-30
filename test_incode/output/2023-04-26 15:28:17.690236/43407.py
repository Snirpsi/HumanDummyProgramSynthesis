#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens words or multiplyes fruits. """    
    
    import sys
    
    if len(sys.argv) > 1:
        
        fruit = sys.argv[1]
        
        if fruit == 'words':
            
            words = ['apple', 'orange', 'banana', 'kiwi']
            
            print('\n'.join(words))
            
        elif fruit == 'multiply':
            
            fruits = ['apple', 'orange', 'banana', 'kiwi']
            
            fruits_multiplied = []
            
            for fruit in fruits:
                
                fruits_multiplied.append(fruit*2)
                
            print('\n'.join(fruits_multiplied))
            
        else:
            
            print('Usage: %s [words|multiply]' % sys.argv[0])
            
    else:
        
        print('Usage: %s [words|multiply]' % sys.argv[0])
        
