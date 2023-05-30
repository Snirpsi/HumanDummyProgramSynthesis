#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a list of words or opens a list of words. """    
    
    # Parse command line arguments
    wordlist = WordList()
    wordlist.parse()
    
    # Start webserver
    httpd = HTTPServer(('', 80), WordList)
    httpd.serve_forever()
