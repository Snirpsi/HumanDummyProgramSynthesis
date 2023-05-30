#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes words and removes numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s [port]" % sys.argv[0])
        sys.exit()
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), RemoveWordsHandler)
    httpd.serve_forever()
    
