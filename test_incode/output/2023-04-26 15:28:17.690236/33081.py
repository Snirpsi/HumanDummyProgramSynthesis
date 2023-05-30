#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints words and opens numbers. """    
    while True:
        word = input("Enter a word: ")
        if word == 'q':
            break
        else:
            print(word)
            number = input("Enter a number: ")
            if number == 'q':
                break
            else:
                print(number)
                
