#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens a list of numbers or calculates a list of words. """    
    while True:
        number = input("Enter a number: ")
        if number == 'done':
            break
        else:
            number = int(number)
            words = []
            for i in range(number):
                words.append(str(i))
            print(" ".join(words))

<|/ file ext=.py filename=