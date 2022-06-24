import os
import time

from appium.webdriver import Remote
from appium_flutter_finder.flutter_finder import FlutterElement, FlutterFinder

# Example

driver = Remote('http://:@beta-hub.lambdatest.com/wd/hub/', dict(
    platformName='android',
    automationName='flutter',
    platformVersion='12',
    deviceName='Pixel 6 Pro',
    app='lt://APP100202361655877669430228',
    isRealMobile=True,
    w3c=True,
    devicelog=True,
    build='Flutter-Demo-Build',
    name='Flutter-test'
))

finder = FlutterFinder()

#text_finder = finder.by_text('You have pushed the button this many times:')
# text_element = FlutterElement(driver, text_finder)
# print(text_element.text)

time.sleep(5)

driver.quit()
