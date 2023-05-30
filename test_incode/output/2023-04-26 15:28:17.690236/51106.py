#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a list of numbers. """    
    from multiprocessing import Process
    
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    proc = Process(target=multiply, args=(numbers,))
    proc.start()
    
    proc.join()
    
    print(numbers)
    
