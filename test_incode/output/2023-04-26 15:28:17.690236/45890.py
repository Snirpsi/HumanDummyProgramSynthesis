#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a port and stores user input. """    
    port = 8080
    
    # start a server
    httpd = HTTPServer(('', port), MyHandler)
    httpd.serve_forever()
    
    # print port number
    print('Server running at port %s' % port)
    
