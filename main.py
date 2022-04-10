import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
driver = webdriver.Chrome("C:/Users/sepeh/Desktop/Extracting-Map-Data/chromedriver.exe")
driver.get('https://your.url/here?yes=brilliant')
results = []
content = driver.page_source
soup = BeautifulSoup(content)
final = soup.findAll(attrs={'id': 'PanelInfoTable'})
print(final[0])
