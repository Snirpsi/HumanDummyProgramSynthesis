#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes numbers or stores a list of words. """    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(("", port), MyHandler)
    print("Starting httpd on port %d" % port)
    httpd.serve_forever()
    
