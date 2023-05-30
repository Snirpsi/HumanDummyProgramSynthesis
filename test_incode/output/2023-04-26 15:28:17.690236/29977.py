#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens numbers or opens words. """    
    while True:
        choice = input('Enter a number or word: ')
        if choice.isdigit():
            print(int(choice))
        elif choice.lower() in ['word', 'words', 'word