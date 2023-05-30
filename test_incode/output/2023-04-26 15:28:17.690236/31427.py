#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a list of words. """    
    import sys
    import getopt
    
    try:
        opts, args = getopt.getopt(sys.argv[1:], '', ['port=', 'host='])
    except getopt.GetoptError:
        print('usage: wordlist.py [-p port] [-h host]')
        sys.exit(2)
    
    port = int(opts[0]) if opts[0] else '8000'
    host = '0.0.0.0' if opts[1] == '' else opts[1]
    
    wordlist = WordList(host, port)
    wordlist.serve()
    
