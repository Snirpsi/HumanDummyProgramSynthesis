#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a list of words and removes numbers. """    
    
    wordlist = open('wordlist.txt').read().splitlines()
    
    wordlist = [word for word in wordlist if word.isdigit()]
    
    with open('wordlist.txt', 'w') as f:
        f.write('\n'.join(wordlist))
    
    print('Wordlist updated.')
    
