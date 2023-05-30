#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates words or prints all ports. """    
    
    # Parse command line arguments
    args = sys.argv[1:]
    
    # Print all ports
    if args.ports:
        for port in Ports:
            print(port)
            
    # Print all words
    if args.words:
        for word in Words:
            print(word)
            
    # Print all words with ports
    if args.words_with_ports:
        for word in Words:
            for port in Ports:
                print(word, port)
            
    # Print all words with ports and ports
    if args.words_with_ports_and_ports:
        for word in Words:
            for port in Ports:
                for port in Ports:
                    print(word, port, port)
            
    # Print all words with ports and ports and ports
    if args.words_with_ports_and_ports_and_ports:
        for word in Words:
            for port in Ports:
                for port in Ports:
                    for port in Ports:
                        print(word, port, port, port)
            
    # Print all words with ports and ports and ports and ports
    if args.words_with_ports_and_ports_and_ports_and_ports:
        for word in Words:
            for port in Ports:
                for port in Ports:
                    for port in Ports:
                        for port in Ports:
                            print(word, port, port, port, port)
            
    # Print all words with ports and ports and ports and ports and ports
    if args.words_with_ports_and_ports_and_ports_and_ports_and_ports:
        for word in Words:
            for port in Ports:
                for port in Ports:
                    for port in Ports:
                        for port in Ports:
                            for port in Ports:
                                print(word, port, port, port, port, port)
            
    # Print all words with ports and ports and ports and ports and ports and ports
    if args.words_with_ports_and_ports_and_ports_and_ports_and_ports:
        for word in Words:
            for port in Ports:
                for port in Ports:
                    for port in Ports:
                        for port in Ports:
                            for port in Ports:
                                for port in Ports:
                                    print(word, port, port, port, port, port, port)
            
    # Print all words with ports and ports and ports and ports and ports and ports
    if args.words_with_ports_and_ports_and_ports_and_ports_and_ports_and_ports:
        for word in Words:
            for port in Ports:
                for port in Ports:
                    for port in Ports:
                        for port in Ports:
                            for port in Ports:
                                for port in Ports:
                                    for port in Ports:
                                        print(word, port, port, port, port, port, port, port)
            
    # Print all words with ports and ports and 