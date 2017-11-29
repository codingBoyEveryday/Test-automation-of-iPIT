import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# class Ipit(unittest.TestCase):
#
#     def setUp(self):
#         self.browser = webdriver.Chrome("C:\\Users\\zhou502\\Documents\\chromedriver.exe")
#
#     # def test_search_ipit_webpage(self):
#     def homePage(self):
#         browser = self.browser
#         browser.get("http://localhost:8070/")
#         # self.assertIn("iPIT", browser.title)
#
#     def tearDown(self):
#         self.browser.close()

# TODO Do we need to test if we cannot find the website


# class SignUp(unittest.TestCase):
#
#     def setUp(self):
#         self.browser = webdriver.Chrome("C:\\Users\\zhou502\\Documents\\chromedriver.exe")
#
#     def test_sign_up_username_empty(self):
#         browser = self.browser
#         browser.get("http://localhost:8070/")
#         time.sleep(3)
#
#         # print browser.find_elements_by_xpath("//span")
#
#         browser.find_elements_by_xpath("//span")[0].click()
#         self.assertIn("Signup", browser.title)
#         time.sleep(3)
#
#         username = browser.find_element_by_id("username")
#         username.send_keys("")
#         login_attempt = browser.find_element_by_xpath("//*[@type='submit']")
#         login_attempt.submit()
#
#         assert "User Name can't be empty." in browser.page_source
#         time.sleep(3)
#         self.browser.close()
#
#     def test_sign_up_username_exists(self):
#         browser = self.browser
#         browser.get("http://localhost:8070/")
#         time.sleep(3)
#
#         browser.find_elements_by_xpath("//span")[0].click()
#         self.assertIn("Signup", browser.title)
#         time.sleep(3)
#
#         username = browser.find_element_by_id("username")
#         username.send_keys("hanrong")
#         login_attempt = browser.find_element_by_xpath("//*[@type='submit']")
#         login_attempt.submit()
#
#         assert "This name already exists." in browser.page_source
#         time.sleep(3)
#         self.browser.close()
#
#     def test_sign_up_username_not_valid(self):
#         browser = self.browser
#         browser.get("http://localhost:8070/")
#         time.sleep(3)
#
#         browser.find_elements_by_xpath("//span")[0].click()
#         self.assertIn("Signup", browser.title)
#         time.sleep(3)
#
#         username = browser.find_element_by_id("username")
#         username.send_keys("1")
#         login_attempt = browser.find_element_by_xpath("//*[@type='submit']")
#         login_attempt.submit()
#
#         assert "Name must be 3 t 20 letters or digits or - or _ or . " in browser.page_source
#         time.sleep(3)
#         self.browser.close()


# class Login(unittest.TestCase):
#
#     def setUp(self):
#         self.browser = webdriver.Chrome("C:\\Users\\zhou502\\Documents\\chromedriver.exe")
#
#     def test_login_username_empty(self):
#         browser = self.browser
#         browser.get("http://localhost:8070/")
#         time.sleep(3)
#
#         browser.find_elements_by_xpath("//span")[1].click()
#         self.assertIn("Login", browser.title)
#         time.sleep(3)
#
#         username = browser.find_element_by_id("username")
#         username.send_keys("")
#         login_attempt = browser.find_element_by_xpath("//*[@type='submit']")
#         login_attempt.submit()
#
#         assert "User Name can't be empty." in browser.page_source
#         time.sleep(3)
#         self.browser.close()
#
#     def test_login_username_not_valid(self):
#         browser = self.browser
#         browser.get("http://localhost:8070/")
#         time.sleep(3)
#
#         browser.find_elements_by_xpath("//span")[1].click()
#         self.assertIn("Login", browser.title)
#         time.sleep(3)
#
#         username = browser.find_element_by_id("username")
#         username.send_keys("1")
#         login_attempt = browser.find_element_by_xpath("//*[@type='submit']")
#         login_attempt.submit()
#
#         assert "Name must be 3 t 20 letters or digits or - or _ or . " in browser.page_source
#         time.sleep(3)
#         self.browser.close()
#
#     def test_login_username_not_exists(self):
#         browser = self.browser
#         browser.get("http://localhost:8070/")
#         time.sleep(3)
#
#         browser.find_elements_by_xpath("//span")[1].click()
#         self.assertIn("Login", browser.title)
#         time.sleep(3)
#
#         username = browser.find_element_by_id("username")
#         username.send_keys("yeghesh")
#         login_attempt = browser.find_element_by_xpath("//*[@type='submit']")
#         login_attempt.submit()
#
#         assert "This username doesn't exists." in browser.page_source
#         time.sleep(3)
#         self.browser.close()
#
#     def test_login_password_empty(self):
#         pass
#
#     def test_login_password_not_match(self):
#         pass
#
#     def test_login_password_match(self):
#         pass
#
#     def tearDown(self):
#         self.browser.close()


