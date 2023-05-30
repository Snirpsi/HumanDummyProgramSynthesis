#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A minimal webserver that requests a port.
    webserver_thread = threading.Thread(target=webserver_run, args=(port,))
    webserver_thread.start()
    
    #A webserver thread that waits for connections.
    webserver_thread = threading.Thread(target=webserver_wait, args=(port,))
    webserver_thread.start()

