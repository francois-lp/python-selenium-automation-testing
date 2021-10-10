import glob
import globals_vars
from pathlib import Path
import os
import unittest

# load globals vars
globals_vars.initialize()

# contruct lists (browsers and tests)
browsers_list_files = glob.glob('model\\drivers\\[!abstra]*_webdriver.py')
browsers_list = [(Path(file.replace('_webdriver', '')).resolve(
).stem).capitalize() for file in browsers_list_files]
browsers_list.sort()

tests_list_files = glob.glob('model\\tests\\[!abstract]*_test.py')
tests_list = [os.path.splitext(file.replace('\\', '.'))[0]
              for file in tests_list_files]

# browser choice
print('##### SELENIUM TESTS #####')
print('\n# STEP 1 - Browser choice #')
for i in range(len(browsers_list)):
    print(str(i+1) + " - " + browsers_list[i])
user_browser_choice = input('Choose the browser to use : ')

try:
    globals_vars.driver_name = browsers_list[int(user_browser_choice)-1]
except (IndexError, ValueError):
    print('Invalid choice "' + str(user_browser_choice) +
          '", the default browser is : ' + globals_vars.driver_name)

# test choice
print('\n# STEP 2 - Test choice #')
for i in range(len(tests_list)):
    print(str(i+1) + " - " + tests_list[i])
chosen_test = input('Choose the test to run (empty = all) : ')

# tests list to run
try:
    tests_to_execute = []
    tests_to_execute.append(tests_list[int(chosen_test)-1])
except (IndexError, ValueError):
    if(str(chosen_test) in ['', '*']):
        tests_to_execute = tests_list
    else:
        print('Invalid choice "' + str(chosen_test) + '"')

# tests list execution
print('\n# STEP 3 - Starting tests')
suite = unittest.TestSuite()
for t in tests_to_execute:
    try:
        # If the module defines a suite() function, call it to get the suite.
        mod = __import__(t, globals(), locals(), ['suite'])
        suitefn = getattr(mod, 'suite')
        suite.addTest(suitefn())
    except (ImportError, AttributeError):
        # else, just load all the test cases from the module.
        suite.addTest(unittest.defaultTestLoader.loadTestsFromName(t))

res = unittest.TextTestRunner().run(suite)
