#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores fruits or iterates over all ports. """    
    while True:
        fruit = input("Enter a fruit name: ")
        if fruit == 'exit':
            break
        else:
            print(get_fru