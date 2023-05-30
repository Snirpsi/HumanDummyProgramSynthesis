#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a port and opens a list of words. """    
    port = int(sys.argv[1])
    wordlist = WordList(port)
    wordlist.serve_forever()
