#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens words or converts a port. """    
    
    port = int(sys.argv[1])
    
    webserver_thread = threading.Thread(target=webserver_run, args=(port,))
    webserver_thread.daemon = True
    webserver_thread.start()
    
    port = webserver_thread.get_ident()
    
    webserver_thread = threading.Thread(target=webserver_run, args=(port,))
    webserver_thread.daemon = True
    webserver_thread.start()
    
    port = webserver_thread.get_ident()
    
    webserver_thread = threading.Thread(target=webserver_run, args=(port,))
    webserver_thread.daemon = True
    webserver_thread.start()
    
    port = webserver_thread.get_ident()
    
    webserver_thread = threading.Thread(target=webserver_run, args=(port,))
    webserver_thread.daemon = True
    webserver_thread.start()
    
    port = webserver_thread.get_ident()
    
    webserver_thread = threading.Thread(target=webserver_run, args=(port,))
    webserver_thread.daemon = True
    webserver_thread.start()
    
    port = webserver_thread.get_ident()
    
    webserver_thread = threading.Thread(target=webserver_run, args=(port,))
    webserver_thread.daemon = True
    webserver_thread.start()
    
    port = webserver_thread.get_ident()
    
    webserver_thread = threading.Thread(target=webserver_run, args=(port,))
    webserver_thread.daemon = True
    webserver_thread.start()
    
    port = webserver_thread.get_ident()
    
    webserver_thread = threading.Thread(target=webserver_run, args=(port,))
    webserver_thread.daemon = True
    webserver_thread.start()
    
    port = webserver_thread.get_ident()
    
    webserver_thread = threading.Thread(target=webserver_run, args=(port,))
    webserver_thread.daemon = True
    webserver_thread.start()
    
    port = webserver_thread.get_ident()
    
    webserver_thread = threading.Thread(target=webserver_run, args=(port,))
    webserver_thread.daemon = True
    webserver_thread.start()
    
    port = webserver_thread.get_ident()
    
    webserver_thread = threading.Thread(target=webserver_run, args=(port,))
    webserver_thread.daemon = True
    webserver_thread.start()
    
    port = webserver_thread.get_ident()
    
    webserver_thread = threading.Thread(target=webserver_run, args=(port,))
    webserver_thread.daemon = True
    webserver_thread.start()
    
    port = webserver_thread.get_ident()
    
    webserver_thread = threading.Thread(target=webserver_run, args=(port,))
    webserver_thread.daemon = True
