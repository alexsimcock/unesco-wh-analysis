import urllib.request
import io
from pandas import read_xml
from datetime import datetime

file = urllib.request.urlopen('https://whc.unesco.org/en/list/xml') 
raw_xml = file.read().decode('utf8')
file.close()

sites = read_xml(io.StringIO(raw_xml))

filename = 'whc-en-' + datetime.today().strftime('%Y-%m-%d') + '.csv'
sites.to_csv('downloaded-files/' + filename)