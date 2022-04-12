import pandas as pd
import requests
from requests_html import HTMLSession
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from fake_headers import Headers


headers = Headers(
        browser="chrome",  # Generate only Chrome UA
        os="win",  # Generate ony Windows platform
        headers=True  # generate misc headers
    ).generate()


driver = webdriver.Chrome()
driver.get('http://apps.lamar.com/inventorybrowser/#center=39.85768,%20-96.743969&zoom=4')
result = []
element1 = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "plant")))
#element1 = driver.find_elements(by=By.CLASS_NAME, value="plant")
element1.click()

element2 = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.CLASS_NAME, "cluster")))
#element2 = driver.find_elements(by=By.CLASS_NAME, value="cluster")
#element2.click()
driver.execute_script('arguments[0].click();', element2)
#element22.click()

element3 = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "number")))
#element3 = driver.find_elements(by=By.CLASS_NAME, value="number")
#driver.execute_async_script("arguments[0].click();", element33)
element3.click()

element4 = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "panel")))
#element4 = driver.find_elements(by=By.CLASS_NAME, value="panel")
#driver.execute_async_script('arguments[0].click();', element4)
element4.click()

url = driver.current_url
r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.text, 'html.parser')
for td in soup.findAll('td'):
    print(td.text)
    result.append(td.text)






