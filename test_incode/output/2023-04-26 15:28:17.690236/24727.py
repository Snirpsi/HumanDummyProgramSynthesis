#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens fruits and multiplyes a port. """    
    
    # Open the fruits file
    fr = open('fruits.txt', 'r')
    
    # Read the fruits into a list
    fruits = fr.readlines()
    
    # Close the fruits file
    fr.close()
    
    # Multiply each fruit by its port
    for fruit in fruits:
        fruit = fruit.strip()
        fruit = fruit.split(' ')
        fruit[1] = int(fruit[1])
        fruit[2] = int(fruit[2])
        fruit[3] = int(fruit[3])
        fruit[4] = int(fruit[4])
        fruit[5] = int(fruit[5])
        fruit[6] = int(fruit[6])
        fruit[7] = int(fruit[7])
        fruit[8] = int(fruit[8])
        fruit[9] = int(fruit[9])
        fruit[10] = int(fruit[10])
        fruit[11] = int(fruit[11])
        fruit[12] = int(fruit[12])
        fruit[13] = int(fruit[13])
        fruit[14] = int(fruit[14])
        fruit[15] = int(fruit[15])
        fruit[16] = int(fruit[16])
        fruit[17] = int(fruit[17])
        fruit[18] = int(fruit[18])
        fruit[19] = int(fruit[19])
        fruit[20] = int(fruit[20])
        fruit[21] = int(fruit[21])
        fruit[22] = int(fruit[22])
        fruit[23] = int(fruit[23])
        fruit[24] = int(fruit[24])
        fruit[25] = int(fruit[25])
        fruit[26] = int(fruit[26])
        fruit[27] = int(fruit[27])
        fruit[28] = int(fruit[28])
        fruit[29] = int(fruit[29])
        fruit[30] = int(fruit[30])
        fruit[31] = int(fruit[31])
        fruit[32] = int(fruit[32])
        fruit[33] = int(fruit[33])
        fruit[34] = int(fruit[34])
        fruit[35] = int(fruit[35])
        fruit[36] = int(fruit[36])
