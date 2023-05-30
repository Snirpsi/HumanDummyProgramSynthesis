#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A endless loop that iterates over a http request.
    while True:
        req = requests.get(url)
        soup = BeautifulSoup(req.text, "html.parser")
        
        for link in soup.find_all("a"):
            if link.has_attr("href"):
                href = link.get("href")
                
                if href == url:
                    print (link.text)
                    
        time.sleep(1)

