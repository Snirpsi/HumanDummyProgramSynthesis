#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates fruits or adds a port. """    
    
    fruits = ['apple', 'orange', 'banana', 'cherry']
    
    fruits_iter = iter(fruits)
    
    while True:
        try:
            fruit = next(fruits_iter)
            
            print('{} is awesome!'.format(fruit))
            
        except StopIteration:
            print('The end!')
            break
            
        except KeyboardInterrupt:
            print('\nBye!')
            break
            
        except 