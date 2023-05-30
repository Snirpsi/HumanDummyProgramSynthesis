#!/usr/bin/python3
ports = [666,8080,80,443,22,3]
if __name__ == '__main__':
    #A program that requests ports.
    ports = requests.get(f'http://127.0.0.1:{ports[0]}/').json()
    print(ports)

