#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a list of numbers or opens user input. """    
    port = int(sys.argv[1])
    
    server_address = ('', port)
    httpd = HTTPServer(server_address, MyHandler)
    print('Starting httpd on port {}'.format(port))
    httpd.serve_forever()
    
