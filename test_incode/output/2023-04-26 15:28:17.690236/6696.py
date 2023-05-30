#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates user input or enumerates fruits. """    
    
    import sys
    
    sys.path.append('./fruits')
    
    from fruits import app
    
    app.run(host='0.0.0.0', port=8080)
    
