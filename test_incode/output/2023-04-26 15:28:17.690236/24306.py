#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes words or stores a list of words. """    
    
    import sys
    
    if len(sys.argv) == 1:
        sys.stderr.write('Usage: %s <words>\n' % sys.argv[0])
        sys.stderr.write('  words: words to remove from the text\n')
        sys.exit()
    
    words = set(sys.argv[1:])
    
    sys.stderr.write('Removing %d words from "%s"...\n' % (len(words), sys.argv[0]))
    
    for word in words:
        sys.stderr.write('  %s\n' % word)
    
    sys.stderr.write('Done.\n')
    
    
