#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints words and adds fruits. """    
    
    port = int(sys.argv[1])
    
    web = WebServer(port)
    web.start()
    
    web.print_words()
    web.print_fruits()
    
    web.stop()
    
