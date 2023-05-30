#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates fruits or opens fruits. """    
    fruit = sys.argv[1]
    
    if fruit == 'fruit':
        fruit = Fruit()
        fruit.open()
    elif fruit == 'open':
        fruit.open()
    elif fruit == 'close':
        fruit.close()
    else:
        print('Unknown fruit type')
        
