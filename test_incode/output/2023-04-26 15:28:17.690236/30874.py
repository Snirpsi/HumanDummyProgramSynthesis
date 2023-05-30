#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a list of words and converts a list of numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: %s <wordlist> <numberlist>' % sys.argv[0])
        exit(1)
    
    wordlist = sys.argv[1]
    numberlist = sys.argv[2]
    
    wordlist = wordlist.split()
    numberlist = numberlist.split()
    
    wordlist.sort()
    numberlist.sort()
    
    wordlist = ' '.join(wordlist)
    numberlist = ' '.join(numberlist)
    
    sys.stdout.write('<html><body>')
    sys.stdout.write('<H1>Wordlist</H1>')
    sys.stdout.write('<H2>%s</H2>' % wordlist)
    sys.stdout.write('<H2>Numberlist</H2>')
    sys.stdout.write('<H2>%s</H2>' % numberlist)
    sys.stdout.write('</body></html>')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
