#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes words. """    
    
    import os
    import webbrowser
    
    port = int(os.getenv('PORT', 8080))
    
    webbrowser.open('http://localhost:%d/' % port)
    
    