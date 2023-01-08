from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from Test_Data import data
import pytest
import time

class Test_TCPIM12:
    url = "https://opensource-demo.orangehrmlive.com"
    
    @pytest.fixture
    def booting_function(self):
        try:
            self.driver = webdriver.Edge()
            yield
            self.driver.close()
        except:
            print("ERROR IN THE FUCTION - booting_function")
            
    def test_tcpim12(self,booting_function):
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
            
            self.driver.find_element(by=By.XPATH, value =data.Orange_Selectors.salary_click).click()
            time.sleep(15)
            
            self.driver.find_element(by=By.XPATH, value =data.Orange_Selectors.add_salary).click()
            time.sleep(5)
            
            self.driver.find_element(by=By.XPATH, value =data.Orange_Selectors.salary_component_salary).send_keys(data.Salary_Details.salarycomponent)
            time.sleep(5)
            
            pay_grade = self.driver.find_element(by=By.XPATH, value =data.Orange_Selectors.pay_grade_salary)
            action = ActionChains(self.driver)
            action.click(on_element=pay_grade).perform()
            time.sleep(5)
            self.driver.find_element(by=By.XPATH, value =data.Orange_Selectors.pay_grade_salary).click()
            time.sleep(5)
            
            pay_frequency = self.driver.find_element(by=By.XPATH, value =data.Orange_Selectors.pay_frequency_salary)
            action = ActionChains(self.driver)
            action.click(on_element=pay_frequency).perform()
            time.sleep(3)
            self.driver.find_element(by=By.XPATH, value =data.Orange_Selectors.pay_frequency_salary).click()
            time.sleep(5)
            
            currency_sal = self.driver.find_element(by=By.XPATH, value =data.Orange_Selectors.currency_salary)
            action = ActionChains(self.driver)
            action.click(on_element=currency_sal).perform()
            time.sleep(3)
            self.driver.find_element(by=By.XPATH, value =data.Orange_Selectors.currency_salary).click()
            time.sleep(5)
            
            self.driver.find_element(by=By.XPATH, value =data.Orange_Selectors.amount_salary).send_keys(data.Salary_Details.amountsalary)
            time.sleep(5)
            
            self.driver.find_element(by=By.XPATH, value =data.Orange_Selectors.comments_salary).send_keys(data.Salary_Details.comments)
            time.sleep(5)
            
            self.driver.find_element(by=By.XPATH, value =data.Orange_Selectors.direct_deposit_details).click()
            time.sleep(5)
            
            self.driver.find_element(by=By.XPATH, value =data.Orange_Selectors.account_number_salary).send_keys(data.Salary_Details.accountnumbersalary)
            time.sleep(5)
            
            account_ty = self.driver.find_element(by=By.XPATH, value =data.Orange_Selectors.account_type_salary)
            action = ActionChains(self.driver)
            action.click(on_element=account_ty).perform()
            time.sleep(3)
            self.driver.find_element(by=By.XPATH, value =data.Orange_Selectors.account_type_salary).click()
            time.sleep(5)
            
            self.driver.find_element(by=By.XPATH, value =data.Orange_Selectors.routing_number_salary).send_keys(data.Salary_Details.routingnumbersalary)
            time.sleep(5)
            
            self.driver.find_element(by=By.XPATH, value =data.Orange_Selectors.amount_total_salary).send_keys(data.Salary_Details.amounttotalsalary)
            time.sleep(5)
            
            self.driver.find_element(by=By.XPATH, value =data.Orange_Selectors.save_salary).click()
            time.sleep(5)
            print("SUCCESS # Updated Salary Details")
            
            time.sleep(5)
            cookie_after_login = self.driver.get_cookies()
            cookie_after_login = cookie_after_login[0]['value']
            print("Cookie Value after Login # ", cookie_after_login)
            if(cookie_home_page != cookie_after_login):
                print("SUCCESS # Login Success. Previous Cookie ID before Login is {a} and after login Cookie ID is {b}".format(a=cookie_home_page, b=cookie_after_login))
        except:
            print("ERROR IN THE FUCTION - test_tcpim12")
