#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens fruits. """    
    while True:
        print("Opening fruits...")
        fruit.open()
        fruit.close()
        print("Done.")
        time.sleep(1)
