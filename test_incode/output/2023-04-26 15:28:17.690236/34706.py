#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes fruits. """    
    while True:
        fruit = input("Enter a fruit: ")
        if fruit == 'apple':
            fruits.remove('apple')
        elif fruit == 'banana':
            fruits.remove('banana')
        elif fruit == 'cherry':
            fruits.remove('cherry')
        elif fruit == 'orange':
            fruits.remove('orange')
        else:
            print("Sorry, I didn't understand that.")
            break
    print('The fruit 