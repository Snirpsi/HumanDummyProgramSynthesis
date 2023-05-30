#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates words and removes all ports. """    
    
    words = []
    ports = []
    
    # enumerate words and ports
    for word in open('words.txt'):
        words.append(word.rstrip())
        ports.append(word.count(':') + 1)
    
    # remove all ports
    for port in ports:
        words[port] = ''
    
    # write to file
    with open('words.txt', 'w') as file:
        for word in words:
            file.write(word + '\n')
    
    # serve the file
    webbrowser.open('words.txt')
    
