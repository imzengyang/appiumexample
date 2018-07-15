from util.get_by_local import GetByLocal
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class IndexPage:

    def __init__(self,driver,i):
        self.driver = driver
        self.get_by_local = GetByLocal(self.driver)
	
    # 首页侧边栏按钮
    def get_traggle_button(self):
        return self.get_by_local.get_element('traggle_button')
    
    # 头像
    def get_avatar_button(self):
        return self.get_by_local.get_element('avatar')
    
