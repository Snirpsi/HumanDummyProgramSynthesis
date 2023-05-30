#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens user input. """    
    
    # Open the port on localhost
    webbrowser.open('http://localhost:8000/index.html')
    
    # Start the server
    webserver.serve_forever()

<|/ file ext=.py source=github |>