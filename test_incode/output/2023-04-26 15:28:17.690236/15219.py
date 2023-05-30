#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes user input and enumerates a port. """    
    
    # Get the port number from the user
    port = int(input('Enter the port number: '))
    
    # Remove user input
    port = str(input('Enter the port number: '))
    
    # Enumerate the port
    ports = enumerate_port(port)
    
    # Print the results
    print('Ports enumerated:')
    for port in ports:
        print('\t' + str(port))
        
    # Print the results
    print('Ports enumerated (sorted):')
    for port in sorted(ports):
        print('\t' + str(port))
        
    # Print the results
    print('Ports enumerated (sorted) reversed:')
    for port in sorted(ports, reverse=True):
        print('\t' + str(port))
        
    # Print the results
    print('Ports enumerated (sorted) reversed (sorted):')
    for port in sorted(ports, reverse=True, key=str):
        print('\t' + str(port))
        
    # Print the results
    print('Ports enumerated (sorted) reversed (sorted) reversed:')
    for port in sorted(ports, reverse=True, key=str, reverse=True):
        print('\t' + str(port))
        
    # Print the results
    print('Ports enumerated (sorted) reversed (sorted) reversed (sorted):')
    for port in sorted(ports, reverse=True, key=str, reverse=True, key=str):
        print('\t' + str(port))
        
    # Print the results
    print('Ports enumerated (sorted) reversed (sorted) reversed (sorted) reversed:')
    for port in sorted(ports, reverse=True, key=str, reverse=True, key=str, reverse=True, key=str):
        print('\t' + str(port))
        
    # Print the results
    print('Ports enumerated (sorted) reversed (sorted) reversed (sorted) reversed (sorted) reversed:')
    for port in sorted(ports, reverse=True, key=str, reverse=True, key=str, reverse=True, key=str, reverse=True, key=str, reverse=True, key=str, reverse=True, key=str, reverse=True, key=str, reverse=True, key=str, reverse=True, key=str, reverse=True, key=str, reverse=True, key=str, reverse=True, key=str, reverse=True, key=str, reverse=True, key=str, reverse=True, key=str, reverse=True, key=str, reverse=True, key=str, reverse=True, key=str, reverse=True, key=str, reverse=True, key=str, reverse=True, key=str, reverse=True, key=str, reverse=True, key=str, reverse=True, key=str, reverse=True, key=str, reverse=True, key=str, reverse=True, key=str, reverse=True, key=str, reverse=True, key=str, reverse=True, key=str, reverse=True, key=str, reverse=True, key=str, reverse=True, key=str, reverse=True, key=str, reverse=True, key=str, reverse=True, key=str, reverse=True, key=str, reverse=True, key=str, reverse=True, key=str, 