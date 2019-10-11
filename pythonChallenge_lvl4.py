from urllib.parse import urlparse
import urllib.request


ur = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345"

while (True):

    a = urlparse(ur)
    page = urllib.request.urlopen(ur).read()
    b = str(page, 'utf-8')

    print(b)
    listt = filter(lambda x: x.isdigit(), b)
    c = ""
    for i in listt:
        c += i

    d = a._replace(query=f"nothing={c}")
    ur = d.geturl()
    print(ur)
