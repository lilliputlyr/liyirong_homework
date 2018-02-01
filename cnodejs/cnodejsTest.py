import unittest
from cnodejs import CnodeJS

from selenium import webdriver


driver = webdriver.Firefox()
class CnodeTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print(1)

    def setUp(self):
        print(2)

    def test_01login(self):
        assertuserName = CnodeJS().login(driver, 'liyirong','123456')
        # self.assertEqual('liyirong',assertuserName)

    def test_02login(self):
        assertuserName = CnodeJS().login(driver,'liyirong','123')
        # self.assertEqual('liyirong',assertuserName)

    # 发布帖子
    def test_postAtopic(self):
        CnodeJS().login(driver,"liyirong",'123456')
        CnodeJS().createATopic(driver,'lyr-标题','lyr-内容')
        CnodeJS().uploadimage(driver)
        CnodeJS().clickSubmit(driver)
    # 删除帖子
    # def test_deleteTopic(self):
    #     pass

    #
    # def tearDown(self):
    #     driver.save_screenshot('xxx.png')
    #
    # @classmethod
    # def tearDownClass(self):
    #     driver.quit()

def main():
    unittest.main()

if __name__ == '__main__':
    main()