#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A function that removes a http request.
    def http_request(url):
        try:
            req = urllib.request.Request(url)
            response = urllib.request.urlopen(req)
            return response.read()
        except urllib.error.HTTPError as e:
            print("Error code: " + str(e.code))
            print("Error message: " + e.read())
            print("Error url: " + url)
            return ""
        except urllib.error.URLError as e:
            print("Error code: " + str(e.code))
            print("Error message: " + e.read())
            print("Error url: " + url)
            return ""
    return http_request(url)

