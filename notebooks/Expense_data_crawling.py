# Import the Python libraries and modules needed
import chromedriver_autoinstaller
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

chromedriver_autoinstaller.install()
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pandas as pd

# Launch the Chrome browser in debugsging mode using the Selenium module
co = Options()
co.add_experimental_option('debuggerAddress', '127.0.0.1:9222')
browser = webdriver.Chrome(options=co)
browser.get("https://www.notion.so/too-much-hobbies/23fc0bae2e36804ea1e1f3f60d0ed401?v=23fc0bae2e368170a775000cbc2f58d7")
time.sleep(5)

# Since the Page Down key doesn’t work for scrolling in Notion, I clicked the first checkbox to scroll the page to the end
check_box = browser.find_element(By.CSS_SELECTOR, 'div[data-index="0"] div.pseudoHover.pseudoActive')
check_box.click()

# Define an empty dictionary to collect expense data
expenses = {'items':[], 'prices':[], 'categories':[], 'date':[] }

# Collect expense data including the items I bought, their prices, categories, and dates
num = 0
while True:
    try:
        ActionChains(browser).key_down(Keys.DOWN).perform()
        item = browser.find_element(By.CSS_SELECTOR, f'div.notion-table-view-cell[data-col-index="0"][data-row-index="{num}"]')
        expenses['items'].append(item.text)
        price = browser.find_element(By.CSS_SELECTOR, f'div.notion-table-view-cell[data-col-index="1"][data-row-index="{num}"]')
        expenses['prices'].append(price.text)
        category = browser.find_element(By.CSS_SELECTOR, f'div.notion-table-view-cell[data-col-index="2"][data-row-index="{num}"]')
        expenses['categories'].append(category.text)
        day = browser.find_element(By.CSS_SELECTOR, f'div.notion-table-view-cell[data-col-index="3"][data-row-index="{num}"]')
        expenses['date'].append(day.text)
        num += 1
    except:
        break

# Convert the dictionary into a DataFrame using pandas
df = pd.DataFrame(expenses)

# Save the DataFrame as a CSV file
df.to_csv('expense.csv', index=False)