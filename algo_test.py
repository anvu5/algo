import os
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time


#FireFox Profile
profile=webdriver.FirefoxProfile()
profile.set_preference('browser.download.folderList',2)
profile.set_preference('browser.download.manager.showWhenStarting',False)
profile.set_preference('browser.download.dir',os.getcwd())
profile.set_preference('browser.helperApps.neverAsk.saveToDisk','text/csv')

#Running Headless Browser
options=Options()
options.headless=True
browser=webdriver.Firefox(options=options, executable_path=r'C:\Users\anvu0\Documents\tradelog\geckodriver.exe')

#Running Non Headless Browser
#browser=webdriver.Firefox(firefox_profile=profile,executable_path=r'C:\Users\anvu0\Documents\tradelog\geckodriver.exe')

#Launch tradingview.com
browser.get('https://tradingview.com')

time.sleep(2)

#Select sign in
signinForm=browser.find_element_by_link_text('Sign in').click()

time.sleep(2)

#Select sign in by email
emailSelect=browser.find_element_by_class_name('tv-signin-dialog__social.tv-signin-dialog__toggle-email.js-show-email').click()

time.sleep(2)

#email & pass

inputBoxes=browser.find_elements_by_css_selector('div.tv-control-material-input__wrap')
print('number of input boxes are '+ str(len(inputBoxes)))


#launch screeber
URL='https://tradingview.com/screener'
script="window.open('" + URL + "','new_window')"
browser.execute_script(script)
time.sleep(2)

#switch window
browser.switch_to.window(browser.window_handles[1])
time.sleep(1)

#find csv
csvBtn=browser.find_elements_by_css_selector('div.tv-screener-toolbar__button.tv-screener-toolbar__button--space_right.tv-screener-toolbar__button--export.apply-common-tooltip.common-tooltip-fixed')
print('csv button find is '+ str(len(csvBtn)))

time.sleep(1)

#Fillout login
#username=driver.find_element_by_xpath()
#username.send_keys()
#time.sleep(2)
#passoword=driver.find_elemeent_by_xpath()
#password.send_keys()

#assert 'Google' in browser.tittle
browser.quit()
#browser.close()
