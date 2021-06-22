import urllib.request, json

from .models import Quote

# Getting the quote base url
base_url=None

def configure_request(app):
    global base_url
    base_url = app.config['BASE_URL']
def getQuotes():
    quotes_list=[]
    new_quote_url=base_url.format()
    with urllib.request.urlopen(new_quote_url) as url:
        get_data=url.read()
        lll = json.loads(get_data)
        
        
    
# def getQuotes(): 
#         request.urlopen(base_url)
        
#         lll = request.get(base_url).json()
       
        # r = []
        id = lll.get('id')
        author = lll.get('author')
        quote = lll.get('quote')

        quoteObject = Quote(id,author,quote)
        quotes_list.append(quoteObject)
    return quotes_list