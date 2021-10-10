## Selenium automation testing
*Selenium is a free (open-source) automated testing framework used to validate web applications across different browsers and platforms.*  

## Installation

__Requirements__
 - Python (>= 3.9.4)
 - pip (>= 21.2.4)

__Project__
```
    $ git clone https://github.com/francois-lp/python-selenium-automation-testing
```

__Dependencies__
```
    pip install selenium
```

*Update pip if it could not find a version that satisfies the requirement selenimum*
```
    pip install --upgrade pip
```

*Browsers drivers*
- ChromeDriver ([download](https://pypi.org/project/chromedriver-py/) | [usage](https://sites.google.com/chromium.org/driver/))
```
    pip install chromedriver-py==93.0.4577.63
```

- FirefoxDriver ([download](https://github.com/mozilla/geckodriver/releases) | [usage](https://pythonbasics.org/selenium-firefox/))
<br />

- EdgeDriver ([download](https://developer.microsoft.com/fr-fr/microsoft-edge/tools/webdriver/) | [usage](https://docs.microsoft.com/fr-fr/microsoft-edge/webdriver-chromium/?tabs=c-sharp))
```
    pip install msedge-selenium-tools selenium==3.141
```

## Getting started
```
    python main.py
```

## Notes
__Conventions__
1. A test case class must inherit from unittest.TestCase
1. "setUpClass" method is executed once per test class before running any test method or setUp or tearDown method
1. "setUp" method is executed before every test method present in the test class (it is part of initialization) 
1. Any test method must start with "test" (the first line inside this method create a local reference to the driver object created in setUp method)
1. The "tearDown" method will get called after every test method (this is a place to do all cleanup actions)
1. Calling close driver method will close a tab, calling the quit method will exit the entire browser

__Best practices__
1. Before to write text in an input field first clear it


## Links
__Documentation__
* [Selenium with Python](https://selenium-python.readthedocs.io/index.html)
* [Selenium with PHP](https://www.lambdatest.com/blog/selenium-php-tutorial/)
* [Selenium drivers](https://selenium-python.readthedocs.io/installation.html#drivers)
* [Unittest Selenium](https://chercher.tech/python/python-unittest-selenium)
* [Commands cheat sheet](http://allselenium.info/python-selenium-commands-cheat-sheet-frequently-used/)

__Tutorials__
* [Selenium Scroll Down Webpage](https://pythonbasics.org/selenium-scroll-down/)
* [Selenium switch to window](https://pythonbasics.org/selenium-switch-to-window/)
* [Take Webpage Screenshot with Python Selenium](https://pythonbasics.org/selenium-screenshot/)
