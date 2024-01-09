from selenium import webdriver
import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re

#ghi chú

option = Options()
option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")
option.add_experimental_option(
    "prefs", {"profile.default_content_setting_values.notifications": 1}
)

#setup

start_url = 'https://www.facebook.com'
profile_url = 'https://www.facebook.com/profile.php?id=100008402384102'
PATH = "./chromedriver.exe"
driver = webdriver.Chrome(chrome_options=option, executable_path=PATH)

#def

def login(url):
    url = url
    driver.get(url)
    driver.maximize_window()
    username = driver.find_element(By.ID, 'email')
    password = driver.find_element(By.ID, 'pass')
    username.send_keys("yelan482@gmail.com")
    password.send_keys('Linhcute542002')
    submit_button = driver.find_element(By.CLASS_NAME, '_6ltg')
    submit_button.find_element(By.XPATH, '//button[contains(@class, "_42ft _4jy0 _6lth _4jy6 _4jy1 selected _51sy")]').click()
    time.sleep(5)

login(start_url)

#infor DatVilla

def get_about_place(url):
    url = url + '/about_places'    
    driver.get(url)
    driver.maximize_window()
    # place = driver.find_element(By.XPATH, "//span[@class = 'xt0psk2']").text
    place = WebDriverWait(driver, 5).until(
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


#if visible

def friend_tab(url):
    url = url
    driver.get(url)
    driver.maximize_window()
    friendsTab = driver.find_element(By.XPATH,"//span[text()='Bạn bè']")
    friendsTab.click()
    driver.execute_script("window.scrollTo(0, 500)")
    test_friend = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div/div/div/div/div/div[2]/div/div/div/div[2]/a[1]")))
    abc = test_friend.get_attribute("href")
    match = re.search(r'friends_all$', abc)
    if match is not None:
        return 'visible'
    else:
        return 'invisible'

def _get_friends_list():
    return driver.find_elements_by_css_selector(".x1iyjqo2.x1pi30zi [href]")



check_public = friend_tab(profile_url)

if check_public == 'visible':
    num_of_loaded_friends = len(_get_friends_list())
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        try:
            WebDriverWait(driver, 2).until(lambda driver: len(_get_friends_list()) > num_of_loaded_friends)
            num_of_loaded_friends = len(_get_friends_list())
        except TimeoutException:
            break  # no more friends loaded
    my_friend = driver.find_elements_by_css_selector(".x1iyjqo2.x1pi30zi [href]")
    friendsList = []
    urlList = []
   
    for friend in my_friend:
        friendsList.append(friend.text)
        url = friend.get_attribute("href")
        urlList.append(url)
        print(friend.text, url)

    # newurlList = urlList[3:] 
    # newfriendList = friendsList[3:]
    # placeList = []
    # genderList = []
    # dateList = []
    # yearList = []

    # for target in newurlList:
    #     place = get_about_place(target)
    #     gender = get_gender(target)
    #     date_of_birth = get_date_of_birth(target)[0]
    #     year = get_date_of_birth(target)[1]
    #     print(place)
    #     print(gender)
    #     print(date_of_birth)
    #     print(year)
    #     placeList.append(place)
    #     genderList.append(gender)
    #     dateList.append(date_of_birth)
    #     yearList.append(year)


else:
    print("bruhhh")


#join dataframe






