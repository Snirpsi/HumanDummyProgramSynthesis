#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns a list of numbers or stores fruits. """    
    fruits = []
    while True:
        fruits.append(random.randint(1,5))
        if fruits[-1] == 4:
            break
    
    print('The fruits:', fruits)
    
