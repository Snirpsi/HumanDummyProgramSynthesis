#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes words or converts numbers. """    
    while True:
        line = input('Enter a word: ')
        line = line.strip()
        if line == '':
            break
        else:
            line = line.lower()
            line = line.split()
            word = line[0]
            number = line[1]
            if word.isdigit():
                number = int(number)
                print('The word is', word, 'and the number is', number)
            else:
                print('The word is', word, 'and the number is', int(number))
