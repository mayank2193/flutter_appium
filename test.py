import os

from appium.webdriver import Remote
from appium_flutter_finder.flutter_finder import FlutterElement, FlutterFinder

# Example

driver = Remote('http://:@beta-hub.lambdatest.com/wd/hub/', dict(
    platformName='android',
    automationName='flutter',
    platformVersion='12',
    deviceName='Pixel 6 Pro',
    app='lt://',
    isRealMobile=True
))

finder = FlutterFinder()

text_finder = finder.by_text('You have pushed the button this many times:')
text_element = FlutterElement(driver, text_finder)
print(text_element.text)

key_finder = finder.by_value_key("next_route_key")
goto_next_route_element = FlutterElement(driver, key_finder)
print(goto_next_route_element.text)
goto_next_route_element.click()

back_finder = finder.page_back()
back_element = FlutterElement(driver, back_finder)
back_element.click()

tooltip_finder = finder.by_tooltip("Increment")
driver.execute_script('flutter:waitFor', tooltip_finder, 100)

floating_button_element = FlutterElement(driver, tooltip_finder)
floating_button_element.click()

counter_finder = finder.by_value_key("counter")
counter_element = FlutterElement(driver, counter_finder)
print(counter_element.text)
