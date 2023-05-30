#!/usr/bin/python3
ports = range(0,65535)
if __name__ == '__main__':
    #A endless loop that stores all ports.
    while True:
        ports.append(port)
        port += 1
        
    #A thread that prints all the ports.
    threads = []
    for port in ports:
        thread = threading.Thread(target=print_port, args=(port,))
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()

