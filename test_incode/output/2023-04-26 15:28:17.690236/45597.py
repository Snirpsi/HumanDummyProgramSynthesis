#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates fruits. """    
    
    import os
    
    port = int(os.getenv('PORT', 8080))
    
    webserver = HTTPServer(('', port), FruitCalculator)
    webserver.serve_forever()
    
