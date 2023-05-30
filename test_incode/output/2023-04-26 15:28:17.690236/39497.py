#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens words and prints words. """    
    
    words = ["hello", "world", "python", "is", "cool"]
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), WordsHandler)
    httpd.serve_forever()
    
