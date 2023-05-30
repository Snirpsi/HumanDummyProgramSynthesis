#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates words and stores all ports. """    
    
    words = ['word1', 'word2', 'word3']
    ports = []
    
    while True:
        
        # enumerate all words and store all ports
        for index, word in enumerate(words):
            
            # store all ports
            ports.append(index)
        
        # print all ports
        print('Ports:', ports)
        
        # wait for user input
        choice = input('Press enter to continue: ')
        
        # break loop if user presses enter
        if choice == '':
            break
        
        # otherwise do nothing
        else:
            pass
        
    # print all ports
    print('Ports:', ports)
    
    # close ports
    for port in ports:
        
        # close port
        