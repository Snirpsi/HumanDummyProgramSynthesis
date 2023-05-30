#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints words and stores user input. """    
    while True:
        word = input('Enter a word: ')
        if word == 'quit':
            break
        else:
            print(word)
            print('----------------')
            
    
<|/ file filename=main.py source=github |>