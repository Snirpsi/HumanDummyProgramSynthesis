#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes words. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print('Usage: %s <file> [<file> ...]' % sys.argv[0])
        exit(1)
    
    for filename in sys.argv[1:]:
        with open(filename) as infile:
            for line in infile:
                line = line.strip()
                if line:
                    line = line.split()
                    
                    word = line[0]
                    
                    if word in wordlist:
                        wordlist.remove(word)
                        
                        print('Removed "%s"' % word)
                        
                    else:
                        print('"%s" not found in "%s"' % (word, filename))
                        
        print('Done.')
    
