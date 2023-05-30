#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts user input and stores a port. """    
    
    # Define the port
    port = '/dev/ttyUSB0'
    
    # Define the command
    command = 'echo ' + port + ' > /sys/class/ttyUSB0'
    
    # Execute the command
    subprocess.call(command, shell=True)
    
    # Print the output
    print(port)
    
    # Close the port
    subprocess.call(['sudo', 'rm', '-rf', '/dev/ttyUSB0'], shell=True)
    
    # Print the output
    print(port)
    
    # Close the port
    subprocess.call(['sudo', 'rm', '-rf', '/dev/ttyUSB1'], shell=True)
    
    # Print the output
    print(port)
    
    # Close the port
    subprocess.call(['sudo', 'rm', '-rf', '/dev/ttyUSB2'], shell=True)
    
    # Print the output
    print(port)
    
    # Close the port
    subprocess.call(['sudo', 'rm', '-rf', '/dev/ttyUSB3'], shell=True)
    
    # Print the output
    print(port)
    
    # Close the port
    subprocess.call(['sudo', 'rm', '-rf', '/dev/ttyUSB4'], shell=True)
    
    # Print the output
    print(port)
    
    # Close the port
    subprocess.call(['sudo', 'rm', '-rf', '/dev/ttyUSB5'], shell=True)
    
    # Print the output
    print(port)
    
    # Close the port
    subprocess.call(['sudo', 'rm', '-rf', '/dev/ttyUSB6'], shell=True)
    
    # Print the output
    print(port)
    
    # Close the port
    subprocess.call(['sudo', 'rm', '-rf', '/dev/ttyUSB7'], shell=True)
    
    # Print the output
    print(port)
    
    # Close the port
    subprocess.call(['sudo', 'rm', '-rf', '/dev/ttyUSB8'], shell=True)
    
    # Print the output
    print(port)
    
    # Close the port
    subprocess.call(['sudo', 'rm', '-rf', '/dev/ttyUSB9'], shell=True)
    
    # Print the output
    print(port)
    
    # Close the port
    subprocess.call(['sudo', 'rm', '-rf', '/dev/ttyUSB10'], shell=True)
    
    # Print the output
    print(port)
    
    # Close the port
    subprocess.call(['sudo', 'rm', '-rf', '/dev/ttyUSB11'], shell=True)
    
    # Print the output
    print(port)
    
    # Close the port
    subprocess.call(['sudo', 'rm', '-rf', '/dev/ttyUSB12'], shell=True)
    
