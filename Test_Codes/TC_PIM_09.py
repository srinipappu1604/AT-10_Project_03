from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from Test_Data import data
import pytest
import time

class Test_TCPIM09:
    url = "https://opensource-demo.orangehrmlive.com"
    
    @pytest.fixture
    def booting_function(self):
        try:
            self.driver = webdriver.Firefox()
            yield
            self.driver.close()
        except:
            print("ERROR IN THE FUCTION - booting_function")
            
    def test_tcpim09(self,booting_function):
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
            
            self.driver.find_element(by=By.XPATH, value =data.Orange_Selectors.employee_list).click()
            time.sleep(5)
            
            self.driver.find_element(by=By.XPATH, value =data.Orange_Selectors.edit_button).click()
            time.sleep(5)
            
            self.driver.find_element(by=By.XPATH, value =data.Orange_Selectors.job_details).click()
            time.sleep(5)
            
            self.driver.find_element(by=By.XPATH, value =data.Orange_Selectors.joined_date_job).send_keys(data.Job_Details.joineddate)
            time.sleep(5)
            
            job_tit = self.driver.find_element(by=By.XPATH, value =data.Orange_Selectors.job_title_job)
            action = ActionChains(self.driver)
            action.click(on_element=job_tit).perform()
            time.sleep(5)
            self.driver.find_element(by=By.XPATH, value =data.Orange_Selectors.job_title_job).click()
            time.sleep(5)
            
            job_cat = self.driver.find_element(by=By.XPATH, value =data.Orange_Selectors.job_category_job)
            action = ActionChains(self.driver)
            action.click(on_element=job_cat).perform()
            time.sleep(5)
            self.driver.find_element(by=By.XPATH, value =data.Orange_Selectors.job_category_job).click()
            time.sleep(5)
            
            sub_un = self.driver.find_element(by=By.XPATH, value =data.Orange_Selectors.sub_unit_job)
            action = ActionChains(self.driver)
            action.click(on_element=sub_un).perform()
            time.sleep(5)
            self.driver.find_element(by=By.XPATH, value =data.Orange_Selectors.sub_unit_job).click()
            time.sleep(5)
            
            loca_tion = self.driver.find_element(by=By.XPATH, value =data.Orange_Selectors.location_job)
            action = ActionChains(self.driver)
            action.click(on_element=loca_tion).perform()
            time.sleep(5)
            self.driver.find_element(by=By.XPATH, value =data.Orange_Selectors.location_job).click()
            time.sleep(5)
            
            employ_ment = self.driver.find_element(by=By.XPATH, value =data.Orange_Selectors.employment_status_job)
            action = ActionChains(self.driver)
            action.click(on_element=employ_ment).perform()
            time.sleep(5)
            self.driver.find_element(by=By.XPATH, value =data.Orange_Selectors.employment_status_job).click()
            time.sleep(5)
            
            self.driver.find_element(by=By.XPATH, value =data.Orange_Selectors.include_employment_contract_details_job).click()
            time.sleep(5)
            
            self.driver.find_element(by=By.XPATH, value =data.Orange_Selectors.contract_start_date_job).send_keys(data.Job_Details.contractstartdate)
            time.sleep(5)
            
            self.driver.find_element(by=By.XPATH, value =data.Orange_Selectors.contract_end_date_job).send_keys(data.Job_Details.contractenddate)
            time.sleep(5)
            
            self.driver.find_element(by=By.XPATH, value =data.Orange_Selectors.contract_details_job).click()
            time.sleep(5)
            
            self.driver.find_element(by=By.XPATH, value =data.Orange_Selectors.save_job).click()
            time.sleep(5)
            print("SUCCESS # Updated Job Details")
            
            time.sleep(5)
            cookie_after_login = self.driver.get_cookies()
            cookie_after_login = cookie_after_login[0]['value']
            print("Cookie Value after Login # ", cookie_after_login)
            if(cookie_home_page != cookie_after_login):
                print("SUCCESS # Login Success. Previous Cookie ID before Login is {a} and after login Cookie ID is {b}".format(a=cookie_home_page, b=cookie_after_login))
        except:
            print("ERROR IN THE FUCTION - test_tcpim09")
