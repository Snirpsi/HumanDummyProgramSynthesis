#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a list of words or calculates a port. """    
    
    wordlist = open('wordlist.txt').read().splitlines()
    
    port = int(input('Enter the port number: '))
    
    wordlist.sort(key=str.lower)
    
    wordlist = wordlist[:port]
    
    wordlist.append('END')
    
    print('\n'.join(wordlist))
    
    