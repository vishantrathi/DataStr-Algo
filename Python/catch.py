
import urllib.request
try:
    webpage=urllib.request.urlopen('https://www.dgoogle.com')

except:
    print('could not access webpage!')
else:
    for line in webpage:
        print(line)