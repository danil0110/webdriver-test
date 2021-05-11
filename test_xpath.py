from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pageObjects.twitchPO import TwitchPO

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.implicitly_wait(30)

twitch_po = TwitchPO(browser)

twitch_po.open()
twitch_po.open_login_form()
twitch_po.fill_login_data('forbiz375', 's1mple98Pass')
twitch_po.login()

alert_text = twitch_po.get_alert_text()
expected_alert = 'Такого имени пользователя не существует.'

assert alert_text == expected_alert
