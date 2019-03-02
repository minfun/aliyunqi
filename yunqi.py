from selenium import webdriver
import time
import os
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# userprofile = ""
chromedriver = "/Users/leifanwang/workspace/appannie/selenium/chromedriver"
options = webdriver.ChromeOptions()
# # options.add_argument("user-data-dir={}".format(userprofile))
# # add here any tag you want.
# # options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors", "safebrowsing-disable-download-protection", "safebrowsing-disable-auto-update", "disable-client-side-phishing-detection"])
# options.add_argument('--proxy-server=127.0.0.1:8080')
# os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(executable_path=chromedriver, chrome_options=options)

# firefox_option = webdriver.FirefoxOptions()
# firefox_option.add_argument('--proxy-server=127.0.0.1:8081')
# driver = webdriver.Firefox(executable_path="/Users/leifanwang/workspace/appannie/selenium/geckodriver", firefox_options=firefox_option)

wait = WebDriverWait(driver, 60)
driver.maximize_window()
username = '491548526@qq.com'
# username = 'sciappintercorp'
password = ''
driver.get('https://yq.aliyun.com/')

js1 = '''Object.defineProperties(navigator,{ webdriver:{ get: () => false } }) '''
js2 = '''window.navigator.chrome = { runtime: {},  }; '''
js3 = '''Object.defineProperty(navigator, 'languages', { get: () => ['en-US', 'en'] }); '''
js4 = '''Object.defineProperty(navigator, 'plugins', { get: () => [1, 2, 3, 4, 5,6], }); '''

driver.execute_script(js1)
driver.execute_script(js2)
driver.execute_script(js3)
driver.execute_script(js4)
# driver.find_element_by_id('script-dropdown-btn').click()
driver.find_element_by_xpath("//a[@class='login']").click()
# driver.get('https://account.aliyun.com/login/login.htm?spm=a2c4e.11157919.headeruserinfo.2.146c27aewg7UVY&from_type=yqclub&oauth_callback=https%3A%2F%2Fyq.aliyun.com%2F%3Fdo%3Dlogin')
# wait.until(EC.element_to_be_clickable((By.ID, 'fm-login-id')))

wait.until(EC.element_to_be_clickable((By.ID, 'alibaba-login-box')))
iframe = driver.find_element_by_xpath("//iframe[@id='alibaba-login-box']")
driver.switch_to.frame(iframe)

driver.execute_script(js1)
driver.execute_script(js2)
driver.execute_script(js3)
driver.execute_script(js4)

print '1'
driver.find_element_by_xpath("//input[@id='fm-login-id']").send_keys(username)

print '2'
driver.find_element_by_xpath("//input[@id='fm-login-password']").send_keys(password)
print '3'

element = driver.find_element_by_xpath("//span[@id='nc_1_n1z']")
action_chains = ActionChains(driver)
action_chains.click_and_hold(element).perform()
action_chains.move_by_offset(70, 0.3)
action_chains.pause(0.1)
action_chains.move_by_offset(80, 0.5)
action_chains.pause(0.3)
action_chains.move_by_offset(148, 0.2)
action_chains.pause(1)
action_chains.release().perform()

# action_chains.move_by_offset(300, 0).perform()
driver.find_element_by_xpath("//button[@type='submit']").click()
time.sleep(100)
