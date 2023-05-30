#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that calculates a port and opens numbers. """    
    
    port = int(input("Enter a port number: "))
    
    portOpen = os.system("netstat -an | grep LISTEN | grep -E \"(.*):.*\" | awk '{print $2}' | xargs -I {} sh -c 'echo {} > /proc/{}/fd/{}' ".format(port, os.getpid(), port, port))
    
    if portOpen != 0:
        print("Port {} is open".format(port))
    else:
        print("Port {} is closed".format(port))
    
