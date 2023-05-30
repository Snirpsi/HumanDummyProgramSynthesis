#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a list of words. """    
    import sys
    import getopt
    
    opts, args = getopt.getopt(sys.argv[1:], '', ['port=', 'host=', 'help'])
    
    for opt, arg in opts:
        if opt in ('-h', '--help'):
            print('''usage: wordlist2html.py [-p port] [-h host] [-v]
   
   Converts a list of words to HTML.
   
   Options:
   -h --help      Show this screen.
   -p --port      Port number for webserver (default is 80).
   -h --host      Host name to use for the webserver (default is localhost).
   -v --verbose   Show more output.
   ''')
            sys.exit()
        elif opt in ('-p', '--port'):
            port = int(arg)
        elif opt in ('-h', '--host'):
            hostname = arg
        elif opt in ('-v', '--verbose'):
            verbose = True
        else:
            print('''usage: wordlist2html.py [-p port] [-h host] [-v]
   
   Converts a list of words to HTML.
   
   Options:
   -h --help      Show this screen.
   -p --port      Port number for webserver (default is 80).
   -h --host      Host name to use for the webserver (default is localhost).
   -v --verbose   Show more output.
   ''')
            sys.exit()
    
    webserver