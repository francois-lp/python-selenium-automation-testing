from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from datetime import datetime
import time

# config
break_time = 5

def do_break_time():
    time.sleep(break_time)

# options
options = Options()
options.add_argument("--headless")
options.add_argument("--start-maximized")
options.add_experimental_option('prefs', {
    'credentials_enable_service': False,
    'profile': {
        'password_manager_enabled': False
    }
})
chrome_options = webdriver.ChromeOptions()
#chrome_options.set_capability('--headless', False)
#chrome_options.set_capability('--start-maximized', True)
#chrome_options.headless = True
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--remote-debugging-port=9222")
# chrome_options.add_argument('--no-sandbox')

# open Chrome
driver = webdriver.Chrome(
    executable_path='F:\Drivers\chromedriver.exe', chrome_options=chrome_options)
driver.set_page_load_timeout(10)
driver.maximize_window()
driver.get('https://duckduckgo.com/')
do_break_time()

# write in input search (voluntary typo)
search_box = driver.find_element_by_xpath(
    '//*[@id="search_form_input_homepage"]')
search_box.clear()
search_box.send_keys('Python tutoraill')
do_break_time()

# click on search button
search_button = driver.find_element_by_xpath(
    '//*[@id="search_button_homepage"]')
search_button.click()
do_break_time()

# click on spelling suggestion
search_button = driver.find_element_by_xpath(
    '//*[@class="js-spelling-suggestion-link"]')
search_button.click()
do_break_time()

# scroll down
# scroll vertically down by 300 pixels the first time
driver.execute_script('window.scrollBy(0,300)')
do_break_time()
# scroll vertically down by 300 pixels the second time
driver.execute_script('window.scrollBy(0,600)')
do_break_time()
driver.execute_script(
    'window.scrollTo(0,document.body.scrollHeight)')  # scroll to bottom
do_break_time()

# taking screenshot
current_datetime = (datetime.now()).strftime('%Y%m%d_%H%M%S')
driver.get_screenshot_as_file('screenshot_' + current_datetime + '.png')

# open second tab
driver.execute_script('window.open()')
driver.switch_to.window(driver.window_handles[1])
do_break_time()

# change page
driver.get('https://www.php.net/')
do_break_time()

# refresh page
driver.refresh()
do_break_time()

# return to first tab
driver.switch_to.window(driver.window_handles[0])

# change page
driver.get('https://python.org')
do_break_time()
driver.get('https://pypi.org/')
do_break_time()

# navigate
driver.back()
do_break_time()
driver.forward()
do_break_time()

# close browser
driver.quit()
print('Script executed successfully !')
# time.sleep(5)
