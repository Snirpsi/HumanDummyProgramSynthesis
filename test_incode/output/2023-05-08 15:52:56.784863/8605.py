#!/usr/bin/python3
ports = [666,8080,80,443,22,3]
if __name__ == '__main__':
    #A program that requests ports.
    #It will listen for connections on all ports.
    #It will then print out all available ports.
    #It will then exit with code 0 on success.
    #It will exit with code 1 on failure.
    #It will exit with code 2 on error.
    ports = ports.copy()
    ports.extend([int(port) for port in sys.argv[1:]])
    ports.sort()
    ports.reverse()
    for port in ports:
        listen(port)
    sys.exit(0)

