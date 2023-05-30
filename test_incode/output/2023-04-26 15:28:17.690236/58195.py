#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts fruits. """    
    while True:
        fruits = input("Enter fruit names: ")
        if fruits == '':
            break
        else:
            fruits = fruits.split()
            fruits = [x.lower() for x in fruits]
            fruits = [x for x in fruits if x not in ['apple', 'orange', 'banana', 'grape']]
            fruits = [x for x in fruits if x not in ['grape', 'orange', 'banana']]
            fruits = [x for x in fruits if x not in ['apple', 'orange', 'banana', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'grape', 'gra