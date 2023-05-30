#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes a list of numbers or multiplyes words. """    
    while True:
        try:
            num = input("Enter a number: ")
            num = float(num)
            
            words = []
            
            for word in num.split():
                words.append(word)
            
            product = 1
            
            for word in words:
                product *= word
            
            print(product)
            
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
            
        except EOFError:
            print("\nGoodbye!")
            break
            
        except TypeError:
            print("\nGoodbye!")
            break
            
        except ZeroDivisionError:
            print("\nGoodbye!")
            break
            
        except TypeError:
            print("\nGoodbye!")
            break
            
        except IndexError:
            print("\nGoodbye!")
            break
            
        except TypeError:
            print("\nGoodbye!")
            break
            
        except NameError:
            print("\nGoodbye!")
            break
            
        except TypeError:
            print("\nGoodbye!")
            break
            
        except IndexError:
            print("\nGoodbye!")
            break
            
        except TypeError:
            print("\nGoodbye!")
            break
            
        except NameError:
            print("\nGoodbye!")
            break
            
        except TypeError:
            print("\nGoodbye!")
            break
            
        except IndexError:
            print("\nGoodbye!")
            break
            
        except TypeError:
            print("\nGoodbye!")
            break
            
        except NameError:
            print("\nGoodbye!")
            break
            
        except TypeError:
            print("\nGoodbye!")
            break
            
        except IndexError:
            print("\nGoodbye!")
            break
            
        except TypeError:
            print("\nGoodbye!")
            break
            
        except NameError:
            print("\nGoodbye!")
            break
            
        except TypeError:
            print("\nGoodbye!")
            break
            
        except IndexError:
            print("\nGoodbye!")
            break
            
        except TypeError:
            print("\nGoodbye!")
            break
            
        except NameError:
            print("\nGoodbye!")
            break
            
        except TypeError:
            print("\nGoodbye!")
            break
            
        except IndexError:
            print("\nGoodbye!")
            break
            
        except TypeError:
            print("\nGoodbye!")
            break
            
        except NameError:
            print("\nGoodbye!")
            break
            
        except TypeError:
            print("\nGoodbye!")
            break
            
        except IndexError:
            print("\nGoodbye!")
            break
            
        except TypeError:
            print("\nGoodbye!")
            break
            
        except NameError:
            print("\n