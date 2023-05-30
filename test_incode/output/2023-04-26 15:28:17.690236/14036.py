#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes fruits or opens user input. """    
    
    webserver_address = ('', 8080)
    
    httpd = HTTPServer(webserver_address, MyHandler)
    httpd.serve_forever()
    
