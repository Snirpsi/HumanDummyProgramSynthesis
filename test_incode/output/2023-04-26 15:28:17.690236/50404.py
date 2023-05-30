#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores numbers or iterates over a port. """    
    while True:
        port = input('Enter a port: ') # Get a port number from the user
        try:
            port = int(port) # Convert it to an int
        except ValueError:
            print('Invalid port number. Try again.')
            continue
        if port < 1 or port > 65535:
            print('Invalid port number. Try again.')
            continue
        print('Port number:', port, '\n')
        
        # Store the port number in an array and print it out
        ports.append(port) # Append the port number to the array
        print('Port numbers:', ports, '\n')
        
        # Iterate over the array and print each number in turn
        for port in ports:
            print(port, '\n')
        
        # Exit the loop if the user enters ctrl-c
        if input('Do you want to exit? [y/N]: ') == 'y':
            break
        
        # Print the array again to show that it has been updated
        print('\nPorts:', ports, '\n')
        
        # Wait for a second before printing the updated array
        time.sleep(1)
        
        # Print the updated array
        print('\nPorts:', ports, '\n')
        
        # Wait for a second before printing the updated array
        time.sleep(1)
        
        # Print the updated array
        print('\nPorts:', ports, '\n')
        
        # Wait for a second before printing the updated array
        time.sleep(1)
        
        # Print the updated array
        print('\nPorts:', ports, '\n')
        
        # Wait for a second before printing the updated array
        time.sleep(1)
        
        # Print the updated array
        print('\nPorts:', ports, '\n')
        
        # Wait for a second before printing the updated array
        time.sleep(1)
        
        # Print the updated array
        print('\nPorts:', ports, '\n')
        
        # Wait for a second before printing the updated array
        time.sleep(1)
        
        # Print the updated array
        print('\nPorts:', ports, '\n')
        
        # Wait for a second before printing the updated array
        time.sleep(1)
        
        # Print the updated array
        print('\nPorts:', ports, '\n')
        
        # Wait for a second before printing the updated array
        time.sleep(1)
        
        # Print the updated array
        print('\nPorts:', ports, '\n')
        
        # Wait for a second before printing the updated array
        time.sleep(1)
        
        # Print the updated array
        print('\nPorts:', ports, '\n')
        
        # Wait for a second before printing the updated array
        time.sleep(1)
        
        # Print the updated array
        print('\nPorts:', ports, '\n')
        
        # Wait for a second before printing the 