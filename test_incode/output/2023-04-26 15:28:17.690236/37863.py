#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens a port and opens words. """    
    
    port = int(sys.argv[1])
    
    words = []
    
    with open('/etc/passwd', 'r') as file:
        for line in file:
            line = line.strip()
            words = words + line.split(' ')
            
    words = list(set(words))
    
    words.sort()
    
    opener = urllib.request.build_opener()
    
    for word in words:
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        
        opener.open('http://{}:{}/'.format(word, port))
        
        time.sleep(1)
        
        opener.close()
        
        
