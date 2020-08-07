from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path=r"C:\webdrivers\chromedriver.exe")
#driver = webdriver.Firefox(executable_path=r"C:\webdrivers\geckodriver.exe")
#driver = webdriver.Ie(executable_path=r"C:\webdrivers\IEDriverServer.exe")

driver.get("https://www.amazon.com/CableMod-PRO-ModMesh-RMi-Cable/dp/B0799F4XWF/ref=sr_1_2?dchild=1&keywords=cablemod%2Bcorsair%2Brmx&qid=1596206319&s=electronics&sr=1-2&th=1/")

print(driver.title)  # Title of the page

print(driver.current_url)  # Returns URL

#print(driver.page_source)  # HTML code of page

driver.close()  # Closes browser
