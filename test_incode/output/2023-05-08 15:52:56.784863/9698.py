#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A endless loop that iterates over a http request.
    while True:
        req = requests.get(url)
        soup = BeautifulSoup(req.text, 'html.parser')
        
        #Iterate over the table and print each row to the console.
        for tr in soup.find_all('tr'):
            print(tr.text)
        
        #Wait for 10 seconds and then exit.
        time.sleep(10)

