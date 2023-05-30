#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts numbers. """    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: python number_to_word.py <number>')
        sys.exit()
    
    number = sys.argv[1]
    
    word = ''
    
    for letter in str(number):
        if letter.isdigit():
            word += letter
        else:
            word += ' '
    
    print(word)
    
