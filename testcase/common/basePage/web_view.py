import time
import os
from appium import webdriver
from appium.webdriver.connectiontype import ConnectionType
from utils.config import REPORT_PATH
from utils.log import logger

TYPES = {'remote': webdriver.Remote}


class UnSupportTypeError(Exception):
    pass


class WebView(object):
    def __init__(self,browser_type=None):
        # self.desired_caps = desired_caps
        self._type = 'remote'
        if self._type in TYPES:
            self.browser = TYPES[self._type]
        else:
            raise UnSupportTypeError('Only support {}！'.join(TYPES.keys()))
        self.driver = None

    def get(self, appium_url, desired_caps, implicitly_wait=30, noReset=None):
        logger.info("Get desired_caps:{}".format(desired_caps))
        if noReset == None or noReset == True:
            desired_caps.update({'noReset':True})
        else:
            desired_caps.update({'noReset': False})
        logger.info("Final desired_caps:{}".format(desired_caps))
        self.driver = webdriver.Remote(appium_url.get('url'), desired_caps)
        self.driver.implicitly_wait(implicitly_wait)
        return self

    def save_screen_shot(self, page_name=None, file_name='screen_shot', ti=False):
        day = time.strftime('%Y%m%d', time.localtime(time.time()))
        screenshot_path = REPORT_PATH + '\%s_%s' % (page_name, day)
        if not os.path.exists(screenshot_path):
            os.makedirs(screenshot_path)
        if ti:
            tm = time.strftime('%H%M%S', time.localtime(time.time()))
            screenshot = self.driver.save_screenshot(screenshot_path + '\\%s_%s.png' % (file_name, tm))
        else:
            screenshot = self.driver.save_screenshot(screenshot_path + '\\%s.png' % (file_name))
        return screenshot

    def getSize(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return (x, y)

    def flickUp(self, x, y1, y2):
        x = int(x * 0.8)
        # y1 = int(y1 * 0.9)
        # y2 = int(y2 * 0.9)
        self.driver.flick(x, y1, x, y2)

    def flickDown(self, x, y1, y2):
        self.driver.flick(x, y2, x, y1)

    def swipeUp(self, x, y1, y2, t=200):
        self.driver.swipe(x, y1, x, y2, t)

    def swipeDown(self, x, y1, y2, t=200):
        print("x, y1, x, y2", x, y1, x, y2)
        self.driver.swipe(x, y1, x, y2, t)

    def tapEle(self, x1, y1, x2, y2, time=0.01):
        self.driver.tap([(x1, y1),(x2, y2)], time)

    def hideKeyboard(self):
        try:
            self.driver.hide_keyboard()
        except:
            logger.info("Soft keyboard not present, cannot hide keyboard")
            pass

    def pressKeyCode(self, keycode=None):
        self.driver.press_keycode(keycode)

    def close(self):
        self.driver.close()

    def quit(self):
        self.driver.quit()

    def is_app_installed(self):
        return self.driver.is_app_installed(self.desired_caps.get('package'))

    # def install_app(self):
    #     return self.driver.install_app(APK_PATH + '\{}'.format(self.apk_file))

    def remove_app(self):
        return self.driver.remove_app(self.desired_caps.get('package'))

    def launch_app(self):
        return self.driver.launch_app()

    def close_app(self):
        return self.driver.close_app()

    def background_app(self, background_time=1):
        if background_time:
            return self.driver.background_app(background_time)
        else:
            return self.driver.background_app(self.desired_caps.get('background_time'))

    def set_network_connection(self, conn_type=0):
        conn = {
            '0': 'NO_CONNECTION',
            '1': 'AIRPLANE_MODE',
            '2': 'WIFI_ONLY',
            '4': 'DATA_ONLY',
            '6': 'ALL_NETWORK_ON',
        }

        if str(conn_type) in conn:
            if conn_type == 0:
                self.driver.set_network_connection(ConnectionType.NO_CONNECTION)
            elif conn_type == 1:
                self.driver.set_network_connection(ConnectionType.AIRPLANE_MODE)
            elif conn_type == 2:
                self.driver.set_network_connection(ConnectionType.WIFI_ONLY)
            elif conn_type == 4:
                self.driver.set_network_connection(ConnectionType.DATA_ONLY)
            elif conn_type == 6:
                self.driver.set_network_connection(ConnectionType.ALL_NETWORK_ON)
        else:
            print("None conn type")

    def test_view(self):
        pass


if __name__ == "__main__":
    b = WebView()
    b.get()