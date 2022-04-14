import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://apps.lamar.com/inventorybrowser/#center=39.85768,%20-96.743969&zoom=4')
driver.switch_to.active_element
result = []

def def_element3(element3):
    for element33 in element3:
        driver.execute_script("arguments[0].click();", element33)
        #element33.click()
        time.sleep(3)
        #element4 = WebDriverWait(driver, 20).until(
        #    EC.element_to_be_clickable((By.CLASS_NAME, "panel")))
        element4 = driver.find_elements(by=By.CLASS_NAME, value="panel")
        def_element4(element4, element33)


def def_element4(element4, element33):
    for element44 in element4:
        driver.execute_script('arguments[0].click();', element44)
        #element44.click()
        time.sleep(3)
        location = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, "PanelInfoTable"))).text
        result.append(location.split('\n'))
        print(result)
        elementClose = driver.find_element(By.CLASS_NAME, "closeButton")
        driver.execute_script('arguments[0].click();', elementClose)
        time.sleep(3)


    driver.execute_script('arguments[0].click();', element33)
    #element33.click()
    time.sleep(3)
    df1 = pd.DataFrame(result)
    df1.to_excel('output3.xlsx', engine='xlsxwriter')


#element1 = WebDriverWait(driver, 20).until(
 #   EC.element_to_be_clickable((By.CLASS_NAME, "plant")))
element1 = driver.find_elements(by=By.CLASS_NAME, value="plant")
y = 0
for element11 in element1:
    if y > 0:
        y = y + 1
        driver.execute_script("window.history.go(-1)")
        driver.refresh()
    element11.click()
    time.sleep(3)
    #element2 = WebDriverWait(driver, 20).until(
     #   EC.presence_of_element_located((By.CLASS_NAME, "cluster")))
    element2 = driver.find_elements(by=By.CLASS_NAME, value="cluster")
    #time.sleep(5)
    x = 0
    for element22 in element2:
        if x > 0:
            x = x + 1
            driver.execute_script("window.history.go(-1)")
            driver.refresh()
        #driver.execute_script('arguments[0].click();', element22)
        element22.click()
        time.sleep(3)

        if driver.find_elements(by=By.CLASS_NAME, value="cluster"):
         #   element2_1 = WebDriverWait(driver, 20).until(
          #      EC.element_to_be_clickable((By.CLASS_NAME, "cluster")))
            element2_1 = driver.find_elements(by=By.CLASS_NAME, value="cluster")
            i = 0

            for element212 in element2_1:
                if i > 0:
                    i = i + 1
                    driver.execute_script("window.history.go(-1)")
                    driver.refresh()
                element212.click()
                time.sleep(3)
             #   element3 = WebDriverWait(driver, 20).until(
              #      EC.element_to_be_clickable((By.CLASS_NAME, "number")))
                element3 = driver.find_elements(by=By.CLASS_NAME, value="number")
                def_element3(element3)
        else:
         #   element3 = WebDriverWait(driver, 20).until(
          #      EC.element_to_be_clickable((By.CLASS_NAME, "number")))
            element3 = driver.find_elements(by=By.CLASS_NAME, value="number")
            def_element3(element3)










