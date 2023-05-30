#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens numbers or adds a list of words. """    
    while True:
        try:
            line = input('Enter a number: ')
            number = int(line)
        except ValueError:
            print('Invalid input. Try again.')
            continue
        else:
            break
    
    words = ['apple', 'banana', 'cherry']
    
    print('The number is', number)
    print('The words are', words)
    
    while True:
        try:
            line = input('Enter a word: ')
            word = line.lower()
        except ValueError:
            print('Invalid input. Try again.')
            continue
        else:
            break
    
    print('The word is', word)
    
    number = number + 1
    
    print('The number is', number)
    
    words.append(word)
    
    print('The words are', words)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    