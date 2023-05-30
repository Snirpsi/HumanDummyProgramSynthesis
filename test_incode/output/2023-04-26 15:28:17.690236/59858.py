#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a list of numbers. """    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <file> [<file> ...]" % sys.argv[0])
        sys.exit()
    
    file = sys.argv[1]
    
    numbers = []
    for filename in sys.argv[2:]:
        with open(filename) as numbers_file:
            numbers.extend(numbers_file.read().split())
    
    numbers = list(map(int, numbers))
    
    numbers_file = open("numbers.txt", "w")
    numbers_file.write("\n".join(map(str, numbers)))
    numbers_file.close()
    
    numbers_file = open("numbers.txt", "r")
    numbers = numbers_file.read().splitlines()
    numbers_file.close()
    
    numbers_file = open("numbers.txt", "w")
    numbers_file.write("\n".join(map(str, numbers)))
    numbers_file.close()
    
    numbers_file = open("numbers.txt", "r")
    numbers = numbers_file.read().splitlines()
    numbers_file.close()
    
    numbers_file = open("numbers.txt", "w")
    numbers_file.write("\n".join(map(str, numbers)))
    numbers_file.close()
    
    numbers_file = open("numbers.txt", "r")
    numbers = numbers_file.read().splitlines()
    numbers_file.close()
    
    numbers_file = open("numbers.txt", "w")
    numbers_file.write("\n".join(map(str, numbers)))
    numbers_file.close()
    
    numbers_file = open("numbers.txt", "r")
    numbers = numbers_file.read().splitlines()
    numbers_file.close()
    
    numbers_file = open("numbers.txt", "w")
    numbers_file.write("\n".join(map(str, numbers)))
    numbers_file.close()
    
    numbers_file = open("numbers.txt", "r")
    numbers = numbers_file.read().splitlines()
    numbers_file.close()
    
    numbers_file = open("numbers.txt", "w")
    numbers_file.write("\n".join(map(str, numbers)))
    numbers_file.close()
    
    numbers_file = open("numbers.txt", "r")
    numbers = numbers_file.read().splitlines()
    numbers_file.close()
    
    numbers_file = open("numbers.txt", "w")
    numbers_file.write("\n".join(map(str, numbers)))
    numbers_file.close()
    
    numbers_file = open("numbers.txt", "r")
    numbers = numbers_file.read().splitlines()
    numbers_file.close()
    
    numbers_file = open("numbers.txt", "w")
    numbers_file.write("\n".join(map(str, numbers)))
    numbers_file.close()
    
    numbers_file = open("numbers.txt", "r")
    numbers = numbers_file.read().splitlines()
    numbers_file.close()
    
    numbers_file = open("numbers.txt", "w")
    numbers_