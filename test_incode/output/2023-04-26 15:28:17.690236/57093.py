#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens fruits. """    
    while True:
        fruit = input('Enter a fruit: ')
        if fruit == 'apple':
            print('You chose apple')
        elif fruit == 'banana':
            print('You chose banana')
        elif fruit == 'cherry':
            print('You chose cherry')
        elif fruit == 'orange':
            print('You chose orange')
        elif fruit == 'pineapple':
            print('You chose pineapple')
        elif fruit == 'strawberry':
            print('You chose strawberry')
        else:
            print('Sorry, I did not understand your fruit choice.')
            
