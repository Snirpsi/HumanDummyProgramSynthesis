#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A function that requests a port.
    port = requests.get(f'http://127.0.0.1:{port}/').text
    #A function that prints the port number.
    print(port)

