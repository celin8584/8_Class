from selenium import webdriver
#from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("file:///C:/Users/celin/Desktop/WebTable.html")
driver.maximize_window()
driver.implicitly_wait(30)

ele = driver.find_elements_by_xpath("//*[@id='emp']/thead/tr/th")
print(len(ele))

ele2 = driver.find_elements_by_xpath("//*[@id='emp']/tbody/tr[1]/td")
print(len(ele2))
