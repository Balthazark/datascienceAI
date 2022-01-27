from email import header
import pandas as pd
import requests
from io import StringIO

url = 'https://www.hemnet.se/salda/bostader?location_ids%5B%5D=940808&item_types%5B%5D=villa&sold_age=6m'
#headers={'User-Agent': 'Mozilla/5.0'}
req = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})

data = StringIO(req.text)
dfs = pd.read_html(data)
