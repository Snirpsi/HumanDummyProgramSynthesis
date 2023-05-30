#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A program that iterates over a http request.
    #It will print out the response from the server
    #and print out a message to the screen if there was a problem.
    #The program will exit if the request fails.
    try:
        req = urllib.request.Request(url)
        response = urllib.request.urlopen(req)
        print(response.read())
    except urllib.error.HTTPError as e:
        print("There was a problem with the request.")
        print(e)
    except urllib.error.URLError as e:
        print("There was a problem with the URL.")
        print(e)
    except urllib.error.HTTPError as e:
        print("There was a problem with the HTTP request.")
        print(e)
    except urllib.error.URLError as e:
        print("There was a problem with the URL request.")
        print(e)

