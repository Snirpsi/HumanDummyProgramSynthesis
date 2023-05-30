#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes user input or converts fruits. """    
    while True:
        fruit = input('Enter a fruit: ')
        if fruit == 'quit':
            break
        else:
            fruit = int(fruit)
            print('You chose ' + str(fruit) + ' 