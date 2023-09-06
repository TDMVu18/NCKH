from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import os
import time
import pandas as pd
import datvilla.env_var as env_var

start_url = 'https://www.facebook.com'
path_chrome_drive = 'driver\chromedriver.exe'

# For selenium 4
chrome_options = webdriver.ChromeOptions()
# Mode Incognito
chrome_options.add_argument("--incognito")
service = Service(path_chrome_drive)
driver = webdriver.Chrome(service=service, options=chrome_options)


def login(url):
    url = url
    driver.get(url)
    driver.maximize_window()
    username = driver.find_element(By.ID, 'email')
    password = driver.find_element(By.ID, 'pass')
    username.send_keys(os.environ.get("FACEBOOK_USER"))
    password.send_keys(os.environ.get("FACEBOOK_PASSWORD"))
    submit_button = driver.find_element(By.CLASS_NAME, '_6ltg')
    submit_button.find_element(By.XPATH, '//button[contains(@class, "_42ft _4jy0 _6lth _4jy6 _4jy1 selected _51sy")]').click()
    time.sleep(5)

login(start_url)

def get_name(url):
    url = url
    driver.get(url)
    driver.maximize_window()
    # name = driver.find_element(By.XPATH, '//h1[@class = "x1heor9g x1qlqyl8 x1pd3egz x1a2a7pz"]').text
    name = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located((By.XPATH, '//h1[@class = "x1heor9g x1qlqyl8 x1pd3egz x1a2a7pz"]'))
    ).text
    return name

def get_about_place(url):
    url = url + '/about_places'    
    driver.get(url)
    driver.maximize_window()
    # place = driver.find_element(By.XPATH, "//span[@class = 'xt0psk2']").text
    place = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located((By.XPATH, "//span[@class = 'xt0psk2']"))
    ).text
    return place

def get_gender(url):
    url = url + '/about_contact_and_basic_info'
    driver.get(url)
    driver.maximize_window()
    try:
        # gender = driver.find_element(By.XPATH, "//div[@class='x1hq5gj4']/div/div/div[2]/div/div/div/div/div/span").text
        gender = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='x1hq5gj4']/div/div/div[2]/div/div/div/div/div/span"))
        ).text
    except:
        gender = None
    return gender

def get_date_of_birth(url):
    url = url + '/about_contact_and_basic_info'
    driver.get(url)
    driver.maximize_window()
    try:
        # date_month = driver.find_element(By.XPATH, "//div[@class = 'x1hq5gj4']/../div[3]/div/div/div[2]/div/div/div/div/div/span").text
        date_month = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class = 'x1hq5gj4']/../div[3]/div/div/div[2]/div/div/div/div/div/span"))
        ).text
        year = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class = 'x1hq5gj4']/../div[3]/div/div/div[2]/div[2]/div/div/div/div/span"))
        ).text
    except:
        date_month = None
        year = None
    return date_month, year

url = "https://www.facebook.com/ttrang0"

name = get_name(url)
place = get_about_place(url)
gender = get_gender(url)
date_of_birth = get_date_of_birth(url)[0]
year = get_date_of_birth(url)[1]
print(name)
print(place)
print(gender)
print(date_of_birth)
print(year)

data = [
    {'name': name, 'place': place, 'gender': gender, 'date_of_birth': date_of_birth, 'year': year}
]
# columns = ('name', 'place', 'gender', 'date_of_birth', 'year')

df = pd.DataFrame(data)
print(df)

    