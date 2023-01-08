from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from Test_Data import data
import pytest
import time

class Test_TCPIM10:
    url = "https://opensource-demo.orangehrmlive.com"
    
    @pytest.fixture
    def booting_function(self):
        try:
            self.driver = webdriver.Firefox()
            yield
            self.driver.close()
        except:
            print("ERROR IN THE FUCTION - booting_function")
            
    def test_tcpim10(self,booting_function):
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
            
            self.driver.find_element(by=By.XPATH, value =data.Orange_Selectors.job_details).click()
            time.sleep(5)
            
            self.driver.find_element(by=By.XPATH, value =data.Orange_Selectors.terminate_employment).click()
            time.sleep(5)
            
            self.driver.find_element(by=By.XPATH, value =data.Orange_Selectors.termination_date).send_keys(data.Job_Details.terminationdate)
            time.sleep(5)
            
            termination_reason_send = self.driver.find_element(by=By.XPATH, value = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div/div/form/div[2]/div/div[2]/div/div/div[1]')
            action = ActionChains(self.driver)
            action.click(on_element=termination_reason_send)
            action.perform()
            time.sleep(5)
            self.driver.find_element(by=By.XPATH, value = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div/div/form/div[2]/div/div[2]/div/div/div[1]').click()
            time.sleep(5)
            
            self.driver.find_element(by=By.XPATH, value =data.Orange_Selectors.note_job).send_keys(data.Job_Details.notejob)
            time.sleep(5)
            
            self.driver.find_element(by=By.XPATH, value =data.Orange_Selectors.save_job_terminate).click()
            time.sleep(5)
            print("SUCCESS # Employee Terminated")
            
            time.sleep(5)
            cookie_after_login = self.driver.get_cookies()
            cookie_after_login = cookie_after_login[0]['value']
            print("Cookie Value after Login # ", cookie_after_login)
            if(cookie_home_page != cookie_after_login):
                print("SUCCESS # Login Success. Previous Cookie ID before Login is {a} and after login Cookie ID is {b}".format(a=cookie_home_page, b=cookie_after_login))
        except:
            print("ERROR IN THE FUCTION - test_tcpim10")
