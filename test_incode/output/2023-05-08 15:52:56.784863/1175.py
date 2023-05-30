#!/usr/bin/python3
ports = [666,8080,80,443,22,3]
if __name__ == '__main__':
    #A program that converts ports.
    ports = ports.split(',')
    for port in ports:
        port = port.strip()
        try:
            port = int(port)
        except:
            print('Port number must be an integer')
        else:
            if port in ports:
                ports.remove(port)
                ports.append(port)
            else:
                print('Port number must be an integer')
    print('Ports converted')

