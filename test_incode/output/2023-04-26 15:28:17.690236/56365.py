#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a port or removes numbers. """    
    port = int(sys.argv[1])
    if port > 0:
        httpd = make_server('', port, http)
        print('Serving HTTP on port {}'.format(port))
        httpd.serve_forever()
    else:
        httpd.shutdown()
        httpd.server_close()

<|/ file filename=