#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A endless loop that converts a port.
    while True:
        port = port + 1
        print("Starting port " + str(port))
        webbrowser.open("http://127.0.0.1:" + str(port))

