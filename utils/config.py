import os
from utils.file_reader import YamlReader

'''
    List home_page dirs
'''
BASE_PATH = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
CONFIG_PATH = os.path.join(BASE_PATH, 'config')
DATA_PATH = os.path.join(BASE_PATH, 'data')
APK_PATH = os.path.join(BASE_PATH, 'apk')
LOG_PATH = os.path.join(BASE_PATH, 'log')
REPORT_PATH = os.path.join(BASE_PATH, 'report')
TEST_PATH = os.path.join(BASE_PATH, 'testcase\case')


class BeforeConfig(object):
    def __init__(self):
        self.config = CONFIG_PATH + "\config.yml"


all_configs = CONFIG_PATH + "\config.yml"
new_all_cfg = CONFIG_PATH + "\devices_cfg.yml"


class Config(object):
    def __init__(self, config=all_configs):
        self.configs = YamlReader(config).data

    def get(self, element):
        for config in self.configs:
            for i in range(len(config)):
                if element in config[i]:
                    yield config[i].get(element)


class NewConfig(object):
    def __init__(self, config=all_configs):
        self.configs = YamlReader(config).data

    def get(self, element):
        for config in self.configs:
            for i in range(len(config)):
                if element in config[i]:
                    yield config[i].get(element)


def get_desired_caps(appium_url='appium_url', caps='desired_caps_info'):
    cfg_info = Config()
    desired_caps = {}
    appium_url = cfg_info.get(appium_url)
    for ur in appium_url:
        url = ur
    content = cfg_info.get(caps)
    for info in content:
        desired_caps.update(info)
    return (desired_caps)

def get_appPackage(caps='desired_caps_info'):
    cfg_info = Config()
    # print(cfg_info)
    app_package = {}
    content = cfg_info.get(caps)
    for info in content:
        app_package.update(info)
    return app_package.get("appPackage")


def get_http(name="http/https"):
    cfg_info = Config()
    content = cfg_info.get(name)
    for info in content:
        return info.get('protocal')

# def get_headers(heads='common'):
#     cfg_info = Config()
#     headers = {}
#     header_info = cfg_info.get(heads)
#     for header in header_info:
#         headers.update(header)
#     # print("headers,",headers)
#     return headers


# def get_device_name(caps='desired_caps_info'):
#     cfg_info = Config()
#     devices_name = {}
#     content = cfg_info.get(caps)
#     for info in content:
#         devices_name.update(info)
#     return devices_name.get("deviceName")


if __name__ == "__main__":
    # result = get_desired_caps(appium_url='appium_url1',caps='desired_caps_info1')
    # print(result[1])
    # print(result[0].pop('appPackage'))
    # print(result[1].pop('headers'))
    # headers = get_headers()
    # host = headers.get('Host')
    # print(headers)
    # print(host)
    # appPackage = get_appPackage()
    # print(appPackage)
    # devices_name = get_device_name(caps='desired_caps_info1')
    # print(devices_name)
    pass

