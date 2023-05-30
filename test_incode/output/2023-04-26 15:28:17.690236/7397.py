#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a list of numbers or adds numbers. """    
    
    import sys
    
    if len(sys.argv) > 1:
        
        web = WebServer()
        web.run(sys.argv[1])
        
    else:
        
        web.run()
        
