#!/usr/bin/env python
"""
BOM Australia Warning from official RSS, VIC Warning
"""
import requests
from bs4 import BeautifulSoup
url = "http://www.bom.gov.au/fwo/IDZ00059.warnings_vic.xml"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
response = requests.get(url, headers=headers) #http requrest
soup = BeautifulSoup(response.text, 'html.parser') #use BS to parse

"""
Main output

"""
print(soup.title)
print("        ")
print(soup.description.string)
print("*******************") #title breaker
print("    ")
print(soup.generator.string)

#soup_find_item = soup.find("item")

print(soup.get_text())
