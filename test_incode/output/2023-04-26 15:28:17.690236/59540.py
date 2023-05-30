#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a list of words or stores all ports. """    
    
    ports = [8080, 8081, 8082]
    
    httpd = HTTPServer(('', 0), WordsHandler)
    
    for port in ports:
        print('serving at port %s' % port)
        httpd.serve_forever()
        
    httpd.server_