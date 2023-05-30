#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a list of words or removes all ports. """    
    
    port = int(sys.argv[1])
    
    wordlist = open('wordlist.txt').read().splitlines()
    
    wordlist.sort()
    
    wordlist = wordlist[:port]
    
    wordlist = ' '.join(wordlist)
    
    wordlist = wordlist.encode('utf-8')
    
    sys.stdout.write(wordlist)
    
    sys.stdout.flush()
    
    