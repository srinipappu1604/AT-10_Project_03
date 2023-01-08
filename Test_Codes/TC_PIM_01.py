from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Test_Data import data
import pytest
import time

class Test_TCPIM01:
    url = "https://opensource-demo.orangehrmlive.com"
    
    @pytest.fixture
    def booting_function(self):
        try:
            self.driver = webdriver.Firefox()
            yield
            self.driver.close()
        except:
            print("ERROR IN THE FUCTION - booting_function")
    
    def test_tcpim01(self, booting_function):
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
            
            admin_button = self.driver.find_element(by=By.XPATH, value=data.Orange_Selectors.search_box)
            admin_button.send_keys(data.Text_Box.admin)
            self.driver.find_element(by=By.XPATH,value=data.Orange_Selectors.admin_click).click()
            time.sleep(7)
            print("SUCCESS # Validated With lower case admin")
            
            ADMIN_button = self.driver.find_element(by=By.XPATH, value=data.Orange_Selectors.search_box)
            ADMIN_button.send_keys(data.Text_Box.ADMIN)
            self.driver.find_element(by=By.XPATH,value=data.Orange_Selectors.admin_click).click()
            time.sleep(7)
            print("SUCCESS # Validated With upper case ADMIN")
            
            pim_button = self.driver.find_element(by=By.XPATH, value=data.Orange_Selectors.search_box)
            pim_button.send_keys(data.Text_Box.pim)
            self.driver.find_element(by=By.XPATH,value=data.Orange_Selectors.pim).click()
            time.sleep(7)
            print("SUCCESS # Validated With lower case pim")
            
            PIM_button = self.driver.find_element(by=By.XPATH, value=data.Orange_Selectors.search_box)
            PIM_button.send_keys(data.Text_Box.PIM)
            self.driver.find_element(by=By.XPATH,value=data.Orange_Selectors.pim).click()
            time.sleep(7)
            print("SUCCESS # Validated With upper case PIM")
            
            leave_button = self.driver.find_element(by=By.XPATH, value=data.Orange_Selectors.search_box)
            leave_button.send_keys(data.Text_Box.leave)
            self.driver.find_element(by=By.XPATH,value=data.Orange_Selectors.leave).click()
            time.sleep(7)
            print("SUCCESS # Validated With lower case leave")
            
            LEAVE_button = self.driver.find_element(by=By.XPATH, value=data.Orange_Selectors.search_box)
            LEAVE_button.send_keys(data.Text_Box.LEAVE)
            self.driver.find_element(by=By.XPATH,value=data.Orange_Selectors.leave).click()
            time.sleep(7)
            print("SUCCESS # Validated With upper case LEAVE")
            
            time_button = self.driver.find_element(by=By.XPATH, value=data.Orange_Selectors.search_box)
            time_button.send_keys(data.Text_Box.time)
            self.driver.find_element(by=By.XPATH,value=data.Orange_Selectors.time).click()
            time.sleep(7)
            print("SUCCESS # Validated With lower case time")
            
            TIME_button = self.driver.find_element(by=By.XPATH, value=data.Orange_Selectors.search_box)
            TIME_button.send_keys(data.Text_Box.TIME)
            self.driver.find_element(by=By.XPATH,value=data.Orange_Selectors.time).click()
            time.sleep(7)
            print("SUCCESS # Validated With upper case TIME")
            
            recruitment_button = self.driver.find_element(by=By.XPATH, value=data.Orange_Selectors.search_box)
            recruitment_button.send_keys(data.Text_Box.recruitment)
            self.driver.find_element(by=By.XPATH,value=data.Orange_Selectors.recruitment).click()
            time.sleep(7)
            print("SUCCESS # Validated With lower case recruitment")
            
            RECRUITMENT_button = self.driver.find_element(by=By.XPATH, value=data.Orange_Selectors.search_box)
            RECRUITMENT_button.send_keys(data.Text_Box.RECRUITMENT)
            self.driver.find_element(by=By.XPATH,value=data.Orange_Selectors.recruitment).click()
            time.sleep(7)
            print("SUCCESS # Validated With upper case RECRUITMENT")
            
            myinfo_button = self.driver.find_element(by=By.XPATH, value=data.Orange_Selectors.search_box)
            myinfo_button.send_keys(data.Text_Box.myinfo)
            self.driver.find_element(by=By.XPATH,value=data.Orange_Selectors.myinfo).click()
            time.sleep(7)
            print("SUCCESS # Validated With lower case myinfo")
            
            MYINFO_button = self.driver.find_element(by=By.XPATH, value=data.Orange_Selectors.search_box)
            MYINFO_button.send_keys(data.Text_Box.MYINFO)
            self.driver.find_element(by=By.XPATH,value=data.Orange_Selectors.myinfo).click()
            time.sleep(7)
            print("SUCCESS # Validated With upper case MYINFO")
            
            performance_button = self.driver.find_element(by=By.XPATH, value=data.Orange_Selectors.search_box)
            performance_button.send_keys(data.Text_Box.performance)
            self.driver.find_element(by=By.XPATH,value=data.Orange_Selectors.performance).click()
            time.sleep(7)
            print("SUCCESS # Validated With lower case performance")
            
            PERFORMANCE_button = self.driver.find_element(by=By.XPATH, value=data.Orange_Selectors.search_box)
            PERFORMANCE_button.send_keys(data.Text_Box.PERFORMANCE)
            self.driver.find_element(by=By.XPATH,value=data.Orange_Selectors.performance).click()
            time.sleep(7)
            print("SUCCESS # Validated With upper case PERFORMANCE")
            
            dashboard_button = self.driver.find_element(by=By.XPATH, value=data.Orange_Selectors.search_box)
            dashboard_button.send_keys(data.Text_Box.dashboard)
            self.driver.find_element(by=By.XPATH,value=data.Orange_Selectors.dashboard).click()
            time.sleep(7)
            print("SUCCESS # Validated With lower case dashboard")
            
            DASHBOARD_button = self.driver.find_element(by=By.XPATH, value=data.Orange_Selectors.search_box)
            DASHBOARD_button.send_keys(data.Text_Box.DASHBOARD)
            self.driver.find_element(by=By.XPATH,value=data.Orange_Selectors.dashboard).click()
            time.sleep(7)
            print("SUCCESS # Validated With upper case DASHBOARD")
            
            directory_button = self.driver.find_element(by=By.XPATH, value=data.Orange_Selectors.search_box)
            directory_button.send_keys(data.Text_Box.directory)
            self.driver.find_element(by=By.XPATH,value=data.Orange_Selectors.directory).click()
            time.sleep(7)
            print("SUCCESS # Validated With lower case directory")
            
            DIRECTORY_button = self.driver.find_element(by=By.XPATH, value=data.Orange_Selectors.search_box)
            DIRECTORY_button.send_keys(data.Text_Box.DIRECTORY)
            self.driver.find_element(by=By.XPATH,value=data.Orange_Selectors.directory).click()
            time.sleep(7)
            print("SUCCESS # Validated With upper case DIRECTORY")
            
            maintenance_button = self.driver.find_element(by=By.XPATH, value=data.Orange_Selectors.search_box)
            maintenance_button.send_keys(data.Text_Box.maintenance)
            self.driver.find_element(by=By.XPATH,value=data.Orange_Selectors.maintenance).click()
            time.sleep(5)
            self.driver.find_element(by=By.XPATH, value = data.Orange_Selectors.password_maintenance).send_keys(data.Orange_Login.password)
            self.driver.find_element(by=By.XPATH, value = data.Orange_Selectors.confirm_maintenance).click()
            time.sleep(7)
            print("SUCCESS # Validated With lower case maintenance")
            
            MAINTENANCE_button = self.driver.find_element(by=By.XPATH, value=data.Orange_Selectors.search_box)
            MAINTENANCE_button.send_keys(data.Text_Box.MAINTENANCE)
            self.driver.find_element(by=By.XPATH,value=data.Orange_Selectors.maintenance).click()
            time.sleep(7)
            print("SUCCESS # Validated With upper case MAINTENANCE")
            
            buzz_button = self.driver.find_element(by=By.XPATH, value=data.Orange_Selectors.search_box)
            buzz_button.send_keys(data.Text_Box.buzz)
            self.driver.find_element(by=By.XPATH,value=data.Orange_Selectors.buzz).click()
            time.sleep(7)
            print("SUCCESS # Validated With lower case buzz")
            
            BUZZ_button = self.driver.find_element(by=By.XPATH, value=data.Orange_Selectors.search_box)
            BUZZ_button.send_keys(data.Text_Box.BUZZ)
            self.driver.find_element(by=By.XPATH,value=data.Orange_Selectors.buzz).click()
            time.sleep(7)
            print("SUCCESS # Validated With upper case BUZZ")
            
            time.sleep(3)
            cookie_after_login = self.driver.get_cookies()
            cookie_after_login = cookie_after_login[0]['value']
            print("Cookie Value after Login # ", cookie_after_login)
            if(cookie_home_page != cookie_after_login):
                print("SUCCESS # Login Success. Previous Cookie ID before Login is {a} and after login Cookie ID is {b}".format(a=cookie_home_page, b=cookie_after_login))
        except:
            print("ERROR IN THE FUCTION - test_tcpim01")