# class Project(unittest.TestCase):
#
#     def test_go_to_project(self):
#         # go to the homepage
#         self.browser = webdriver.Chrome("C:\\Users\\zhou502\\Documents\\chromedriver.exe")
#
#         browser = self.browser
#         browser.get("http://localhost:8070/")
#         time.sleep(3)
#
#         browser.find_elements_by_xpath("//span")[1].click()
#         # self.assertIn("Login", browser.title)
#         time.sleep(3)
#         # login as an admin
#         username = browser.find_element_by_id("username")
#         password = browser.find_element_by_id("password")
#         username.send_keys("hanrong")
#         password.send_keys("640519")
#         time.sleep(3)
#
#         login_attempt = browser.find_element_by_xpath("//*[@type='submit']")
#         login_attempt.submit()
#         time.sleep(3)
#
#         browser.find_elements_by_link_text("Projects & maintenance")[0].click()
#         self.assertIn("Projects", browser.title)
#         time.sleep(3)
#
#         self.browser.close()
#
#     def test_project_add_project(self):
#         self.browser = webdriver.Chrome("C:\\Users\\zhou502\\Documents\\chromedriver.exe")
#
#         browser = self.browser
#         browser.get("http://localhost:8070/")
#         time.sleep(3)
#
#         browser.find_elements_by_xpath("//span")[1].click()
#         # self.assertIn("Login", browser.title)
#         time.sleep(3)
#
#         username = browser.find_element_by_id("username")
#         password = browser.find_element_by_id("password")
#         username.send_keys("hanrong")
#         password.send_keys("640519")
#         time.sleep(3)
#
#         login_attempt = browser.find_element_by_xpath("//*[@type='submit']")
#         login_attempt.submit()
#         time.sleep(3)
#
#         browser.find_elements_by_link_text("Projects & maintenance")[0].click()
#         time.sleep(3)
#         browser.find_elements_by_name("user_action")[0].click()
#         self.assertIn("New Project", browser.title)
#
#         self.browser.close()
#
#     def test_project_add_project_name_empty(self):
#         self.browser = webdriver.Chrome("C:\\Users\\zhou502\\Documents\\chromedriver.exe")
#
#         browser = self.browser
#         browser.get("http://localhost:8070/")
#         time.sleep(3)
#
#         browser.find_elements_by_xpath("//span")[1].click()
#         # self.assertIn("Login", browser.title)
#         time.sleep(3)
#
#         username = browser.find_element_by_id("username")
#         password = browser.find_element_by_id("password")
#         username.send_keys("hanrong")
#         password.send_keys("640519")
#         time.sleep(3)
#
#         login_attempt = browser.find_element_by_xpath("//*[@type='submit']")
#         login_attempt.submit()
#         time.sleep(3)
#
#         browser.find_elements_by_link_text("Projects & maintenance")[0].click()
#         time.sleep(3)
#         browser.find_elements_by_name("user_action")[0].click()
#
#         name = browser.find_element_by_id("name")
#         name.send_keys("")
#         add_attempt = browser.find_element_by_xpath("//*[@type='submit']")
#         add_attempt.submit()
#         assert "Name can't be empty." in browser.page_source
#
#         self.browser.close()
#
#     def test_project_add_project_name_existing(self):
#         self.browser = webdriver.Chrome("C:\\Users\\zhou502\\Documents\\chromedriver.exe")
#         browser = self.browser
#         browser.get("http://localhost:8070/")
#         time.sleep(3)
#         browser.find_elements_by_xpath("//span")[1].click()
#         time.sleep(3)
#         username = browser.find_element_by_id("username")
#         password = browser.find_element_by_id("password")
#         username.send_keys("hanrong")
#         password.send_keys("640519")
#         time.sleep(3)
#         login_attempt = browser.find_element_by_xpath("//*[@type='submit']")
#         login_attempt.submit()
#         time.sleep(3)
#         browser.find_elements_by_link_text("Projects & maintenance")[0].click()
#         time.sleep(3)
#         browser.find_elements_by_name("user_action")[0].click()
#         name = browser.find_element_by_id("name")
#         name.send_keys("Rose")
#         add_attempt = browser.find_element_by_xpath("//*[@type='submit']")
#         add_attempt.submit()
#         assert "This name is already in use." in browser.page_source
#         self.browser.close()
#
#     def test_project_add_project_priority_empty(self):
#         self.browser = webdriver.Chrome("C:\\Users\\zhou502\\Documents\\chromedriver.exe")
#         browser = self.browser
#         browser.get("http://localhost:8070/")
#         time.sleep(3)
#         browser.find_elements_by_xpath("//span")[1].click()
#         time.sleep(3)
#         username = browser.find_element_by_id("username")
#         password = browser.find_element_by_id("password")
#         username.send_keys("hanrong")
#         password.send_keys("640519")
#         time.sleep(3)
#         login_attempt = browser.find_element_by_xpath("//*[@type='submit']")
#         login_attempt.submit()
#         time.sleep(3)
#         browser.find_elements_by_link_text("Projects & maintenance")[0].click()
#         time.sleep(3)
#         browser.find_elements_by_name("user_action")[0].click()
#         name = browser.find_element_by_id("name")
#         name.send_keys("Rose_1")  # please type a project name doesn't exist
#
#         priority = browser.find_element_by_xpath("//*[@id= 'priority']")
#         for option in priority.find_elements_by_tag_name('option'):
#             if option.text == '':
#                 option.click()
#                 break
#
#         add_attempt = browser.find_element_by_xpath("//*[@type='submit']")
#         add_attempt.submit()
#         assert "Please select a priority" in browser.page_source
#         self.browser.close()
#
#     def test_project_add_project_department_empty(self):
#         self.browser = webdriver.Chrome("C:\\Users\\zhou502\\Documents\\chromedriver.exe")
#         browser = self.browser
#         browser.get("http://localhost:8070/")
#         time.sleep(3)
#         browser.find_elements_by_xpath("//span")[1].click()
#         time.sleep(3)
#         username = browser.find_element_by_id("username")
#         password = browser.find_element_by_id("password")
#         username.send_keys("hanrong")
#         password.send_keys("640519")
#         time.sleep(3)
#         login_attempt = browser.find_element_by_xpath("//*[@type='submit']")
#         login_attempt.submit()
#         time.sleep(3)
#         browser.find_elements_by_link_text("Projects & maintenance")[0].click()
#         time.sleep(3)
#         browser.find_elements_by_name("user_action")[0].click()
#         name = browser.find_element_by_id("name")
#         name.send_keys("Rose_1")  # please type a project name doesn't exist
#         time.sleep(3)
#
#         priority = browser.find_element_by_xpath("//*[@id= 'priority']")
#         for option in priority.find_elements_by_tag_name('option'):
#             if option.text == 'Rood':
#                 option.click()
#                 break
#         time.sleep(3)
#
#         department = browser.find_element_by_xpath("//*[@id= 'department']")
#         for option in department.find_elements_by_tag_name('option'):
#             if option.text == '':
#                 option.click()
#                 break
#         time.sleep(3)
#
#         add_attempt = browser.find_element_by_xpath("//*[@type='submit']")
#         add_attempt.submit()
#         assert "Please select a department" in browser.page_source
#         self.browser.close()
#
#     def test_project_add_project_domain_empty(self):
#         self.browser = webdriver.Chrome("C:\\Users\\zhou502\\Documents\\chromedriver.exe")
#         browser = self.browser
#         browser.get("http://localhost:8070/")
#         time.sleep(3)
#         browser.find_elements_by_xpath("//span")[1].click()
#         time.sleep(3)
#         username = browser.find_element_by_id("username")
#         password = browser.find_element_by_id("password")
#         username.send_keys("hanrong")
#         password.send_keys("640519")
#         time.sleep(3)
#         login_attempt = browser.find_element_by_xpath("//*[@type='submit']")
#         login_attempt.submit()
#         time.sleep(3)
#         browser.find_elements_by_link_text("Projects & maintenance")[0].click()
#         time.sleep(3)
#         browser.find_elements_by_name("user_action")[0].click()
#         name = browser.find_element_by_id("name")
#         name.send_keys("Rose_1")  # please type a project name doesn't exist
#         time.sleep(3)
#
#         priority = browser.find_element_by_xpath("//*[@id= 'priority']")
#         for option in priority.find_elements_by_tag_name('option'):
#             if option.text == 'Rood':
#                 option.click()
#                 break
#         time.sleep(3)
#
#         department = browser.find_element_by_xpath("//*[@id= 'department']")
#         for option in department.find_elements_by_tag_name('option'):
#             if option.text == 'Innovation Test Data':
#                 option.click()
#                 break
#         time.sleep(3)
#
#         domain = browser.find_element_by_xpath("//*[@id= 'domain']")
#         for option in domain.find_elements_by_tag_name('option'):
#             if option.text == '':
#                 option.click()
#                 break
#         time.sleep(3)
#
#         add_attempt = browser.find_element_by_xpath("//*[@type='submit']")
#         add_attempt.submit()
#         assert "Please select a domain" in browser.page_source
#         self.browser.close()
#
#     def test_project_add_project_successfully(self):
#         self.browser = webdriver.Chrome("C:\\Users\\zhou502\\Documents\\chromedriver.exe")
#         browser = self.browser
#         browser.get("http://localhost:8070/")
#         time.sleep(3)
#         browser.find_elements_by_xpath("//span")[1].click()
#         time.sleep(3)
#         username = browser.find_element_by_id("username")
#         password = browser.find_element_by_id("password")
#         username.send_keys("hanrong")
#         password.send_keys("640519")
#         time.sleep(3)
#         login_attempt = browser.find_element_by_xpath("//*[@type='submit']")
#         login_attempt.submit()
#         time.sleep(3)
#         browser.find_elements_by_link_text("Projects & maintenance")[0].click()
#         time.sleep(3)
#         browser.find_elements_by_name("user_action")[0].click()
#         name = browser.find_element_by_id("name")
#         name.send_keys("Rose_1")  # please type a project name doesn't exist
#         time.sleep(3)
#
#         priority = browser.find_element_by_xpath("//*[@id= 'priority']")
#         for option in priority.find_elements_by_tag_name('option'):
#             if option.text == 'Rood':
#                 option.click()
#                 break
#         time.sleep(3)
#
#         department = browser.find_element_by_xpath("//*[@id= 'department']")
#         for option in department.find_elements_by_tag_name('option'):
#             if option.text == 'Innovation Test Data':
#                 option.click()
#                 break
#         time.sleep(3)
#
#         domain = browser.find_element_by_xpath("//*[@id= 'domain']")
#         for option in domain.find_elements_by_tag_name('option'):
#             if option.text == 'IT':
#                 option.click()
#                 break
#         time.sleep(3)
#
#         add_attempt = browser.find_element_by_xpath("//*[@type='submit']")
#         add_attempt.submit()
#         assert "Successfully added project Rose_1." in browser.page_source
#         self.browser.close()
#
#     def test_project_change_project(self):
#         pass
#
#     def test_project_delete_project(self):
#         self.browser = webdriver.Chrome("C:\\Users\\zhou502\\Documents\\chromedriver.exe")
#         browser = self.browser
#         browser.get("http://localhost:8070/")
#         time.sleep(3)
#         browser.find_elements_by_xpath("//span")[1].click()
#         time.sleep(3)
#         username = browser.find_element_by_id("username")
#         password = browser.find_element_by_id("password")
#         username.send_keys("hanrong")
#         password.send_keys("640519")
#         time.sleep(3)
#         login_attempt = browser.find_element_by_xpath("//*[@type='submit']")
#         login_attempt.submit()
#         time.sleep(3)
#         browser.find_elements_by_link_text("Projects & maintenance")[0].click()
#         time.sleep(3)
#
#         project_name = browser.find_element_by_link_text("Rooster")
#         project_name.click()
#         time.sleep(3)
#
#         del_attempt = browser.find_element_by_xpath("//*[@value='Delete']")
#         del_attempt.click()
#         time.sleep(3)
#         self.assertIn("Projects", browser.title)
#         self.browser.close()


