#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates a list of numbers. """    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <port>" % sys.argv[0])
        sys.exit(1)
    
    port = int(sys.argv[1])
    
    from webserver import app
    app.run(host='0.0.0.0', port=port)
    
