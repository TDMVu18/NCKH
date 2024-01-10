from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import os
import time
import pandas as pd
import env_var


# For selenium 4
path_chrome_drive = 'E:/TOOLS/Chromedrive_ver120/chromedriver-win64/chromedriver.exe'
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
service = Service(path_chrome_drive)
driver = webdriver.Chrome(service=service, options=chrome_options)

# Login function
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
    url = url + '&sk=about_places'    
    driver.get(url)
    driver.maximize_window()
    try:
        # place = driver.find_element(By.XPATH, "//span[@class = 'xt0psk2']").text
        place = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class = 'xt0psk2']"))
        ).text
    except:     
        place = None
    return place

def get_gender(url):
    url = url + '&sk=about_contact_and_basic_info'
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
    url = url + '&sk=about_contact_and_basic_info'
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

def get_total_friend(url):
    driver.get(url)
    driver.maximize_window()
    try:
        total_friend = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class = 'x1n2onr6 x1ja2u2z x9f619 x78zum5 xdt5ytf x2lah0s x193iq5w']/div/div[2]/span/a"))
        ).text
    except:
        total_friend = None
    return total_friend