# class Element(unittest.TestCase):
#
#     def test_go_to_element(self):
#         # go to the homepage
#         self.browser = webdriver.Chrome("C:\\Users\\zhou502\\Documents\\chromedriver.exe")
#
#         browser = self.browser
#         browser.get("http://localhost:8070/")
#         time.sleep(3)
#
#         browser.find_elements_by_xpath("//span")[1].click()
#         # self.assertIn("Login", browser.title)
#         time.sleep(3)
#         # login as an admin
#         username = browser.find_element_by_id("username")
#         password = browser.find_element_by_id("password")
#         username.send_keys("hanrong")
#         password.send_keys("640519")
#         time.sleep(3)
#
#         login_attempt = browser.find_element_by_xpath("//*[@type='submit']")
#         login_attempt.submit()
#         time.sleep(3)
#
#         browser.find_elements_by_link_text("Elements")[0].click()
#         self.assertIn("Element", browser.title)
#         time.sleep(3)
#
#         self.browser.close()
#
#     def test_element_go_to_new_domain(self):
#         self.browser = webdriver.Chrome("C:\\Users\\zhou502\\Documents\\chromedriver.exe")
#
#         browser = self.browser
#         browser.get("http://localhost:8070/")
#         time.sleep(3)
#
#         browser.find_elements_by_xpath("//span")[1].click()
#         # self.assertIn("Login", browser.title)
#         time.sleep(3)
#         # login as an admin
#         username = browser.find_element_by_id("username")
#         password = browser.find_element_by_id("password")
#         username.send_keys("hanrong")
#         password.send_keys("640519")
#         time.sleep(3)
#
#         login_attempt = browser.find_element_by_xpath("//*[@type='submit']")
#         login_attempt.submit()
#         time.sleep(3)
#
#         browser.find_elements_by_link_text("Elements")[0].click()
#         time.sleep(3)
#
#         new_domain = browser.find_element_by_xpath("//*[@value='new-domain']")
#         new_domain.click()
#         self.assertIn("New Domain", browser.title)
#         time.sleep(3)
#         self.browser.close()
#
#     def test_element_new_domain_domain_empty(self):
#         self.browser = webdriver.Chrome("C:\\Users\\zhou502\\Documents\\chromedriver.exe")
#
#         browser = self.browser
#         browser.get("http://localhost:8070/")
#         time.sleep(3)
#
#         browser.find_elements_by_xpath("//span")[1].click()
#         # self.assertIn("Login", browser.title)
#         time.sleep(3)
#         # login as an admin
#         username = browser.find_element_by_id("username")
#         password = browser.find_element_by_id("password")
#         username.send_keys("hanrong")
#         password.send_keys("640519")
#         time.sleep(3)
#
#         login_attempt = browser.find_element_by_xpath("//*[@type='submit']")
#         login_attempt.submit()
#         time.sleep(3)
#
#         browser.find_elements_by_link_text("Elements")[0].click()
#         time.sleep(3)
#
#         new_domain = browser.find_element_by_xpath("//*[@value='new-domain']")
#         new_domain.click()
#         time.sleep(3)
#
#         domain_name = browser.find_element_by_id("domain")
#         domain_name.send_keys("")
#         add_domain_attempt = browser.find_element_by_xpath("//*[@type='submit']")
#         add_domain_attempt.click()
#         assert "Domain can't be empty." in browser.page_source
#         time.sleep(3)
#         self.browser.close()
#
#     def test_element_new_domain_domain_existing(self):
#         self.browser = webdriver.Chrome("C:\\Users\\zhou502\\Documents\\chromedriver.exe")
#
#         browser = self.browser
#         browser.get("http://localhost:8070/")
#         time.sleep(3)
#
#         browser.find_elements_by_xpath("//span")[1].click()
#         # self.assertIn("Login", browser.title)
#         time.sleep(3)
#         # login as an admin
#         username = browser.find_element_by_id("username")
#         password = browser.find_element_by_id("password")
#         username.send_keys("hanrong")
#         password.send_keys("640519")
#         time.sleep(3)
#
#         login_attempt = browser.find_element_by_xpath("//*[@type='submit']")
#         login_attempt.submit()
#         time.sleep(3)
#
#         browser.find_elements_by_link_text("Elements")[0].click()
#         time.sleep(3)
#
#         new_domain = browser.find_element_by_xpath("//*[@value='new-domain']")
#         new_domain.click()
#         time.sleep(3)
#
#         domain_name = browser.find_element_by_id("domain")
#         domain_name.send_keys("VAS")
#         add_domain_attempt = browser.find_element_by_xpath("//*[@type='submit']")
#         add_domain_attempt.click()
#         time.sleep(3)
#
#         assert "The domain name already exists" in browser.page_source
#         time.sleep(3)
#         self.browser.close()
#
#     def test_element_new_domain_successfully(self):
#         self.browser = webdriver.Chrome("C:\\Users\\zhou502\\Documents\\chromedriver.exe")
#
#         browser = self.browser
#         browser.get("http://localhost:8070/")
#         time.sleep(3)
#
#         browser.find_elements_by_xpath("//span")[1].click()
#         # self.assertIn("Login", browser.title)
#         time.sleep(3)
#         # login as an admin
#         username = browser.find_element_by_id("username")
#         password = browser.find_element_by_id("password")
#         username.send_keys("hanrong")
#         password.send_keys("640519")
#         time.sleep(3)
#
#         login_attempt = browser.find_element_by_xpath("//*[@type='submit']")
#         login_attempt.submit()
#         time.sleep(3)
#
#         browser.find_elements_by_link_text("Elements")[0].click()
#         time.sleep(3)
#
#         new_domain = browser.find_element_by_xpath("//*[@value='new-domain']")
#         new_domain.click()
#         time.sleep(3)
#
#         domain_name = browser.find_element_by_id("domain")
#         domain_name.send_keys("hahaha")
#         add_domain_attempt = browser.find_element_by_xpath("//*[@type='submit']")
#         add_domain_attempt.click()
#         time.sleep(3)
#
#         assert "Domain hahaha added successfully." in browser.page_source
#         time.sleep(3)
#         self.browser.close()
#
#     def test_element_go_to_new_node(self):
#         self.browser = webdriver.Chrome("C:\\Users\\zhou502\\Documents\\chromedriver.exe")
#
#         browser = self.browser
#         browser.get("http://localhost:8070/")
#         time.sleep(3)
#
#         browser.find_elements_by_xpath("//span")[1].click()
#         # self.assertIn("Login", browser.title)
#         time.sleep(3)
#         # login as an admin
#         username = browser.find_element_by_id("username")
#         password = browser.find_element_by_id("password")
#         username.send_keys("hanrong")
#         password.send_keys("640519")
#         time.sleep(3)
#
#         login_attempt = browser.find_element_by_xpath("//*[@type='submit']")
#         login_attempt.submit()
#         time.sleep(3)
#
#         browser.find_elements_by_link_text("Elements")[0].click()
#         time.sleep(3)
#
#         new_domain = browser.find_element_by_xpath("//*[@value='node_info']")
#         new_domain.click()
#         self.assertIn("Node Info", browser.title)
#         time.sleep(3)
#         self.browser.close()
#
#     def test_element_new_node_node_empty(self):
#         self.browser = webdriver.Chrome("C:\\Users\\zhou502\\Documents\\chromedriver.exe")
#
#         browser = self.browser
#         browser.get("http://localhost:8070/")
#         time.sleep(3)
#
#         browser.find_elements_by_xpath("//span")[1].click()
#         # self.assertIn("Login", browser.title)
#         time.sleep(3)
#         # login as an admin
#         username = browser.find_element_by_id("username")
#         password = browser.find_element_by_id("password")
#         username.send_keys("hanrong")
#         password.send_keys("640519")
#         time.sleep(3)
#
#         login_attempt = browser.find_element_by_xpath("//*[@type='submit']")
#         login_attempt.submit()
#         time.sleep(3)
#
#         browser.find_elements_by_link_text("Elements")[0].click()
#         time.sleep(3)
#
#         new_domain = browser.find_element_by_xpath("//*[@value='node_info']")
#         new_domain.click()
#         time.sleep(3)
#
#         node_name = browser.find_element_by_id("node")
#         node_name.send_keys("")
#         add_node_attempt = browser.find_element_by_xpath("//*[@type='submit']")
#         add_node_attempt.click()
#         assert "Node name can't be empty." in browser.page_source
#         time.sleep(3)
#         self.browser.close()
#
#     def test_element_new_node_node_existing(self):
#         self.browser = webdriver.Chrome("C:\\Users\\zhou502\\Documents\\chromedriver.exe")
#
#         browser = self.browser
#         browser.get("http://localhost:8070/")
#         time.sleep(3)
#
#         browser.find_elements_by_xpath("//span")[1].click()
#         # self.assertIn("Login", browser.title)
#         time.sleep(3)
#         # login as an admin
#         username = browser.find_element_by_id("username")
#         password = browser.find_element_by_id("password")
#         username.send_keys("hanrong")
#         password.send_keys("640519")
#         time.sleep(3)
#
#         login_attempt = browser.find_element_by_xpath("//*[@type='submit']")
#         login_attempt.submit()
#         time.sleep(3)
#
#         browser.find_elements_by_link_text("Elements")[0].click()
#         time.sleep(3)
#
#         new_domain = browser.find_element_by_xpath("//*[@value='node_info']")
#         new_domain.click()
#         time.sleep(3)
#
#         node_name = browser.find_element_by_id("node")
#         node_name.send_keys("BSSD")
#         time.sleep(3)
#         add_node_attempt = browser.find_element_by_xpath("//*[@type='submit']")
#         add_node_attempt.click()
#         time.sleep(3)
#         assert "The node name already exists." in browser.page_source
#         time.sleep(3)
#         self.browser.close()
#
#     def test_element_new_node_note_empty(self):
#         self.browser = webdriver.Chrome("C:\\Users\\zhou502\\Documents\\chromedriver.exe")
#
#         browser = self.browser
#         browser.get("http://localhost:8070/")
#         time.sleep(3)
#
#         browser.find_elements_by_xpath("//span")[1].click()
#         # self.assertIn("Login", browser.title)
#         time.sleep(3)
#         # login as an admin
#         username = browser.find_element_by_id("username")
#         password = browser.find_element_by_id("password")
#         username.send_keys("hanrong")
#         password.send_keys("640519")
#         time.sleep(3)
#
#         login_attempt = browser.find_element_by_xpath("//*[@type='submit']")
#         login_attempt.submit()
#         time.sleep(3)
#
#         browser.find_elements_by_link_text("Elements")[0].click()
#         time.sleep(3)
#
#         new_domain = browser.find_element_by_xpath("//*[@value='node_info']")
#         new_domain.click()
#         time.sleep(3)
#
#         node_name = browser.find_element_by_id("node")
#         node_name.send_keys("KK")
#         time.sleep(3)
#
#         note_name = browser.find_element_by_id("note")
#         note_name.send_keys("")
#         time.sleep(3)
#
#         add_node_attempt = browser.find_element_by_xpath("//*[@type='submit']")
#         add_node_attempt.click()
#         time.sleep(3)
#         assert "Node KK added successfully." in browser.page_source
#         self.browser.close()
#
#     def test_element_new_node_note_not_empty(self):
#         self.browser = webdriver.Chrome("C:\\Users\\zhou502\\Documents\\chromedriver.exe")
#
#         browser = self.browser
#         browser.get("http://localhost:8070/")
#         time.sleep(3)
#
#         browser.find_elements_by_xpath("//span")[1].click()
#         # self.assertIn("Login", browser.title)
#         time.sleep(3)
#         # login as an admin
#         username = browser.find_element_by_id("username")
#         password = browser.find_element_by_id("password")
#         username.send_keys("hanrong")
#         password.send_keys("640519")
#         time.sleep(3)
#
#         login_attempt = browser.find_element_by_xpath("//*[@type='submit']")
#         login_attempt.submit()
#         time.sleep(3)
#
#         browser.find_elements_by_link_text("Elements")[0].click()
#         time.sleep(3)
#
#         new_domain = browser.find_element_by_xpath("//*[@value='node_info']")
#         new_domain.click()
#         time.sleep(3)
#
#         node_name = browser.find_element_by_id("node")
#         node_name.send_keys("KKK")
#         time.sleep(3)
#
#         note_name = browser.find_element_by_id("note")
#         note_name.send_keys("xxx")
#         time.sleep(3)
#
#         add_node_attempt = browser.find_element_by_xpath("//*[@type='submit']")
#         add_node_attempt.click()
#         time.sleep(3)
#         assert "Node KKK added successfully." in browser.page_source
#         self.browser.close()
#
#     def test_element_delete_node(self):
#         self.browser = webdriver.Chrome("C:\\Users\\zhou502\\Documents\\chromedriver.exe")
#
#         browser = self.browser
#         browser.get("http://localhost:8070/")
#         time.sleep(3)
#
#         browser.find_elements_by_xpath("//span")[1].click()
#         # self.assertIn("Login", browser.title)
#         time.sleep(3)
#         # login as an admin
#         username = browser.find_element_by_id("username")
#         password = browser.find_element_by_id("password")
#         username.send_keys("hanrong")
#         password.send_keys("640519")
#         time.sleep(3)
#
#         login_attempt = browser.find_element_by_xpath("//*[@type='submit']")
#         login_attempt.submit()
#         time.sleep(3)
#
#         browser.find_elements_by_link_text("Elements")[0].click()
#         time.sleep(3)
#
#         new_domain = browser.find_element_by_xpath("//*[@value='node_info']")
#         new_domain.click()
#         time.sleep(3)
#
#         delete_node_name = browser.find_element_by_xpath("//*[@id= 'delete_node']")
#         for option in delete_node_name.find_elements_by_tag_name('option'):
#             if option.text == 'KKK':
#                 option.click()
#                 time.sleep(3)
#                 browser.find_element_by_xpath("//*[@type='submit']").click()
#                 break
#         time.sleep(3)
#         assert "Deleted KKK successfully" in browser.page_source
#         self.browser.close()
#
#     def test_element_add_new_element_hostname_empty(self):
#         self.browser = webdriver.Chrome("C:\\Users\\zhou502\\Documents\\chromedriver.exe")
#
#         browser = self.browser
#         browser.get("http://localhost:8070/")
#         time.sleep(3)
#
#         browser.find_elements_by_xpath("//span")[1].click()
#         # self.assertIn("Login", browser.title)
#         time.sleep(3)
#         # login as an admin
#         username = browser.find_element_by_id("username")
#         password = browser.find_element_by_id("password")
#         username.send_keys("hanrong")
#         password.send_keys("640519")
#         time.sleep(3)
#
#         login_attempt = browser.find_element_by_xpath("//*[@type='submit']")
#         login_attempt.submit()
#         time.sleep(3)
#
#         browser.find_elements_by_link_text("Elements")[0].click()
#         time.sleep(3)
#
#         new_element = browser.find_element_by_xpath("//*[@value='new-element']")
#         new_element.click()
#         time.sleep(3)
#         # self.assertIn("New Element", browser.title)
#
#         host_name = browser.find_element_by_id("hostname")
#         host_name.send_keys("")
#         add_element_attempt = browser.find_element_by_xpath("//*[@type='submit']")
#         add_element_attempt.click()
#         assert "Adding failed, must type a hostname." in browser.page_source
#         time.sleep(3)
#
#         self.browser.close()
#
#     def test_element_add_new_element_hostname_not_empty(self):
#         self.browser = webdriver.Chrome("C:\\Users\\zhou502\\Documents\\chromedriver.exe")
#
#         browser = self.browser
#         browser.get("http://localhost:8070/")
#         time.sleep(3)
#
#         browser.find_elements_by_xpath("//span")[1].click()
#         # self.assertIn("Login", browser.title)
#         time.sleep(3)
#         # login as an admin
#         username = browser.find_element_by_id("username")
#         password = browser.find_element_by_id("password")
#         username.send_keys("hanrong")
#         password.send_keys("640519")
#         time.sleep(3)
#
#         login_attempt = browser.find_element_by_xpath("//*[@type='submit']")
#         login_attempt.submit()
#         time.sleep(3)
#
#         browser.find_elements_by_link_text("Elements")[0].click()
#         time.sleep(3)
#
#         new_element = browser.find_element_by_xpath("//*[@value='new-element']")
#         new_element.click()
#         time.sleep(3)
#         # self.assertIn("New Element", browser.title)
#
#         host_name = browser.find_element_by_id("hostname")
#         host_name.send_keys("a")
#         add_element_attempt = browser.find_element_by_xpath("//*[@type='submit']")
#         add_element_attempt.click()
#         assert "a added successfully." in browser.page_source
#         time.sleep(3)
#
#         self.browser.close()
#
#     def test_element_info(self):
#         self.browser = webdriver.Chrome("C:\\Users\\zhou502\\Documents\\chromedriver.exe")
#
#         browser = self.browser
#         browser.get("http://localhost:8070/")
#         time.sleep(3)
#
#         browser.find_elements_by_xpath("//span")[1].click()
#         # self.assertIn("Login", browser.title)
#         time.sleep(3)
#         # login as an admin
#         username = browser.find_element_by_id("username")
#         password = browser.find_element_by_id("password")
#         username.send_keys("hanrong")
#         password.send_keys("640519")
#         time.sleep(3)
#
#         login_attempt = browser.find_element_by_xpath("//*[@type='submit']")
#         login_attempt.submit()
#         time.sleep(3)
#
#         browser.find_elements_by_link_text("Elements")[0].click()
#         time.sleep(3)
#
#         browser.find_elements_by_link_text("a")[0].click()
#         time.sleep(3)
#
#         # I don't know what assertion that needed to put here
#         self.browser.close()
#
#     def test_element_info_refresh(self):
#         self.browser = webdriver.Chrome("C:\\Users\\zhou502\\Documents\\chromedriver.exe")
#
#         browser = self.browser
#         browser.get("http://localhost:8070/")
#         time.sleep(3)
#
#         browser.find_elements_by_xpath("//span")[1].click()
#         # self.assertIn("Login", browser.title)
#         time.sleep(3)
#         # login as an admin
#         username = browser.find_element_by_id("username")
#         password = browser.find_element_by_id("password")
#         username.send_keys("hanrong")
#         password.send_keys("640519")
#         time.sleep(3)
#
#         login_attempt = browser.find_element_by_xpath("//*[@type='submit']")
#         login_attempt.submit()
#         time.sleep(3)
#
#         browser.find_elements_by_link_text("Elements")[0].click()
#         time.sleep(3)
#
#         browser.find_elements_by_link_text("a")[0].click()
#         time.sleep(3)
#
#         element_refresh = browser.find_element_by_xpath("//*[@value='Refresh']")
#         element_refresh.click()
#         time.sleep(3)
#
#         # I don't know what assertion that needed to put here
#         self.browser.close()
#
#     def test_element_info_change(self):
#         self.browser = webdriver.Chrome("C:\\Users\\zhou502\\Documents\\chromedriver.exe")
#
#         browser = self.browser
#         browser.get("http://localhost:8070/")
#         time.sleep(3)
#
#         browser.find_elements_by_xpath("//span")[1].click()
#         # self.assertIn("Login", browser.title)
#         time.sleep(3)
#         # login as an admin
#         username = browser.find_element_by_id("username")
#         password = browser.find_element_by_id("password")
#         username.send_keys("hanrong")
#         password.send_keys("640519")
#         time.sleep(3)
#
#         login_attempt = browser.find_element_by_xpath("//*[@type='submit']")
#         login_attempt.submit()
#         time.sleep(3)
#
#         browser.find_elements_by_link_text("Elements")[0].click()
#         time.sleep(3)
#
#         browser.find_elements_by_link_text("a")[0].click()
#         time.sleep(3)
#
#         element_refresh = browser.find_element_by_xpath("//*[@value='Change']")
#         element_refresh.click()
#         time.sleep(3)
#
#         # I don't know what assertion that needed to put here
#         self.browser.close()

