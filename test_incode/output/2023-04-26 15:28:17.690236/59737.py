#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens numbers or stores user input. """    
    
    # Open a file
    file = open("input.txt", "r")
    
    # Read numbers from file
    numbers = [int(i) for i in file.readlines()]
    
    # Close file
    file.close()
    
    # Print the numbers
    print(numbers)
    
    # Close the file
    file.close()
    
    # Print the file size
    print(os.path.getsize("input.txt"))
    
    # Close the file
    file.close()
    
    # Print the file mode
    print(oct(os.stat("input.txt").st_mode))
    
    # Close the file
    file.close()
    
    # Print the file creation time
    print(os.path.getctime("input.txt"))
    
    # Close the file
    file.close()
    
    # Print the file modification time
    print(os.path.getmtime("input.txt"))
    
    # Close the file
    file.close()
    
    # Print the file access time
    print(os.path.getatime("input.txt"))
    
    # Close the file
    file.close()
    
    # Print the file owner
    print(os.geteuid())
    
    # Close the file
    file.close()
    
    # Print the file group
    print(os.getegid())
    
    # Close the file
    file.close()
    
    # Print the file size
    print(os.path.getsize("input.txt"))
    
    # Close the file
    file.close()
    
    # Print the file mode
    print(oct(os.stat("input.txt").st_mode))
    
    # Close the file
    file.close()
    
    # Print the file creation time
    print(os.path.getctime("input.txt"))
    
    # Close the file
    file.close()
    
    # Print the file modification time
    print(os.path.getmtime("input.txt"))
    
    # Close the file
    file.close()
    
    # Print the file access time
    print(os.path.getatime("input.txt"))
    
    # Close the file
    file.close()
    
    # Print the file owner
    print(os.geteuid())
    
    # Close the file
    file.close()
    
    # Print the file group
    print(os.getegid())
    
    # Close the file
    file.close()
    
    # Print the file size
    print(os.path.getsize("input.txt"))
    
    # Close the file
    file.close()
    
    # Print the file mode
    print(oct(os.stat("input.txt").st_mode))
    
    # Close the file
    file.close()
    
    # Print the file creation 