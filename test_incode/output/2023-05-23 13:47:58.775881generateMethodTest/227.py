#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A endless loop that adds a http request.
    while True:
        #The request is made to the url specified in the url variable.
        req = urllib.request.Request(url)
        #The response is made to the url specified in the url variable.
        response = urllib.request.urlopen(req)
        #The response is converted to a string.
        html = response.read()
        #The html variable is converted to a string.
        soup = BeautifulSoup(html, 'html.parser')
        #The soup variable is converted to a string.
        table = soup.find('table')
        #The table variable is converted to a string.
        rows = table.find_all('tr')
        #The rows variable is converted to a string.
        for row in rows:
            #The row variable is converted to a string.
            cols = row.find_all('td')
            #The cols variable is converted to a string.
            cells = cols[2:]
            #The cells variable is converted to a string.
            cells = [cell.text.strip() for cell in cells]
            #The cells variable is converted to a string.
            cells = [cell for cell in cells if cell]
            #The cells variable is converted to a string.
            cells = [cell for cell in cells if cell]
            #The cells variable is converted to a string.
            cells = [cell for cell in cells if cell]
            #The cells variable is converted to a string.
            cells = [cell for cell in cells if cell]
            #The cells variable is converted to a string.
            cells = [cell for cell in cells if cell]
            #The cells variable is converted to a string.
            cells = [cell for cell in cells if cell]
            #The cells variable is converted to a string.
            cells = [cell for cell in cells if cell]
            #The cells variable is converted to a string.
            cells = [cell for cell in cells if cell]
            #The cells variable is converted to a string.
            cells = [cell for cell in cells if cell]
            #The cells variable is converted to a string.
            cells = [cell for cell in cells if cell]
            #The cells variable is converted to a string.
            cells = [cell for cell in cells if cell]
            #The cells variable is converted to a string.
            cells = [cell for cell in cells if cell]
            #The cells variable is converted to a string.
            cells = [cell for cell in cells if cell]
            #The cells variable is converted to a string.
            cells = [cell for cell in cells if cell]
            #The cells variable is converted to a string.
            cells = [cell for cell in cells if cell]
            #The cells variable is converted to a string.
            cells = [cell for cell in cells if cell]
            #The cells variable is converted to a string.
            cells = [cell for cell in cells if cell]
            #The cells variable is converted to a string.
            cells = [cell for cell in cells if cell]
            #The cells variable is converted to a string.
            cells = [cell for cell in cells if cell]
            #The cells variable is converted to a string.
            cells = [cell for cell in cells if cell]
            #The cells variable is converted to a string.
            cells = [cell for cell in cells if cell]
            #The cells variable is converted to a string.
            cells = [cell for cell in cells if cell]
            #The cells variable is converted to a string.
            cells = [cell for cell in cells if cell]
            #The cells variable is converted to a string.
            cells = [cell for cell in cells if cell]
            #The cells variable is converted to a string.
            cells = [cell for cell in cells if cell]
            #The cells variable is converted to a string.
            cells = [cell for cell in cells if cell]
            #The cells variable is converted to a string.
            cells = [cell for cell in cells if cell]
            #The cells variable is converted to a string.
            cells = [cell for cell in cells if cell]
            #The cells variable is converted to a string.
            cells = [cell for cell in cells if cell]
            #The cells variable is converted to a string.
            cells = [cell for cell in cells if cell]
            #The cells variable is converted to a string.
            cells = [cell for cell in cells if cell]
            #The cells variable is converted to a string.
            cells = [cell for cell in cells if cell]
            #The cells variable is converted to a string.
            cells = [cell for cell in cells if cell]
            #The cells variable is converted to a string.
            cells = [cell for cell in cells if cell]
            #The cells variable is converted to a string.
            cells = [cell for cell in cells if cell]
            #The cells variable is converted to a string.
            cells = [cell for cell in cells if cell]
            #The cells variable is converted to a string.
            cells = [cell for cell in cells if cell]
            #The cells variable is converted to a string.
            cells = [cell for cell in cells if cell]
            #The cells variable is converted to a string.
            cells = [cell for cell in cell