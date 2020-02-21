from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

option = webdriver.ChromeOptions()
option.add_argument(" - incognito") # browsing in private mode

path_to_chromedriver = '/Users/arian/WorkSpace/dev/scraper/drivers/chromedriver'
driver = webdriver.Chrome(executable_path = path_to_chromedriver, options=option)

URL = "https://github.com/TheDancerCodes"
driver.get(URL)
driver.mazimize_window()

# Wait 20 seconds for page to load
timeout = 20
try:
    WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, "//img[@class=’avatar width-full rounded-2']")))
except TimeoutException:
    print(“Timed out waiting for page to load”)
    browser.quit()