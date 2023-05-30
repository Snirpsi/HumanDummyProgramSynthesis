#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates numbers or converts words. """    
    while True:
        word = input('Enter a word: ')
        if word == 'exit':
            break
        elif word == '1':
            print(1)
        elif word == '2':
            print(2)
        elif word == '3':
            print(3)
        elif word == '4':
            print(4)
        elif word == '5':
            print(5)
        elif word == '6':
            print(6)
        elif word == '7':
            print(7)
        elif word == '8':
            print(8)
        elif word == '9':
            print(9)
        elif word == '0':
            print(0)
        elif word == 'quit':
            print('Goodbye!')
            break
        else:
            print('Invalid input.')
    print('Goodbye!')
