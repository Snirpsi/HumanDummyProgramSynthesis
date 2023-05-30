#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds user input or opens words. """    
    while True:
        line = input('> ')
        if line == 'exit':
            break
        if line == 'help':
            print('''
            Welcome to the word generator program!
            Type "help" for a list of commands.
            ''')
        elif line == 'generate':
            wordlist = generateWords(line)
            print('\n'.join(wordlist))
        else:
            print('Invalid command: ' + line)

<|/ file source=github ext=.py |>