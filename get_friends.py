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

#Option Chrome Driver ~

option = Options()
option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")
option.add_experimental_option(
    "prefs", {"profile.default_content_setting_values.notifications": 1}
)

#set up

start_url = 'https://www.facebook.com'
profile_url = 'https://www.facebook.com/jijivishaphuoc' #url truyền vào, lấy từ người thả react, crawl bạn bè của nó
PATH = "driver\chromedriver.exe"
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

#if visible: có tag friend mới lấy, k thì thôi :v
#hiện chưa nghĩ ra nên làm gì vào nếu ko hiện friend, bỏ qua ? đếm friend ?

def friend_tab(url):
    url = url
    driver.get(url + '/friends')
    driver.maximize_window()
    driver.execute_script("window.scrollTo(0, 500)") #Scroll down đến khi thấy tag friend ? 
    test_friend = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div/div/div/div/div/div[2]/div/div/div/div[2]/a[1]")))
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

    newurlList = urlList[3:] 
    newfriendList = friendsList[3:]
   
else:
    print("bruhhh")


#join dataframe
# thông tin của 1 cá nhân (name, birthday, gender, friend number(if visible), place) ?





