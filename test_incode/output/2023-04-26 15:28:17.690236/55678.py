#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes fruits. """    
    fruits = ['apple', 'banana', 'cherry']
    while True:
        fruit = ''.join(random.choice(fruits) for _ in range(3))
        print('The fruit is', fruit)
        time.sleep(1)
