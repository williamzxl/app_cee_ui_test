import os
import yaml
import multiprocessing
from testcase.page.tests.all_task.all_task_funcs import *
from testcase.page.learn_center.all_class import AllPage
from testcase.page.study_center.study_center_main_page import StudyCenter
from testcase.interface.all_interface import AllInterface
from testcase.interface.study_center.get_study_center_serverID import GetTaskGroupNum
from utils.log import logger
from testcase.page.api.login.login_branch.login_post_step1 import LoginToGetAccessToken

class HomeWork(AllInterface):
    pass


class HomeWork1(StudyCenter, AllPage, GetTaskGroupNum):
    pass


def main_all(appium_url, d, h, a):
    import os
    port = str(appium_url.get("url").split("http://127.0.0.1:")[1]).split("/wd/hub")[0]
    print("Port", port, d.get("udid"))
    cmd = "appium -p {} -bp {} -U {}".format(port, int(port) + 2, d.get("udid"))
    print(cmd)
    os.system("appium -p {} -bp {} -U {}".format(port, int(port) + 2, d.get("udid")))
    print("DDDDDDDDDDDD", d)
    sleep(30)
    while True:
        try:
            main1(appium_url, d, h, a)
            pass
        except:
            pass
        finally:
            pass


if __name__ == '__main__':
    devices = []
    new_devices = []
    env = None
    with open(os.getcwd().split("testcase")[0] + "\config\devices_cfg.yml") as f:
        data = list(yaml.safe_load_all(f))
        for d in data:
            for d1 in d:
                devices.append(list(d1.items()))
    logger.info("Old devices: {}".format( devices))
    globals_info = None
    for d in devices:
        for info in d:
            globals = None
            if "globals" in list(info[1].keys()):
                globals = info[1].get('globals')
                env = (globals.get("env"))
                if env.lower() == "test":
                    globals.pop("Host_cus")
                    globals.update({"Host": globals.get("Host_test")})
                    globals.pop("loginUrl_cus")
                    globals.update({"loginUrl": globals.get("loginUrl_test")})
                    globals.pop("loginProxy_cus")
                    globals.update({"loginProxy": globals.get("loginProxy_test")})
                if env.lower() != "test":
                    globals.pop("Host_test")
                    globals.update({"Host": globals.get("Host_cus")})
                    globals.pop("loginUrl_test")
                    globals.update({"loginUrl": globals.get("loginUrl_cus")})
                    globals.pop("loginProxy_test")
                    globals.update({"loginProxy": globals.get("loginProxy_cus")})
                globals_info = globals
    logger.info("globals_info: {}".format(globals_info))
    for d1 in devices:
        for info1 in d1:
            if info1[0] != "common":
                logger.info("INFO1: {}".format(info1))
                for k, v in info1[1].items():
                    for k1, v1 in v.items():
                        if v1 == None:
                            v.update({k1:globals_info.get(k1)})

    for result in devices:
        for r in result:
            if r[0] != "common":
                if r[1].get("headers").get("accesstoken") == None:
                    get_access_token = LoginToGetAccessToken()
                    headers = r[1].get('headers')
                    if env.lower() == "test":
                        headers.update({"Host":r[1].get("account").get("loginProxy_test")})
                        headers.pop("accesstoken")
                        common = {}
                        common.update({"loginUrl":r[1].get("account").get("loginUrl_test")})
                        common.update({'uname':r[1].get("account").get("uname")})
                        common.update({'pwd': r[1].get("account").get("pwd")})
                        common.update({'loginProxy':headers.get('Host')})
                        accesstoken = get_access_token.get_access_token(common=common, headers=headers)
                        logger.info("accesstoken: {}".format(accesstoken))
                        r[1].get("headers").update({"accesstoken":accesstoken})
                        r[1].get("headers").update({"Host": globals_info.get("Host")})
                    if env.lower() != "test":
                        headers.update({"Host": r[1].get("account").get("loginProxy_cus")})
                        headers.pop("accesstoken")
                        common = {}
                        common.update({"loginUrl": r[1].get("account").get("loginUrl_cus")})
                        common.update({'uname': r[1].get("account").get("uname")})
                        common.update({'pwd': r[1].get("account").get("pwd")})
                        common.update({'loginProxy': headers.get('Host')})
                        accesstoken = get_access_token.get_access_token(common=common, headers=headers)
                        logger.info("accesstoken: {}".format(accesstoken))
                        r[1].get("headers").update({"accesstoken": accesstoken})
                        r[1].get("headers").update({"Host": globals_info.get("Host")})
                new_devices.append([r[1]])
    # for result in new_devices:
    #     print(result)
    logger.info("new_devices: {} ".format(new_devices))
    pool = multiprocessing.Pool(processes=2)
    for device in new_devices:
        print(device[0].get('appium_url'))
        print(device[0].get("headers"))
        print(device[0].get('desired_caps'))
        print(device[0].get('account'))
        pool.apply_async(main_all, (device[0].get('appium_url'), device[0].get('desired_caps'), \
                                    device[0].get("headers"), device[0].get('account')))
    pool.close()
    pool.join()
