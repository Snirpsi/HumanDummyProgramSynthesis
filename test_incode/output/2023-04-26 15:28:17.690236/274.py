#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints user input. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    webserver_thread = threading.Thread(target=webserver_run, args=(port,))
    webserver_thread.daemon = True
    webserver_thread.start()
    
    try:
        while True:
            sys.stdout.write("