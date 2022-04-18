import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.window import WindowTypes
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from geopy.geocoders import Nominatim

driver = webdriver.Chrome()
driver.maximize_window()
geolocator = Nominatim(user_agent="geoapiExercises")
#driver.switch_to.active_element
result = []


def def_element2(element2, x):
    for element22 in element2:
        element2 = driver.find_elements(by=By.CSS_SELECTOR, value="div.cluster")
        time.sleep(3)
        driver.execute_script('document.getElementsByClassName("cluster")[' + str(x) + '].click()', element2[x])
        #time.sleep(5)
        #element22.click()
        time.sleep(3)
        if driver.find_elements(by=By.CLASS_NAME, value="cluster"):
            #element2_1 = driver.find_elements(by=By.CLASS_NAME, value="cluster")
            element2_1 = driver.find_elements(by=By.CSS_SELECTOR, value="div.cluster")
            i = 0
            for element212 in element2_1:
                try:
                    element2_2 = driver.find_elements(by=By.CSS_SELECTOR, value="div.cluster")
                    time.sleep(3)
                    driver.execute_script('document.getElementsByClassName("cluster")['+str(i)+'].click()', element2_2[i])
                    time.sleep(5)
                    '''
                    current_url = driver.current_url
                    time.sleep(5)
                    print(current_url)
                    zoom = "zoom=22"
                    if zoom in current_url:
                        driver.back()
                        driver.refresh()
                    '''
                    element3 = driver.find_elements(by=By.CLASS_NAME, value="number")
                    def_element3(element3)
                    driver.back()
                    driver.refresh()
                    i = i + 1
                except:
                    driver.back()
                    driver.refresh()
                    i = i + 1
                    continue

        else:
            element3 = driver.find_elements(by=By.CLASS_NAME, value="number")
            def_element3(element3)

        driver.back()
        driver.refresh()

def def_element3(element3):
    for element33 in element3:
        driver.execute_script("arguments[0].click();", element33)
        time.sleep(3)
        element4 = driver.find_elements(by=By.CLASS_NAME, value="panel")
        def_element4(element4, element33)


def def_element4(element4, element33):
    for element44 in element4:
        driver.execute_script('arguments[0].click();', element44)
        time.sleep(3)
        location = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, "PanelInfoTable"))).text
        location_list = location.split('\n')
        lat_long = location.split('\n')[3].split(' ')
        lat = lat_long[1]
        long = lat_long[3]
        location2 = geolocator.reverse(lat + "," + long)
        address = location2.raw['address']
        city = address.get('city', '')
        town = address.get('town', '')

        location_list.append(city)
        location_list.append(town)
        location_list.append(address)
        result.append(location_list)
        elementClose = driver.find_element(By.CLASS_NAME, "closeButton")
        driver.execute_script('arguments[0].click();', elementClose)
        time.sleep(3)


    driver.execute_script('arguments[0].click();', element33)
    time.sleep(3)
    df1 = pd.DataFrame(result)
    df1.to_excel('output.xlsx', engine='xlsxwriter')
#######################jquery hayi be vojud mian ke tushun etelaAt hast ##########################33

california_urls = [
                   'https://apps.lamar.com/inventorybrowser/#center=36.588658,%20-121.848773&zoom=10',
                   'https://apps.lamar.com/inventorybrowser/#center=36.8122219,%20-119.8787071&zoom=10',
                   'https://apps.lamar.com/inventorybrowser/#center=35.3939977,%20-119.0800721&zoom=10',
                   'https://apps.lamar.com/inventorybrowser/#center=34.655213,%20-118.130577&zoom=10',
                   'https://apps.lamar.com/inventorybrowser/#center=34.0306891,%20-118.2205959&zoom=10',
                   'https://apps.lamar.com/inventorybrowser/#center=34.074582,%20-117.274979&zoom=10',
                   'https://apps.lamar.com/inventorybrowser/#center=33.7674653,%20-116.3095856&zoom=10',
                   'https://apps.lamar.com/inventorybrowser/#center=32.911966,%20-117.113093&zoom=10',
                   'https://apps.lamar.com/inventorybrowser/#center=41.322313732451455,%20-122.11004246925718&zoom=9',
                   'https://apps.lamar.com/inventorybrowser/#center=39.79608,%20-121.84999&zoom=10',
                   'https://apps.lamar.com/inventorybrowser/#center=38.356369,%20-121.988137&zoom=10',
                   'https://apps.lamar.com/inventorybrowser/#center=38.297297,%20-122.287573&zoom=10',
                   'https://apps.lamar.com/inventorybrowser/#center=38.0015156,%20-122.0563625&zoom=10',
                   ]

for url in california_urls:
    driver.get(url)
    driver.refresh()
    time.sleep(3)
    element2 = driver.find_elements(by=By.CLASS_NAME, value="cluster")
    x = 0
    def_element2(element2, x)













