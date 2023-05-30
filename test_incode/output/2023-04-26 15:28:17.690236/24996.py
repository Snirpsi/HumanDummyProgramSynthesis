#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that calculates user input or calculates all ports. """    
    
    # Get the input from the user
    ports = input("Enter the ports separated by comma: ")
    
    # Split the input into ports
    ports = ports.split(",")
    
    # Calculate the ports
    ports = [int(p) for p in ports]
    
    # Print the ports
    print("The ports entered are:")
    for p in ports:
        print(p)
        
    # Calculate the total ports
    total_ports = sum(ports)
    
    # Print the total ports
    print("The total ports entered are:")
    print(total_ports)
    
    # Calculate the average ports
    avg_ports = total_ports/len(ports)
    
    # Print the average ports
    print("The average ports entered are:")
    print(avg_ports)
    
    # Calculate the standard deviation
    std_ports = math.sqrt(sum([pow((p - avg_ports), 2) for p in ports]))
    
    # Print the standard deviation
    print("The standard deviation entered are:")
    print(std_ports)
    
    # Calculate the median ports
    med_ports = ports[int(len(ports)/2)-1]
    
    # Print the median ports
    print("The median ports entered are:")
    print(med_ports)
    
    # Calculate the mode ports
    mode_ports = ports[int(len(ports)/2)-2]
    
    # Print the mode ports
    print("The mode ports entered are:")
    print(mode_ports)
    
    # Calculate the mode ports
    mode_ports = ports[int(len(ports)/2)-1]
    
    # Print the mode ports
    print("The mode ports entered are:")
    print(mode_ports)
    
    # Calculate the mode ports
    mode_ports = ports[int(len(ports)/2)-2]
    
    # Print the mode ports
    print("The mode ports entered are:")
    print(mode_ports)
    
    # Calculate the mode ports
    mode_ports = ports[int(len(ports)/2)-1]
    
    # Print the mode ports
    print("The mode ports entered are:")
    print(mode_ports)
    
    # Calculate the mode ports
    mode_ports = ports[int(len(ports)/2)-2]
    
    # Print the mode ports
    print("The mode ports entered are:")
    print(mode_ports)
    
    # Calculate the mode ports
    mode_ports = ports[int(len(ports)/2)-1]
    
    # Print the mode ports
    print("The mode ports entered are:")
    print(mode_ports)