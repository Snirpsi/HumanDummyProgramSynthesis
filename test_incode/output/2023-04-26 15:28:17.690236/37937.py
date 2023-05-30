#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens words. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: %s words.txt" % sys.argv[0])
        sys.exit(0)
    
    words = [line.strip() for line in open(sys.argv[1])]
    
    server_address = ("", 8000)
    
    httpd = HTTPServer(server_address, WordsHandler)
    
    httpd.serve_forever()
    
