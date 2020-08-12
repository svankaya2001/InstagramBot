from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.firefox.options import Options
import time

class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        cap = DesiredCapabilities().FIREFOX
        binary = r'C:\Program Files\Mozilla Firefox\firefox.exe'
        options = Options()
        options.set_headless(headless=True)
        options.binary = binary
        cap["marionette"] = True       
        self.bot = webdriver.Firefox(firefox_options=options, capabilities = cap, executable_path = r'C:\Users\shrey\OneDrive\Documents\geckodriver-v0.26.0-win64\geckodriver.exe')

    def login(self):
        bot = self.bot
        bot.get('https://www.instagram.com/accounts/login/')
        time.sleep(3)
        bot.find_element_by_name('username').send_keys(self.username)
        bot.find_element_by_name('password').send_keys(self.password + Keys.RETURN)
        time.sleep(3)

    def search(self, hashtag):
        bot = self.bot
        bot.get('https://www.instagram.com/explore/tags/'+hashtag)
    
    def likePhotos(self, amount):
        bot = self.bot
        bot.find_element_by_class_name('v1Nh3').click()
        i = 0
        while i < amount:
            time.sleep(1)
            bot.find_element_by_class_name('fr66n').click()
            bot.find_element_by_class_name('coreSpriteRightPaginationArrow').click()
            i+=1

hashtag = input("Search term: ")
amount = int(input("number of likes:"))
insta = InstagramBot('username', 'password')
insta.login()
insta.search(hashtag)
insta.likePhotos(amount)
