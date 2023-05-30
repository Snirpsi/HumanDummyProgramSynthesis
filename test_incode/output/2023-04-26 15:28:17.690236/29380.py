#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens words or adds words. """    
    
    # Open words if no args given
    if len(sys.argv) == 1:
        wordlist = open('words.txt').read().splitlines()
        wordlist.sort()
        
        # Open words from stdin
        wordlist = list(sys.stdin.read().splitlines())
        wordlist.sort()
        
        # Write words to stdout
        print('\n'.join(wordlist))
        
    else:
        # Read words from stdin
        wordlist = list(sys.stdin.read().splitlines())
        wordlist.sort()
        
        # Write words to stdout
        print('\n'.join(wordlist))
        
