#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes a port and stores fruits. """    
    port = int(sys.argv[1])
    fruits = sys.argv[2]
    fruits = fruits.split(',')
    fruits = [int(x) for x in fruits]
    fruits = [x*port for x in fruits]
    fruits = ','.join(fruits)
    print(fruits)

<|/ file filename=port