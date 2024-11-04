import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from datetime import datetime
import time

newdf = []

driver = webdriver.Chrome()  # Ensure chromedriver is in PATH
driver.get("https://petrolspy.com.au/map/station/5212f92f0364bb212f028d66")

time.sleep(3)  # Wait for data to load; adjust based on page load times
data_91 = driver.find_element(By.CSS_SELECTOR, "#infobox > div.infoContainer > div.prices > div:nth-child(1) > b.selected-price")
data_95 = driver.find_element(By.CSS_SELECTOR, "#infobox > div.infoContainer > div.prices > div:nth-child(2) > span:nth-child(2)")
data_98 = driver.find_element(By.CSS_SELECTOR, "#infobox > div.infoContainer > div.prices > div:nth-child(2) > span:nth-child(3)")
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Create data frame
newdf.append({
    "timestamp": current_time,
    "price 91": data_91.text,
    "price 95": data_95.text,
    "price 98": data_98.text,
})
driver.quit()

# Clean the data
newdf = pd.DataFrame(newdf)

# Get up to date csv file
current_data = pd.read_csv('eleven-7_endeavourhills_prices.csv')

# Update the file
updated_data = pd.concat([current_data, newdf], ignore_index=True)

# Update csv file
updated_data.to_csv('eleven-7_endeavourhills_prices.csv')