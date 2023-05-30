#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates numbers or opens words. """    
    
    import sys
    
    if len(sys.argv) == 1:
        print("Usage: %s [number]" % sys.argv[0])
        sys.exit()
    
    number = sys.argv[1]
    
    if number == '':
        number = 0
    
    numbers = [str(n) for n in range(number)]
    
    file = open("words.txt", "w")
    
    for number in numbers:
        file.write(number + "\n")
    
    file.close()
    
    print("Done")

<|/ file filename=word.py ext=.py |>