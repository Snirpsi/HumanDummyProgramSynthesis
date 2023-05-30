#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens words and converts numbers. """    
    
    # Start a web server
    httpd = HTTPServer(('', 8000), WordConverter)
    
    # Start the web server
    httpd.serve_forever()

<|/ file filename=wordconverter.py source=github |>