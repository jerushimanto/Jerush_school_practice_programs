import urllib.request 
request_url = urllib.request.urlopen('https://www.youtube.com') 
print(request_url.read())
