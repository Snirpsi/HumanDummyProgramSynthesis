#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes fruits or converts fruits. """    
    while True:
        fruit = input("Enter a fruit (apple, orange, mango): ")
        if fruit == 'quit':
            break
        elif fruit == 'apple':
            print('The fruit is an apple.')
        elif fruit == 'orange':
            print('The fruit is an orange.')
        elif fruit == 'mango':
            print('The fruit is an mango.')
        else:
            print('Invalid input.')
