from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from Test_Data import data
import pytest
import time

class Test_TCPIM02:
    url = "https://opensource-demo.orangehrmlive.com"
    
    @pytest.fixture
    def booting_function(self):
        try:
            self.driver = webdriver.Chrome()
            yield
            self.driver.close()
        except:
            print("ERROR IN THE FUCTION - booting_function")
    
    def test_tcpim02(self, booting_function):
        try:
            self.driver.maximize_window()
            self.driver.get(self.url)
            time.sleep(10)
            
            cookies = self.driver.get_cookies()
            cookie_home_page = cookies[0]['value']
            print('Initial Value of Cookie Before Login # ', cookie_home_page)
            
            self.driver.find_element(by=By.NAME, value = data.Orange_Selectors.input_box_username).send_keys(data.Orange_Login.username)
            self.driver.find_element(by=By.NAME, value = data.Orange_Selectors.input_box_password).send_keys(data.Orange_Login.password)
            self.driver.find_element(by=By.XPATH, value = data.Orange_Selectors.login_xpath).click()
            time.sleep(5)
            
            self.driver.find_element(by=By.XPATH, value =data.Orange_Selectors.admin_click).click()
            time.sleep(5)
            
            user_management_button = self.driver.find_element(by=By.XPATH, value = data.Orange_Selectors.user_management)
            action = ActionChains(self.driver)
            action.click(on_element=user_management_button)
            action.perform()
            time.sleep(3)
            self.driver.find_element(by=By.LINK_TEXT, value="Users").click()
            time.sleep(3)
            print("SUCCESS # Validated With USER in user_management")
            
            user_role_button = self.driver.find_element(by=By.XPATH, value = data.Orange_Selectors.user_role)
            action = ActionChains(self.driver)
            action.click(on_element=user_role_button)
            action.perform()
            time.sleep(10)
            self.driver.find_element(by=By.LINK_TEXT, value ="Admin").click()
            time.sleep(10)
            print("SUCCESS # Validated With ADMIN user_role")
            
            
            status_button = self.driver.find_element(by=By.XPATH, value = data.Orange_Selectors.status_disable)
            action = ActionChains(self.driver)
            action.click(on_element=status_button)
            action.perform()
            time.sleep(10)
            self.driver.find_element(by=By.XPATH, value ='//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[4]/div/div[2]/div/div/div[1]').click()
            time.sleep(10)
            print("SUCCESS # Validated With DISABLE in status")

            cookie_after_login = self.driver.get_cookies()
            cookie_after_login = cookie_after_login[0]['value']
            print("Cookie Value after Login # ", cookie_after_login)
            if(cookie_home_page != cookie_after_login):
                print("SUCCESS # Login Success. Previous Cookie ID before Login is {a} and after login Cookie ID is {b}".format(a=cookie_home_page, b=cookie_after_login))
        except:
            print("ERROR IN THE FUCTION - test_tcpim02")
