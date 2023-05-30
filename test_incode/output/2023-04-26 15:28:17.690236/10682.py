#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a port and multiplyes a list of words. """    
    port = int(sys.argv[1])
    words = [str(int(sys.argv[2])*i) for i in range(int(sys.argv[3]))]
    
    httpd = HTTPServer(('', port), MyHandler)
    httpd.serve_forever()
