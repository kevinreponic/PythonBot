from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import firebase_admin
from firebase_admin import credentials, db
import time


class InstagramBot: 

    def __init__(self, username, password):        
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox()
        cred = credentials.Certificate('./ServiceKey/igbot-python-firebase-adminsdk-zxoyd-e30fb4aa6a.json')
        firebase_admin.initialize_app(cred, {
            'databaseURL' : 'https://igbot-python.firebaseio.com/'
        })


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

    def getFollowers(self):
        driver = self.driver
        driver.get('https://www.instagram.com/instagram')
        followers_button =  driver.find_element_by_xpath('/html/body/span/section/main/div/header/section/ul/li[2]/a')
        followers_button.click()
        time.sleep(2)
        for i in range(1,10):
            followers_window= driver.find_elements_by_xpath("/html/body/div[3]/div/div/div[2]/ul/div/li")[-1]
            followers_window.location_once_scrolled_into_view
            time.sleep(2)
        
        followers= driver.find_elements_by_xpath("/html/body/div[3]/div/div/div[2]/ul/div/li/div/div[1]/div[2]/div[1]/a")
        followers_hrefs = [elem.get_attribute('href') for elem in followers]

        for follower_href in followers_hrefs : 
            driver.get(follower_href)
            try:
                follower_username = driver.find_element_by_xpath("/html/body/span/section/main/div/header/section/div[1]/h1").get_attribute('innerHTML')
                follower_name = driver.find_element_by_xpath("/html/body/span/section/main/div/header/section/div[2]/h1").get_attribute('innerHTML')
                follower_bio = driver.find_element_by_xpath("/html/body/span/section/main/div/header/section/div[2]/span").get_attribute('innerHTML')
                for i in range (1, 5) :  
                 driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                 time.sleep(2)
                follower_photos = driver.find_elements_by_xpath("/html/body/span/section/main/div/div/article/div/div/div/div/a")
                follower_photos_hrefs = [elem.get_attribute("href") for elem in follower_photos]       
                                                    
                follower = {
                "username" : follower_username,
                "name" : follower_name,
                "bio" : follower_bio,
                }
                follower_push = db.reference('/users/testreponic123/followers').push(follower)
                time.sleep(2)
                push_key = follower_push.key
                for follower_photo_href in follower_photos_hrefs :
                    driver.get(follower_photo_href)
                    time.sleep(2)
                    photo_likes = driver.find_element_by_xpath('/html/body/span/section/main/div/div/article/div[2]/section[2]/div/div/a/span').get_attribute('innerHTML')
                    photo_caption = driver.find_element_by_xpath('/html/body/span/section/main/div/div/article/div[2]/div[1]/ul/li[1]/div/div/div/div/span').get_attribute('innerHTML')
                    comments_elements = driver.find_elements_by_xpath('/html/body/span/section/main/div/div/article/div[2]/div[1]/ul/li/div/div/div/div/span')
                    photo_comments = [elem.get_attribute('innerHTML') for elem in comments_elements]
                    photo = {
                        'likes' : photo_likes,
                        'caption' : photo_caption,
                        'comments' : photo_comments
                    }
                    db.reference('/users/testreponic123/followers/'+push_key+'/photos/feed/').push(photo)
                    time.sleep(3)
                
                time.sleep(10)
            except Exception as e:
                print(e)
                time.sleep(3)
        
igBot = InstagramBot("testreponic123", "Test123")
igBot.login()
igBot.getFollowers()


