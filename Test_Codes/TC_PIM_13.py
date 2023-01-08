from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from Test_Data import data
import pytest
import time

class Test_TCPIM13:
    url = "https://opensource-demo.orangehrmlive.com"
    
    @pytest.fixture
    def booting_function(self):
        try:
            self.driver = webdriver.Edge()
            yield
            self.driver.close()
        except:
            print("ERROR IN THE FUCTION - booting_function")
            
    def test_tcpim13(self,booting_function):
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
            
            self.driver.find_element(by=By.XPATH, value =data.Orange_Selectors.tax_exemptions).click()
            time.sleep(5)
            
            
            status_tax_exemp = self.driver.find_element(by=By.XPATH, value =data.Orange_Selectors.status_tax_exemptions)
            action = ActionChains(self.driver)
            action.click(on_element=status_tax_exemp).perform()
            time.sleep(5)
            self.driver.find_element(by=By.XPATH, value =data.Orange_Selectors.status_tax_exemptions).click()
            time.sleep(5)
            
            self.driver.find_element(by=By.XPATH, value =data.Orange_Selectors.exemptions_tax_exemptions).send_keys(data.Tax_Exemptions.exemptions)
            time.sleep(5)
            
            state_state = self.driver.find_element(by=By.XPATH, value =data.Orange_Selectors.state_state_income_tax)
            action = ActionChains(self.driver)
            action.click(on_element=state_state).perform()
            time.sleep(5)
            self.driver.find_element(by=By.XPATH, value =data.Orange_Selectors.state_state_income_tax).click()
            time.sleep(5)
            
            status_state = self.driver.find_element(by=By.XPATH, value =data.Orange_Selectors.status_state_income_tax)
            action = ActionChains(self.driver)
            action.click(on_element=status_state).perform()
            time.sleep(5)
            self.driver.find_element(by=By.XPATH, value =data.Orange_Selectors.status_state_income_tax).click()
            time.sleep(5)
            
            self.driver.find_element(by=By.XPATH, value =data.Orange_Selectors.exemptions_state_income_tax).send_keys(data.Tax_Exemptions.exemptionsstateincometax)
            time.sleep(5)
            
            unemployee_state = self.driver.find_element(by=By.XPATH, value =data.Orange_Selectors.unemployment_state_state_income_tax)
            action = ActionChains(self.driver)
            action.click(on_element=unemployee_state).perform()
            time.sleep(5)
            self.driver.find_element(by=By.XPATH, value =data.Orange_Selectors.unemployment_state_state_income_tax).click()
            time.sleep(5)
            
            work_sta = self.driver.find_element(by=By.XPATH, value =data.Orange_Selectors.work_state_state_income_tax)
            action = ActionChains(self.driver)
            action.click(on_element=work_sta).perform()
            time.sleep(5)
            self.driver.find_element(by=By.XPATH, value =data.Orange_Selectors.work_state_state_income_tax).click()
            time.sleep(5)
            
            self.driver.find_element(by=By.XPATH, value =data.Orange_Selectors.save_tax_exemptions).click()
            time.sleep(5)
            print("SUCCESS # Updated Tax Exemptions")
            
            time.sleep(5)
            cookie_after_login = self.driver.get_cookies()
            cookie_after_login = cookie_after_login[0]['value']
            print("Cookie Value after Login # ", cookie_after_login)
            if(cookie_home_page != cookie_after_login):
                print("SUCCESS # Login Success. Previous Cookie ID before Login is {a} and after login Cookie ID is {b}".format(a=cookie_home_page, b=cookie_after_login))
        except:
            print("ERROR IN THE FUCTION - test_tcpim13")
