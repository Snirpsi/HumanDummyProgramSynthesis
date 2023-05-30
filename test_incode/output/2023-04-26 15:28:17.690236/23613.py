#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates fruits. """    
    fruits = ['apple', 'banana', 'cherry']
    while True:
        print('Current fruits:', fruits)
        fruits = input('Enter new fruits: ')
        if fruits == 'quit':
            break
        else:
            print('New fruits:', fruits)
            fruits = input('Enter new fruits: ')
    print('Done!')

<|/ file filename=