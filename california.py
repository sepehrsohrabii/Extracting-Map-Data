import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.maximize_window()

#driver.switch_to.active_element
result = []

def def_element3(element3):
    for element33 in element3:
        driver.execute_script("arguments[0].click();", element33)
        time.sleep(3)
        element4 = driver.find_elements(by=By.CLASS_NAME, value="panel")
        def_element4(element4, element33)
    driver.execute_script("window.history.go(-1)")
    driver.refresh()


def def_element4(element4, element33):
    for element44 in element4:
        driver.execute_script('arguments[0].click();', element44)
        time.sleep(3)
        location = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, "PanelInfoTable"))).text
        result.append(location.split('\n'))
        print(result)
        elementClose = driver.find_element(By.CLASS_NAME, "closeButton")
        driver.execute_script('arguments[0].click();', elementClose)
        time.sleep(3)


    driver.execute_script('arguments[0].click();', element33)
    time.sleep(3)
    df1 = pd.DataFrame(result)
    df1.to_excel('output4.xlsx', engine='xlsxwriter')


california_urls = ['https://apps.lamar.com/inventorybrowser/#center=39.79608,%20-121.84999&zoom=10',
                   'https://apps.lamar.com/inventorybrowser/#center=38.356369,%20-121.988137&zoom=10',
                   'https://apps.lamar.com/inventorybrowser/#center=38.297297,%20-122.287573&zoom=10',
                   'https://apps.lamar.com/inventorybrowser/#center=38.0015156,%20-122.0563625&zoom=10',
                   'https://apps.lamar.com/inventorybrowser/#center=36.588658,%20-121.848773&zoom=10',
                   'https://apps.lamar.com/inventorybrowser/#center=36.8122219,%20-119.8787071&zoom=10',
                   'https://apps.lamar.com/inventorybrowser/#center=35.3939977,%20-119.0800721&zoom=10',
                   'https://apps.lamar.com/inventorybrowser/#center=34.655213,%20-118.130577&zoom=10',
                   'https://apps.lamar.com/inventorybrowser/#center=34.0306891,%20-118.2205959&zoom=10',
                   'https://apps.lamar.com/inventorybrowser/#center=34.074582,%20-117.274979&zoom=10',
                   'https://apps.lamar.com/inventorybrowser/#center=33.7674653,%20-116.3095856&zoom=10',
                   'https://apps.lamar.com/inventorybrowser/#center=32.911966,%20-117.113093&zoom=10',
                   'https://apps.lamar.com/inventorybrowser/#center=41.322313732451455,%20-122.11004246925718&zoom=9',
                   ]

for url in california_urls:
    driver.get(url)
    time.sleep(3)
    element2 = driver.find_elements(by=By.CLASS_NAME, value="cluster")

    for element22 in element2:
        element22.click()
        time.sleep(3)
        if driver.find_elements(by=By.CLASS_NAME, value="cluster"):
            element2_1 = driver.find_elements(by=By.CLASS_NAME, value="cluster")

            for element212 in element2_1:
                time.sleep(5)
                #element212.click()
                driver.execute_script('arguments[0].click();', element212)
                time.sleep(3)
                element3 = driver.find_elements(by=By.CLASS_NAME, value="number")
                #def_element3(element3)
                #driver.execute_script("document.body.scrollTo(0, 100)")
                driver.execute_script("window.history.go(-1)")
                driver.refresh()

            driver.execute_script("window.history.go(-1)")
            driver.refresh()

        else:
         #   element3 = WebDriverWait(driver, 20).until(
          #      EC.element_to_be_clickable((By.CLASS_NAME, "number")))
            element3 = driver.find_elements(by=By.CLASS_NAME, value="number")
            #def_element3(element3)

    driver.execute_script("window.history.go(-1)")
    driver.refresh()










