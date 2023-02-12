#!/home/cavemansimon/.virtualenvs/diceblaster/bin/python
import requests
from bs4 import BeautifulSoup
from selenium import webdriver


# https://www.dice.com/jobs?q=software%20engineer&location=Austin,%20TX,%20USA&latitude=30.267153&longitude=-97.7430608&countryCode=US&locationPrecision=City&radius=30&radiusUnit=mi&page=1&pageSize=20&language=en&eid=S2Q_

options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.binary_location = '/usr/bin/chromium'
chrome_driver_binary = "/usr/local/bin/chromedriver"
driver = webdriver.Chrome(chrome_driver_binary, chrome_options=options)

driver.get("https://www.dice.com/jobs?q=software%20engineer&location=Austin,%20TX,%20USA")
