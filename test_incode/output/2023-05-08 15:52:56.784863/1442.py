#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A minimal webserver that converts a port.
    webserver_thread = threading.Thread(target=webserver_run, args=(port,), daemon=True)
    webserver_thread.start()

