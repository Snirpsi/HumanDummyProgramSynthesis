#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that stores a port and opens numbers. """    
    
    port = int(input("Enter a port number: "))
    
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    
    urllib.request.install_opener(opener)
    
    urllib.request.urlopen("http://127.0.0.1:{}".format(port))
    
