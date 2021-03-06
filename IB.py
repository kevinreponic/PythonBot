from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import json
class InstagramBot: 

    def __init__(self, username, password):        
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox()
        
       
    def closeBrowser(self) :
        self.driver.close()

    def login(self) :
        driver = self.driver
        driver.get('https://www.instagram.com/')
        time.sleep(4)
        login_button = driver.find_element_by_xpath("//a[@href='/accounts/login/?source=auth_switcher']")
        login_button.click()
        time.sleep(2)
        user_name_elem = driver.find_element_by_xpath("//input[@name='username']")
        user_name_elem.clear()
        user_name_elem.send_keys(self.username)
        password_elem =  driver.find_element_by_xpath("//input[@name='password']")
        password_elem.clear()
        password_elem.send_keys(self.password)
        password_elem.send_keys(Keys.RETURN)
        time.sleep(4)
    
    def like_photo(self, hashtags) :
        driver = self.driver
        for hashtag in hashtags:      
         driver.get("https://www.instagram.com/explore/tags/"+hashtag+"/")
         time.sleep(2)
         for i in range (1, 5):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)

         hrefs = driver.find_elements_by_xpath('/html/body/span/section/main/article/div/div/div/div/div/a')
         pic_hrefs = [elem.get_attribute('href') for elem in hrefs]
         print(hashtag + ' photos: '+str(len(pic_hrefs)))

         for pic_href in pic_hrefs:
            driver.get(pic_href)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            try:
                time.sleep(4)
                like_button = lambda: driver.find_element_by_xpath("//span[@aria-label='Like']")
                like_button().click()
                time.sleep(15)
            except Exception as e:
                print(e)
                time.sleep(2)


kevinIG = InstagramBot("testreponic123", 'Test123')
kevinIG.login()
kevinIG.like_photo(["test1234567890", "test123test"])
kevinIG.closeBrowser()