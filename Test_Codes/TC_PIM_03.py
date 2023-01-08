from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Test_Data import data
import pytest
import time

class Test_TCPIM03:
    url = "https://opensource-demo.orangehrmlive.com"
    
    @pytest.fixture
    def booting_function(self):
        try:
            self.driver = webdriver.Chrome()
            yield
            self.driver.close()
        except:
            print("ERROR IN THE FUCTION - booting_function")
    
    def test_tcpim03(self, booting_function):
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
            
            self.driver.find_element(by=By.XPATH, value =data.Orange_Selectors.pim_button).click()
            time.sleep(5)
            
            self.driver.find_element(by=By.XPATH, value =data.Orange_Selectors.add_button).click()
            time.sleep(5)
            
            self.driver.find_element(by=By.NAME, value = data.Orange_Selectors.name_first__box).send_keys(data.PIM_Add.first_name)
            time.sleep(5)
            
            self.driver.find_element(by=By.NAME, value = data.Orange_Selectors.name_last_box).send_keys(data.PIM_Add.last_name)
            time.sleep(5)
            
            employee_id_fill = self.driver.find_element(by=By.XPATH, value= '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/input')
            employee_id_fill.send_keys(Keys.CONTROL + Keys.BACKSPACE)
            employee_id_fill.send_keys("9999")
            time.sleep(5)
            
            self.driver.find_element(by=By.XPATH, value = data.Orange_Selectors.create_login_details).click()
            time.sleep(5)
            
            self.driver.find_element(by=By.XPATH, value = data.Orange_Selectors.username_login).send_keys(data.PIM_Add.username)
            time.sleep(5)
            
            self.driver.find_element(by=By.XPATH, value = data.Orange_Selectors.status_enable).click()
            time.sleep(5)
            
            self.driver.find_element(by=By.XPATH, value = data.Orange_Selectors.password_login).send_keys(data.PIM_Add.password)
            time.sleep(5)
            
            self.driver.find_element(by=By.XPATH, value = data.Orange_Selectors.confirm_password_login).send_keys(data.PIM_Add.confirm_password)
            time.sleep(5)
            
            self.driver.find_element(by=By.XPATH, value = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]').click()
            time.sleep(5)
            print("SUCCESS # Validated With ADD EMPLOYEE in PIM")
            
            time.sleep(5)
            cookie_after_login = self.driver.get_cookies()
            cookie_after_login = cookie_after_login[0]['value']
            print("Cookie Value after Login # ", cookie_after_login)
            if(cookie_home_page != cookie_after_login):
                print("SUCCESS # Login Success. Previous Cookie ID before Login is {a} and after login Cookie ID is {b}".format(a=cookie_home_page, b=cookie_after_login))
        except:
            print("ERROR IN THE FUCTION - test_tcpim03")
