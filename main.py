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
element1 = driver.find_elements(by=By.CLASS_NAME, value="plant")
for element11 in element1:
    element11.click()
    element2 = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CLASS_NAME, "cluster")))

    element2 = driver.find_elements(by=By.CLASS_NAME, value="cluster")


    for element22 in element2:
        driver.execute_script('arguments[0].click();', element22)
        #element22.click()

        element3 = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "number")))

        element3 = driver.find_elements(by=By.CLASS_NAME, value="number")

        for element33 in element3:
            driver.execute_script("arguments[0].click();", element33)
            #element33.click()
            element4 = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "panel")))
            #driver.refresh()
            element4 = driver.find_elements(by=By.CLASS_NAME, value="panel")
            print(result)


            driver.execute_script('arguments[0].click();', element4[0])
            #element4[0].click()
            result.append(WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.ID, "PanelInfoTable"))).text)
            print(result)
            elementClose = driver.find_element(By.CLASS_NAME, "closeButton")
            driver.execute_script('arguments[0].click();', elementClose)

            #url = driver.current_url
            #r = requests.get(url, headers=headers)
            #soup = BeautifulSoup(r.text, 'html.parser')

            #result.append(soup.findAll('#PanelInfoTable'))








