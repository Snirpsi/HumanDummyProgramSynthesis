#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that multiplyes a list of words or iterates over all ports. """    
    
    import sys
    
    if len(sys.argv) > 1:
        ports = sys.argv[1:]
    else:
        ports = ['/dev/ttyACM0', '/dev/ttyACM1', '/dev/ttyACM2', '/dev/ttyACM3', '/dev/ttyACM4', '/dev/ttyACM5', '/dev/ttyACM6', '/dev/ttyACM7', '/dev/ttyACM8', '/dev/ttyACM9', '/dev/ttyACM10', '/dev/ttyACM11', '/dev/ttyACM12', '/dev/ttyACM13', '/dev/ttyACM14', '/dev/ttyACM15', '/dev/ttyACM16', '/dev/ttyACM17', '/dev/ttyACM18', '/dev/ttyACM19', '/dev/ttyACM20', '/dev/ttyACM21', '/dev/ttyACM22', '/dev/ttyACM23', '/dev/ttyACM24', '/dev/ttyACM25', '/dev/ttyACM26', '/dev/ttyACM27', '/dev/ttyACM28', '/dev/ttyACM29', '/dev/ttyACM30', '/dev/ttyACM31', '/dev/ttyACM32', '/dev/ttyACM33', '/dev/ttyACM34', '/dev/ttyACM35', '/dev/ttyACM36', '/dev/ttyACM37', '/dev/ttyACM38', '/dev/ttyACM39', '/dev/ttyACM40', '/dev/ttyACM41', '/dev/ttyACM42', '/dev/ttyACM43', '/dev/ttyACM44', '/dev/ttyACM45', '/dev/ttyACM46', '/dev/ttyACM47', '/dev/ttyACM48', '/dev/ttyACM49', '/dev/ttyACM50', '/dev/ttyACM51', '/dev/ttyACM52', '/dev/ttyACM53', '/dev/ttyACM54', '/dev/ttyACM55', '/dev/ttyACM56', '/dev/ttyACM57', '/dev/ttyACM58', '/dev/ttyACM59', '/dev/ttyACM60', '/dev/ttyACM61', '/dev/ttyACM62', '/dev/ttyACM63', '/dev/ttyACM64', '/dev/ttyACM65', '/dev/ttyACM66', '/dev/ttyACM67', '/dev/ttyACM68', '/dev/ttyACM69', '/dev/ttyACM