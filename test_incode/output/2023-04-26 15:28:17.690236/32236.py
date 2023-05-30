#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <words>" % sys.argv[0])
        sys.exit()
    
    words = sys.argv[1:]
    
    for word in words:
        
        word = word.strip()
        
        if word == "":
            continue
        
        print("Opening %s..." % word)
        
        try:
            
            subprocess.call(['open', word])
            
        except FileNotFoundError:
            print("File not found: %s" % word)
        
        except subprocess.CalledProcessError:
            print("Command failed: %s %s" % (word, subprocess.CalledProcessError.output))
        
        except KeyboardInterrupt:
            print("\nUser interrupted")
            
        except OSError:
            print("\nCommand failed: %s %s" % (word, OSError.output))
        
        except subprocess.TimeoutExpired:
            print("\nCommand timed out")
        
        except subprocess.CalledProcessError:
            print("\nCommand failed: %s %s" % (word, subprocess.CalledProcessError.output))
        
        except subprocess.TimeoutExpired:
            print("\nCommand timed out")
        
        except subprocess.CalledProcessError:
            print("\nCommand failed: %s %s" % (word, subprocess.CalledProcessError.output))
        
        except subprocess.TimeoutExpired:
            print("\nCommand timed out")
        
        except subprocess.CalledProcessError:
            print("\nCommand failed: %s %s" % (word, subprocess.CalledProcessError.output))
        
        except subprocess.TimeoutExpired:
            print("\nCommand timed out")
        
        except subprocess.CalledProcessError:
            print("\nCommand failed: %s %s" % (word, subprocess.CalledProcessError.output))
        
        except subprocess.TimeoutExpired:
            print("\nCommand timed out")
        
        except subprocess.CalledProcessError:
            print("\nCommand failed: %s %s" % (word, subprocess.CalledProcessError.output))
        
        except subprocess.TimeoutExpired:
            print("\nCommand timed out")
        
        except subprocess.CalledProcessError:
            print("\nCommand failed: %s %s" % (word, subprocess.CalledProcessError.output))
        
        except subprocess.TimeoutExpired:
            print("\nCommand timed out")
        
        except subprocess.CalledProcessError:
            print("\nCommand failed: %s %s" % (word, subprocess.CalledProcessError.output))
        
        except subprocess.TimeoutExpired:
            print("\nCommand timed out")
        
        except subprocess.CalledProcessError:
            print("\nCommand failed: %s %s" % (word, subprocess.CalledProcessError.output))
        
        except subprocess.TimeoutExpired:
            print("\nCommand timed out")
        
        except subprocess.CalledProcessError:
            print("\nCommand failed: %s %s" % (word, subprocess.CalledProcessError.output))
        
        except subprocess.TimeoutExpired: