from . import requests,json
from .models import Quote

# Getting the quote base url
base_url=None

def configure_request(app):
    global base_url
    base_url = app.config['BASE_URL']
    
def getQuotes(): 
    # request.urlopen(base_url):
        
        bbb = requests.get(base_url).json()
       
        r = []
        id = bbb.get('id')
        author = bbb.get('author')
        quote = bbb.get('quote')

        quoteObject = Quote(id,author,quote)
        r.append(quoteObject)
        return r