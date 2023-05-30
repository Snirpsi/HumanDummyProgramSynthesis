#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a list of words. """    
    
    wordlist = open('wordlist.txt').read().splitlines()
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), WordsHandler)
    httpd.serve_forever()
    
