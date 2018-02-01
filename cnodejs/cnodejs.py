from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

class CnodeJS(object):
    def __init__(self):
        pass

    #
    # def register(self,userName,passwd,repasswd,email):
    #     pass
    #
    # def active(self,userName):
    #     pass

    def login(self,driver,username,passwd):
        driver.get("http://118.31.19.120:3000/")
        loginlink = driver.find_element_by_css_selector('body > div.navbar > div > div > ul > li:nth-child(6) > a')
        loginlink.click()

        usernameInput = driver.find_element_by_id('name')

        usernameInput.clear()
        usernameInput.send_keys(username)

        passInput = driver.find_element_by_id('pass')
        passInput.clear()
        passInput.send_keys(passwd)
        driver.find_element_by_class_name('span-primary').click()
        loginUserName = driver.find_element_by_css_selector('#sidebar > div:nth-child(1) > div.inner > div > div > span.user_name > a').text
        driver.quit()
        return loginUserName


    def createATopic(self,driver,title,content):
        driver.find_element_by_class_name('span-success').click()

        assertVal = driver.find_element_by_class_name('active').text

        assert assertVal in "发布话题"

        option = driver.find_element_by_id('tab-value')

        option.click()

        ask = driver.find_element_by_css_selector('#tab-value > option:nth-child(3)')

        ask.click()

        titlearea = driver.find_element_by_id('title')
        titlearea.clear()
        titlearea.send_keys(title)

        contentArea = driver.find_element_by_css_selector(
            '#create_topic_form > fieldset > div > div > div.CodeMirror.cm-s-paper > div.CodeMirror-scroll')
        contentArea.click()

        ActionChains(driver).move_to_element(contentArea).key_down(Keys.COMMAND).send_keys('b').key_up(
            Keys.COMMAND).send_keys("abc").perform()  # 快捷键command+b
        ActionChains(driver).move_to_element(contentArea).send_keys(content).perform()

    def uploadimage(self,driver):
        driver.find_element_by_class_name("eicon-image").click()
        uploadimageInput = driver.find_element_by_class_name('webuploader-element-invisible')
        uploadimageInput.send_keys('/Users/liyirong/Desktop/view.jpg')
        time.sleep(2)

    def clickSubmit(self,driver):
        driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div[2]/form/fieldset/div/div/div[4]/input").submit()
