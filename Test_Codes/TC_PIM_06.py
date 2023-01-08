from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from Test_Data import data
import pytest
import time

class Test_TCPIM06:
    url = "https://opensource-demo.orangehrmlive.com"
    
    @pytest.fixture
    def booting_function(self):
        try:
            self.driver = webdriver.Edge()
            yield
            self.driver.close()
        except:
            print("ERROR IN THE FUCTION - booting_function")
            
    def test_tcpim06(self,booting_function):
        try:
            self.driver.maximize_window()
            self.driver.get(self.url)
            time.sleep(5)
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
            
            self.driver.find_element(by=By.XPATH, value =data.Orange_Selectors.contact_details).click()
            time.sleep(5)
            
            self.driver.find_element(by=By.XPATH, value =data.Orange_Selectors.street_1).send_keys(data.Contact_Details.street1)
            time.sleep(5)
            
            self.driver.find_element(by=By.XPATH, value =data.Orange_Selectors.street_2).send_keys(data.Contact_Details.street2)
            time.sleep(5)
            
            self.driver.find_element(by=By.XPATH, value =data.Orange_Selectors.city).send_keys(data.Contact_Details.city)
            time.sleep(5)
            
            
            self.driver.find_element(by=By.XPATH, value =data.Orange_Selectors.state).send_keys(data.Contact_Details.state)
            time.sleep(5)
            
            self.driver.find_element(by=By.XPATH, value =data.Orange_Selectors.zip_code).send_keys(data.Contact_Details.zip)
            time.sleep(5)
            
            country_select = self.driver.find_element(by=By.XPATH, value=data.Orange_Selectors.country)
            action = ActionChains(self.driver)
            action.click(on_element=country_select).perform()
            time.sleep(3)
            self.driver.find_element(by=By.XPATH, value=data.Orange_Selectors.country)
            time.sleep(3)
            
            self.driver.find_element(by=By.XPATH, value =data.Orange_Selectors.home_telephone).send_keys(data.Contact_Details.home)
            time.sleep(5)
            
            self.driver.find_element(by=By.XPATH, value =data.Orange_Selectors.mobile_telephone).send_keys(data.Contact_Details.mobile)
            time.sleep(5)
            
            self.driver.find_element(by=By.XPATH, value =data.Orange_Selectors.work_telephone).send_keys(data.Contact_Details.work)
            time.sleep(5)
            
            self.driver.find_element(by=By.XPATH, value =data.Orange_Selectors.work_email).send_keys(data.Contact_Details.workemail)
            time.sleep(5)
            
            self.driver.find_element(by=By.XPATH, value =data.Orange_Selectors.other_email).send_keys(data.Contact_Details.otheremail)
            time.sleep(5)
            
            self.driver.find_element(by=By.XPATH, value =data.Orange_Selectors.save_contact).click()
            time.sleep(5)
            print("SUCCESS # Updated Employee Contact Details")
            
            time.sleep(5)
            cookie_after_login = self.driver.get_cookies()
            cookie_after_login = cookie_after_login[0]['value']
            print("Cookie Value after Login # ", cookie_after_login)
            if(cookie_home_page != cookie_after_login):
                print("SUCCESS # Login Success. Previous Cookie ID before Login is {a} and after login Cookie ID is {b}".format(a=cookie_home_page, b=cookie_after_login))
        except:
            print("ERROR IN THE FUCTION - test_tcpim06")
