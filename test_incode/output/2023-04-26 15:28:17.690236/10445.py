#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens numbers or multiplyes words. """    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: %s <words>' % sys.argv[0])
        sys.exit()
    
    words = sys.argv[1:]
    
    for word in words:
        
        try:
            number = int(word)
            
            if number > 0:
                
                number = number * 10
                
                print(number)
            
            else:
                
                number = word * 10
                
                print(number)
            
        except ValueError:
            
            print('%s is not a number' % word)
            
        except TypeError:
            
            print('%s is not a string' % word)
            
        except OverflowError:
            
            print('%s is too big' % word)
            
        except ZeroDivisionError:
            
            print('%s is zero' % word)
            
        except IndexError:
            
            print('%s is too short' % word)
            
        except TypeError:
            
            print('%s is not a number' % word)
            
        except IndexError:
            
            print('%s is too short' % word)
            
        except TypeError:
            
            print('%s is not a number' % word)
            
        except IndexError:
            
            print('%s is too short' % word)
            
        except TypeError:
            
            print('%s is not a number' % word)
            
        except IndexError:
            
            print('%s is too short' % word)
            
        except TypeError:
            
            print('%s is not a number' % word)
            
        except IndexError:
            
            print('%s is too short' % word)
            
        except TypeError:
            
            print('%s is not a number' % word)
            
        except IndexError:
            
            print('%s is too short' % word)
            
        except TypeError:
            
            print('%s is not a number' % word)
            
        except IndexError:
            
            print('%s is too short' % word)
            
        except TypeError:
            
            print('%s is not a number' % word)
            
        except IndexError:
            
            print('%s is too short' % word)
            
        except TypeError:
            
            print('%s is not a number' % word)
            
        except IndexError:
            
            print('%s is too short' % word)
            
        except TypeError:
            
            print('%s is not a number' % word)
            
        except IndexError:
            
            print('%s is too short' % word)
            
        except TypeError:
            
            print('%s is not a number' % word)
            
        except IndexError:
            
            print('%s is too short' % word)
            
        except TypeError:
            
            print('%s is not a number' % word)
            
        except IndexError:
            
            print('%s is too short' % word)
            
        except TypeError:
            
            print('%s is not a number' % word)
            
        except IndexError:
            
            print('%s is too short' % word)
            
        except TypeError:
            
            print('