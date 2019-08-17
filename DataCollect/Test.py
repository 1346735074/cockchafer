import urllib.request

response = urllib.request.urlopen('https://www.python.org')

htmlCode = response.read()
print(htmlCode)