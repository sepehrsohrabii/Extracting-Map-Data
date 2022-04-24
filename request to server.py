from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://apps.lamar.com/inventorybrowser/#center=34.033023923078964,%20-118.448615&zoom=13')

result = driver.execute_script('return JSON.stringify(window.dataJSON)')

print(result)