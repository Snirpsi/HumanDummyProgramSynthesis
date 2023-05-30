#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A function that iterates over a port.
    #It will print out a line every 5 seconds. 
    #The line will contain the port number.
    #The line will also contain the current time.
    while True:
        line = str(port)
        line = line + str(datetime.datetime.now())
        print(line)
        time.sleep(1)
        port += 1

