from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import firebase_admin
from firebase_admin import credentials, db
import time
import json
class InstagramBot: 

    def __init__(self, username, password):        
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox()
        cred = credentials.Certificate('./ServiceKey/igbot-python-firebase-adminsdk-zxoyd-e30fb4aa6a.json')
        firebase_admin.initialize_app(cred, {
            'databaseURL' : 'https://igbot-python.firebaseio.com/'
        })
        self.ref = db.reference('/users')
        
       
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
    
    def like_photo(self, hashtag) :
        driver = self.driver
        driver.get("https://www.instagram.com/explore/tags/"+hashtag+"/")
        time.sleep(2)
        for i in range (1, 3):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)

        hrefs = driver.find_elements_by_tag_name('a')
        pic_hrefs = [elem.get_attribute('href') for elem in hrefs]
        print(hashtag + ' photos: '+str(len(pic_hrefs)))

        for pic_href in pic_hrefs:
            driver.get(pic_href)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            try:
                time.sleep(4)
                like_button = lambda: driver.find_element_by_xpath("//span[@aria-label='Like']")
                like_button().click()
                photo_username = driver.find_element_by_xpath("/html/body/span/section/main/div/div/article/header/div[2]/div[1]/div[1]/h2/a").get_attribute("innerHTML")
                print("Username: "+photo_username)
                aux = {
                    "username" : photo_username,
                    "test" : "true"
                }
                
                self.ref.push(aux)

                time.sleep(15)
            except Exception as e:
                print(e)
                time.sleep(2)
    

kevinIG = InstagramBot("testreponic123", 'Test123')
kevinIG.login()
kevinIG.like_photo("paris")