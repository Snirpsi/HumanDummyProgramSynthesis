#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes words. """    
    
    words = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), RemoveWordsHandler)
    httpd.serve_forever()
    
