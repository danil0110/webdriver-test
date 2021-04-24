from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.implicitly_wait(30)
browser.get('https://www.twitch.tv/')

browser.find_element_by_css_selector('[data-a-target="login-button"]').click()
body = browser.find_element_by_tag_name('body')
modalClass = 'ReactModal__Body--open'

assert modalClass in body.get_attribute('class')

usernameInput = browser.find_element_by_css_selector('input#login-username')
passwordInput = browser.find_element_by_css_selector('input#password-input')

usernameInput.send_keys('forbiz375')
passwordInput.send_keys('s1mple98Pass')
passwordInput.send_keys(Keys.RETURN)

expectedError = 'Такого имени пользователя не существует.'
errorMessage = browser.find_element_by_css_selector('.server-message-alert strong').text

assert errorMessage == expectedError