import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print('NÃO FOI POSSÍVEL ACESSAR O SITE PUDIM!')
else:
    print('FOI POSSÍVEL ACESSAR O SITE PUDIM!')
    print(site.read())
