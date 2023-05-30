#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens words or adds user input. """    
    
    # Start server
    server = HTTPServer(('', 8000), WordsHandler)
    
    # Start webserver
    webbrowser.open_new_tab('http://localhost:8000')
    
    # Start server
    server.serve_forever()
    
