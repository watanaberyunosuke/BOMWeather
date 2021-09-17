#!/usr/bin/env python
"""
BOM Australia Forcast from official RSS, VIC Forcast
"""
import requests
import urllib.request
from bs4 import BeautifulSoup
import json

x = requests.get('http://www.bom.gov.au/fwo/IDV60901/IDV60901.95936.json', "json")
info = json.loads(str(x))

print(info)