class Department(unittest.TestCase):

    # def test_go_to_department(self):
    #         # go to the homepage
    #         self.browser = webdriver.Chrome("C:\\Users\\zhou502\\Documents\\chromedriver.exe")
    #
    #         browser = self.browser
    #         browser.get("http://localhost:8070/")
    #         time.sleep(3)
    #
    #         browser.find_elements_by_xpath("//span")[1].click()
    #         # self.assertIn("Login", browser.title)
    #         time.sleep(3)
    #         # login as an admin
    #         username = browser.find_element_by_id("username")
    #         password = browser.find_element_by_id("password")
    #         username.send_keys("hanrong")
    #         password.send_keys("640519")
    #         time.sleep(3)
    #
    #         login_attempt = browser.find_element_by_xpath("//*[@type='submit']")
    #         login_attempt.submit()
    #         time.sleep(3)
    #
    #         browser.find_elements_by_link_text("Departments")[0].click()
    #         self.assertIn("Departments", browser.title)
    #         time.sleep(3)
    #
    #         self.browser.close()

    # def test_department_delete_department(self):
    #     # go to the homepage
    #     self.browser = webdriver.Chrome("C:\\Users\\zhou502\\Documents\\chromedriver.exe")
    #
    #     browser = self.browser
    #     browser.get("http://localhost:8070/")
    #     time.sleep(3)
    #
    #     browser.find_elements_by_xpath("//span")[1].click()
    #     # self.assertIn("Login", browser.title)
    #     time.sleep(3)
    #     # login as an admin
    #     username = browser.find_element_by_id("username")
    #     password = browser.find_element_by_id("password")
    #     username.send_keys("hanrong")
    #     password.send_keys("640519")
    #     time.sleep(3)
    #
    #     login_attempt = browser.find_element_by_xpath("//*[@type='submit']")
    #     login_attempt.submit()
    #     time.sleep(3)
    #
    #     browser.find_elements_by_link_text("Departments")[0].click()
    #     time.sleep(3)
    #
    #     delete_department = browser.find_element_by_xpath("//*[@id= 'delete_department']")
    #     for option in delete_department.find_elements_by_tag_name('option'):
    #         if option.text == 'Innovation Test Data':
    #             option.click()
    #             break
    #     time.sleep(3)
    #
    #     delete_department_attempt = browser.find_element_by_xpath("//*[@value='Delete']")
    #     delete_department_attempt.click()
    #     time.sleep(3)
    #     assert "Successfully removed Innovation Test Data from department list." in browser.page_source
    #     self.browser.close()

    # def test_department_add_new_department_empty(self):
    #     # go to the homepage
    #     self.browser = webdriver.Chrome("C:\\Users\\zhou502\\Documents\\chromedriver.exe")
    #
    #     browser = self.browser
    #     browser.get("http://localhost:8070/")
    #     time.sleep(3)
    #
    #     browser.find_elements_by_xpath("//span")[1].click()
    #     # self.assertIn("Login", browser.title)
    #     time.sleep(3)
    #     # login as an admin
    #     username = browser.find_element_by_id("username")
    #     password = browser.find_element_by_id("password")
    #     username.send_keys("hanrong")
    #     password.send_keys("640519")
    #     time.sleep(3)
    #
    #     login_attempt = browser.find_element_by_xpath("//*[@type='submit']")
    #     login_attempt.submit()
    #     time.sleep(3)
    #
    #     browser.find_elements_by_link_text("Departments")[0].click()
    #     time.sleep(3)
    #
    #     # add_new_department = browser.find_element_by_xpath("//*[@id= 'new_department']")
    #     add_new_department = browser.find_element_by_id("new_department")
    #     add_new_department.send_keys("")
    #     time.sleep(3)
    #
    #     add_new_department_attempt = browser.find_element_by_xpath("//*[@value='Add']")
    #     add_new_department_attempt.click()
    #     time.sleep(3)
    #     assert "Department field can't be empty." in browser.page_source
    #     self.browser.close()

    # def test_department_add_new_department_existing(self):
    #     # go to the homepage
    #     self.browser = webdriver.Chrome("C:\\Users\\zhou502\\Documents\\chromedriver.exe")
    #
    #     browser = self.browser
    #     browser.get("http://localhost:8070/")
    #     time.sleep(3)
    #
    #     browser.find_elements_by_xpath("//span")[1].click()
    #     # self.assertIn("Login", browser.title)
    #     time.sleep(3)
    #     # login as an admin
    #     username = browser.find_element_by_id("username")
    #     password = browser.find_element_by_id("password")
    #     username.send_keys("hanrong")
    #     password.send_keys("640519")
    #     time.sleep(3)
    #
    #     login_attempt = browser.find_element_by_xpath("//*[@type='submit']")
    #     login_attempt.submit()
    #     time.sleep(3)
    #
    #     browser.find_elements_by_link_text("Departments")[0].click()
    #     time.sleep(3)
    #
    #     # add_new_department = browser.find_element_by_xpath("//*[@id= 'new_department']")
    #     add_new_department = browser.find_element_by_id("new_department")
    #     add_new_department.send_keys("Innovation Test Radio")
    #     time.sleep(3)
    #
    #     add_new_department_attempt = browser.find_element_by_xpath("//*[@value='Add']")
    #     add_new_department_attempt.click()
    #     time.sleep(3)
    #     assert "Department \"Innovation Test Radio\" already exists" in browser.page_source
    #     self.browser.close()

    # def test_department_add_new_department(self):
    #     # go to the homepage
    #     self.browser = webdriver.Chrome("C:\\Users\\zhou502\\Documents\\chromedriver.exe")
    #
    #     browser = self.browser
    #     browser.get("http://localhost:8070/")
    #     time.sleep(3)
    #
    #     browser.find_elements_by_xpath("//span")[1].click()
    #     # self.assertIn("Login", browser.title)
    #     time.sleep(3)
    #     # login as an admin
    #     username = browser.find_element_by_id("username")
    #     password = browser.find_element_by_id("password")
    #     username.send_keys("hanrong")
    #     password.send_keys("640519")
    #     time.sleep(3)
    #
    #     login_attempt = browser.find_element_by_xpath("//*[@type='submit']")
    #     login_attempt.submit()
    #     time.sleep(3)
    #
    #     browser.find_elements_by_link_text("Departments")[0].click()
    #     time.sleep(3)
    #
    #     add_new_department = browser.find_element_by_id("new_department")
    #     add_new_department.send_keys("Innovation Test Case 1")
    #     time.sleep(3)
    #
    #     add_new_department_attempt = browser.find_element_by_xpath("//*[@value='Add']")
    #     add_new_department_attempt.click()
    #     time.sleep(3)
    #     assert "Department Innovation Test Case 1 added successfully." in browser.page_source
    #     self.browser.close()

    # def test_department_change_department_empty(self):
    #     # go to the homepage
    #     self.browser = webdriver.Chrome("C:\\Users\\zhou502\\Documents\\chromedriver.exe")
    #
    #     browser = self.browser
    #     browser.get("http://localhost:8070/")
    #     time.sleep(3)
    #
    #     browser.find_elements_by_xpath("//span")[1].click()
    #     # self.assertIn("Login", browser.title)
    #     time.sleep(3)
    #     # login as an admin
    #     username = browser.find_element_by_id("username")
    #     password = browser.find_element_by_id("password")
    #     username.send_keys("hanrong")
    #     password.send_keys("640519")
    #     time.sleep(3)
    #
    #     login_attempt = browser.find_element_by_xpath("//*[@type='submit']")
    #     login_attempt.submit()
    #     time.sleep(3)
    #
    #     browser.find_elements_by_link_text("Departments")[0].click()
    #     time.sleep(3)
    #
    #     change_department_old = browser.find_element_by_xpath("//*[@id= 'change_department_list']")
    #     for option in change_department_old.find_elements_by_tag_name('option'):
    #         if option.text == 'Innovation Test Case 1':
    #             option.click()
    #             break
    #     time.sleep(3)
    #
    #     change_department_new = browser.find_element_by_id("change_department_input")
    #     change_department_new.send_keys("")
    #     time.sleep(3)
    #
    #     change_department_attempt = browser.find_element_by_xpath("//*[@value='Change']")
    #     change_department_attempt.click()
    #     time.sleep(3)
    #     assert "Department field can't be empty." in browser.page_source
    #     self.browser.close()

    # def test_department_change_department_existing(self):
    #     # go to the homepage
    #     self.browser = webdriver.Chrome("C:\\Users\\zhou502\\Documents\\chromedriver.exe")
    #
    #     browser = self.browser
    #     browser.get("http://localhost:8070/")
    #     time.sleep(3)
    #
    #     browser.find_elements_by_xpath("//span")[1].click()
    #     # self.assertIn("Login", browser.title)
    #     time.sleep(3)
    #     # login as an admin
    #     username = browser.find_element_by_id("username")
    #     password = browser.find_element_by_id("password")
    #     username.send_keys("hanrong")
    #     password.send_keys("640519")
    #     time.sleep(3)
    #
    #     login_attempt = browser.find_element_by_xpath("//*[@type='submit']")
    #     login_attempt.submit()
    #     time.sleep(3)
    #
    #     browser.find_elements_by_link_text("Departments")[0].click()
    #     time.sleep(3)
    #
    #     change_department_old = browser.find_element_by_xpath("//*[@id= 'change_department_list']")
    #     for option in change_department_old.find_elements_by_tag_name('option'):
    #         if option.text == 'Innovation Test Case 1':
    #             option.click()
    #             break
    #     time.sleep(3)
    #
    #     change_department_new = browser.find_element_by_id("change_department_input")
    #     change_department_new.send_keys("Innovation Test Case 1")
    #     time.sleep(3)
    #
    #     change_department_attempt = browser.find_element_by_xpath("//*[@value='Change']")
    #     change_department_attempt.click()
    #     time.sleep(3)
    #     assert "Department \"Innovation Test Case 1\" already exists" in browser.page_source
    #     self.browser.close()

    def test_department_change_department(self):
        self.browser = webdriver.Chrome("C:\\Users\\zhou502\\Documents\\chromedriver.exe")

        browser = self.browser
        browser.get("http://localhost:8070/")
        time.sleep(3)

        browser.find_elements_by_xpath("//span")[1].click()
        # self.assertIn("Login", browser.title)
        time.sleep(3)
        # login as an admin
        username = browser.find_element_by_id("username")
        password = browser.find_element_by_id("password")
        username.send_keys("hanrong")
        password.send_keys("640519")
        time.sleep(3)

        login_attempt = browser.find_element_by_xpath("//*[@type='submit']")
        login_attempt.submit()
        time.sleep(3)

        browser.find_elements_by_link_text("Departments")[0].click()
        time.sleep(3)

        change_department_old = browser.find_element_by_xpath("//*[@id= 'change_department_list']")
        for option in change_department_old.find_elements_by_tag_name('option'):
            if option.text == 'Innovation Test Case 1':
                option.click()
                break
        time.sleep(3)

        change_department_new = browser.find_element_by_id("change_department_input")
        change_department_new.send_keys("Innovation Test Case 3")
        time.sleep(3)

        change_department_attempt = browser.find_element_by_xpath("//*[@value='Change']")
        change_department_attempt.click()
        time.sleep(3)
        assert "Changed Department \"Innovation Test Case 1\" successfully in \"Innovation Test Case 3\"." in browser.page_source
        self.browser.close()


if __name__ == "__main__":
    unittest.main()