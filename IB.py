<<<<<<< HEAD
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 



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
        time.sleep(2)
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
    
    def like_photo(self, hashtag) :
        driver = self.driver
        driver.get("https://www.instagram.com/explore/tags/"+hashtag+"/")
        time.sleep(2)
        for i in range (1, 3):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)

        hrefs = driver.find_element_by_tag_name("a")
        pic_hrefs = [elem.get_attribute("href") for elem in hrefs]
        pic_hrefs = [href for href in pic_hrefs if hashtag in href]
        print(hashtag + ' photos: '+str(len(pic_hrefs)))

        for pic_href in pic_hrefs:
            driver.get(pic_href)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            try:
                driver.find_element_by_link_text("Like").click()
                time.sleep(20)
            except Exception as e:
                time.sleep(2)

kevinIG = InstagramBot("testreponic123", 'Test123')
kevinIG.login()
kevinIG.like_photo("newyork")
=======
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 



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
        time.sleep(2)
        # "//a[@href'accounts/login']"
        # "//input[@name='username']"
        # "//input[@name='password']"

        kevinIG = InstagramBot("awesomePossum98765", 'Password12345')
        kevinIG.login()
>>>>>>> f11d89273c11eef078ad59b13d699567b0574043
