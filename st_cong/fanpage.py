from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions, Chrome
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.action_chains import ActionChains
import re
import pandas as pd
from time import sleep
import random
import csv

# from login_fb import Login


class GET_USER_FFANPAGE:
    def __init__(self):
        self.username =  "yelan482@gmail.com" #"Buithingan011195@gmail.com"  #
        self.password =  "Linhcute542002" # "iubele"  #

        # self.df = pd.read_csv("datasets/data.csv")
        # Options

        service = Service(executable_path="fanpage_bot/chromedriver.exe")
        options = ChromeOptions()
        options.add_experimental_option("detach", True)
        options.add_argument("--disable-extensions")
        # options.add_argument("--headless")
        options.add_argument("--incognito")
        options.add_argument("--window-size=1920x1080")
        self.browser = Chrome(options=options)
        self.actions = ActionChains(self.browser)

        # self.browser = Login().login()

    def login(self):
        self.browser.get("https://www.facebook.com/")
        assert "Facebook" in self.browser.title
        elem = self.browser.find_element(By.ID, "email")
        elem.send_keys(self.username)
        elem = self.browser.find_element(By.ID, "pass")
        elem.send_keys(self.password)

        self.browser.find_element(By.NAME, "login").click()
        sleep(random.randint(3, 5))

        return

    def get_user_link(self):
        # for i, link in enumerate(self.df["link"]):
        #     # self.browser.get(link)
        #     pass

        self.browser.get("https://www.facebook.com/DoantruongQuocHoc")
        sleep(random.randint(3, 5))

        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # sleep(random.randint(2,4))
        # self.browser.execute_script(
        #     "window.scrollTo(0, document.body.scrollHeight);")

        l = []
        for p in range(5, 15):
            print("loop:", p)
            try:
                post_react = self.browser.find_element(
                    By.XPATH,
                    f"/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div[2]/div/div[2]/div[3]/div[{p}]/div/div/div/div/div/div/div/div/div/div/div[8]/div/div/div[4]/div/div/div[1]/div/div[1]/div/div[1]/div/span/div/span[2]"
                    # f"/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div[2]/div/div[2]/div[3]/div[{p}]/div/div/div/div/div/div/div/div/div/div/div[8]/div/div/div[4]/div/div/div[1]/div/div[1]/div/div[1]"
                    # "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[4]/div[2]/div/div[2]/div[3]/div["+str(p)+"]/div/div/div/div/div/div/div/div/div/div/div[2]/div/div/div[4]/div/div/div[1]/div/div[1]/div/div[1]/div/span/div/span[2]/span/span"
                )
            except:
                post_react = self.browser.find_element(
                    By.XPATH,   
                    
                    f"/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[4]/div[2]/div/div[2]/div[3]/div[{p}]/div/div/div/div/div/div/div/div/div/div/div[8]/div/div/div[4]/div/div/div[1]/div/div[1]/div/div[1]/div/span/div/span[2]/span/span",
                )

            self.actions.move_to_element(post_react).perform()
            post_react.click()

            sleep(random.randint(2, 4))

            scroll_element = self.browser.find_element(
                By.XPATH,
                # '/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[3]/div'
                # '/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div[2]/div[3]/div/div[3]/div'
                "/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[3]",
            )

            self.actions.click_and_hold(scroll_element).move_by_offset(
                0, 200
            ).release().perform()

            last_react_user = None
            while last_react_user is None:
                try:
                    last_react_user = self.browser.find_element(
                        By.XPATH,
                        f"/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[{post_react.text}]/div/div"
                        # "/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div[2]/div[3]/div/div[1]/div["+str(post_react.text)+"]/div/div/div[2]/div[1]/div/div/div/span/div/a"
                    )
                except:
                    try:
                        self.actions.click_and_hold(scroll_element).move_by_offset(
                            0, 150
                        ).release().perform()
                    except:
                        while True:
                            current_scroll_position = self.browser.execute_script(
                                "return window.scrollY;"
                            )
                            sleep(random.randint(1,2))
                            document_height = self.browser.execute_script(
                                "return document.body.scrollHeight;"
                            )
                            if current_scroll_position <= document_height:
                                break

            for i in range(1, int(post_react.text)):
                link = self.browser.find_element(
                    By.XPATH,
                    f"/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[{i}]/div/div/div[2]/div[1]/div/div/div/span/div/a",
                )
                z = link.get_attribute("href")
                z = re.sub(r"__cft__.*", "", z)
                l.append(z)
                print(z)

            print(len(l))
            # close_element
            self.browser.find_element(
                By.XPATH,
                "/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[2]/div",
            ).click()
            sleep(random.randint(2, 5))

        with open("user_qh_link.csv", "a", newline="", encoding="utf-8") as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(l)
        return


G = GET_USER_FFANPAGE()
G.login()
G.get_user_link()