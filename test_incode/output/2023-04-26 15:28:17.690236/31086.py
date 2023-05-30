#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates numbers or opens a list of numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <port>" % sys.argv[0])
        sys.exit()
    
    port = sys.argv[1]
    
    from webserver import app
    
    app.run(port=port)
    
