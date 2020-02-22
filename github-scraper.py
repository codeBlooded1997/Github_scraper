from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import pandas as pd

option = webdriver.ChromeOptions()
option.add_argument(" - incognito") # browsing in private mode

path_to_chromedriver = '/Users/arian/WorkSpace/dev/scraper/drivers/chromedriver'
driver = webdriver.Chrome(executable_path = path_to_chromedriver, options=option)

URL = "https://github.com/TheDancerCodes"
driver.get(URL)
driver.maximize_window()

# Wait 20 seconds for page to load
timeout = 30
try:
    WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.XPATH, "//img[@class=’avatar width-full rounded-2']")))
except TimeoutException:
    print("Timed out waiting for page to load")
    driver.quit()

xp_pinned_repos = "//div[@class='js-pinned-items-reorder-container']/ol/li"
repos = driver.find_elements_by_xpath(xp_pinned_repos)

titles = [repo.find_element_by_css_selector('a.text-bold ').text for repo in repos]
languages = [repo.find_element_by_css_selector('p.text-gray span').text for repo in repos]

for title, language in zip(titles, languages):
    print("RepoName : Language")
    print(title + ": " + language, '\n')

result = pd.DataFrame(
    {
        "TITLE": titles,
        "LANGUAGE": languages,
    })