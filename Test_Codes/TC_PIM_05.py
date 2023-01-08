from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from Test_Data import data
import pytest
import time

class Test_TCPIM05:
    url = "https://opensource-demo.orangehrmlive.com"
    
    @pytest.fixture
    def booting_function(self):
        try:
            self.driver = webdriver.Edge()
            yield
            self.driver.close()
        except:
            print("ERROR IN THE FUCTION - booting_function")
            
    def test_tcpim05(self,booting_function):
        try:
            self.driver.maximize_window()
            self.driver.get(self.url)
            time.sleep(3)
            cookies = self.driver.get_cookies()
            cookie_home_page = cookies[0]['value']
            print('Initial Value of Cookie Before Login # ', cookie_home_page)
            
            self.driver.find_element(by=By.NAME, value = data.Orange_Selectors.input_box_username).send_keys(data.Orange_Login.username)
            self.driver.find_element(by=By.NAME, value = data.Orange_Selectors.input_box_password).send_keys(data.Orange_Login.password)
            self.driver.find_element(by=By.XPATH, value = data.Orange_Selectors.login_xpath).click()
            time.sleep(5)
            
            self.driver.find_element(by=By.XPATH, value =data.Orange_Selectors.pim_button).click()
            time.sleep(5)
            
            self.driver.find_element(by=By.XPATH, value =data.Orange_Selectors.employee_list).click()
            time.sleep(5)
            
            self.driver.find_element(by=By.XPATH, value =data.Orange_Selectors.edit_button).click()
            time.sleep(5)
            
            self.driver.find_element(by=By.XPATH, value =data.Orange_Selectors.personal_details).click()
            time.sleep(5)
            
            self.driver.find_element(by=By.XPATH, value =data.Orange_Selectors.nick_name).send_keys(data.Personal_Details.nickname)
            time.sleep(5)
            
            self.driver.find_element(by=By.XPATH, value =data.Orange_Selectors.other_details).send_keys(data.Personal_Details.otherdetails)
            time.sleep(5)
            
            self.driver.find_element(by=By.XPATH, value =data.Orange_Selectors.ssn_number).send_keys(data.Personal_Details.ssn)
            time.sleep(5)
            
            self.driver.find_element(by=By.XPATH, value =data.Orange_Selectors.sin_number).send_keys(data.Personal_Details.sin)
            time.sleep(5)
            
            nationality_button = self.driver.find_element(by=By.XPATH, value = data.Orange_Selectors.nationality)
            action = ActionChains(self.driver)
            action.click(on_element=nationality_button)
            action.perform()
            time.sleep(3)
            self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[1]/div/div[2]/div/div').click()
            time.sleep(3)
            
            marital_status_button = self.driver.find_element(by=By.XPATH, value = data.Orange_Selectors.marital_status)
            action = ActionChains(self.driver)
            action.click(on_element=marital_status_button)
            action.perform()
            time.sleep(3)
            self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[2]/div/div[2]/div/div/div[1]').click()
            time.sleep(3)
            
            self.driver.find_element(by=By.XPATH, value =data.Orange_Selectors.date_of_birth).send_keys(data.Personal_Details.dateofbirth)
            time.sleep(5)
            
            self.driver.find_element(by=By.XPATH, value =data.Orange_Selectors.gender_box).click()
            time.sleep(5)
            
            self.driver.find_element(by=By.XPATH, value =data.Orange_Selectors.military_service).send_keys(data.Personal_Details.militaryservice)
            time.sleep(5)
            
            self.driver.find_element(by=By.XPATH, value =data.Orange_Selectors.save_button).click()
            time.sleep(5)
            print("SUCCESS # Filled All Personal Details")
            
            time.sleep(5)
            cookie_after_login = self.driver.get_cookies()
            cookie_after_login = cookie_after_login[0]['value']
            print("Cookie Value after Login # ", cookie_after_login)
            if(cookie_home_page != cookie_after_login):
                print("SUCCESS # Login Success. Previous Cookie ID before Login is {a} and after login Cookie ID is {b}".format(a=cookie_home_page, b=cookie_after_login))
        except:
            print("ERROR IN THE FUCTION - test_tcpim05")
