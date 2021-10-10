from selenium import webdriver
import time

if __name__ == '__main__':

    # instantiate the webdriver with the executable location of MS Edge web driver
    browser = webdriver.Edge(r'F:\Drivers\msedgedriver.exe')

    # open a new Edge browser and go to duckduckgo.com
    browser.get('http://duckduckgo.com/')

    # delay 5 seconds
    time.sleep(5)

    # quit browser
    browser.quit()

    # status message
    print('Script executed successfully !')
