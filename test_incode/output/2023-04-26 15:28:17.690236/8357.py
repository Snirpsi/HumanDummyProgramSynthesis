#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts a list of words and stores fruits. """    
    
    # read input from stdin
    words = []
    for line in sys.stdin:
        line = line.strip()
        if line:
            words.append(line)
    
    # convert words to fruits
    fruits = []
    for word in words:
        fruits.append(word)
    
    # print fruits
    for fruit in fruits:
        print(fruit)
        
    # write output to stdout
    sys.stdout.write('\n'.join(fruits))
    
    # close stdin
    sys.stdin.close()
    
    # close stdout
    sys.stdout.close()
    
    # close stderr
    sys.stderr.close()
    
    # exit program
    sys.exit(0)
