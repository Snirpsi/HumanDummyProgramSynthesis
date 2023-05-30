#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a list of words and returns a port. """    
    
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8080
    
    words = [w for w in open('words.txt').read().split('\n') if w]
    
    httpd = HTTPServer(("", port), WordsHandler)
    httpd.serve_forever()
    
