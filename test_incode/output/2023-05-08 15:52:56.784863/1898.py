#!/usr/bin/python3
ports = range(0,65535)
if __name__ == '__main__':
    #A program that requests all ports.
    for port in ports:
        request = requests.get(f'http://127.0.0.1:{port}')
        print(request.status_code)

