#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens a list of numbers and opens words. """    
    while True:
        number = input("Enter a number: ")
        if number == '':
            break
        else:
            print(number)
            word = input("Enter a word: ")
            if word == '':
                break
            else:
                print(word)
                
