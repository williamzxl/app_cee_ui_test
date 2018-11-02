import os
import yaml
from time import sleep
import multiprocessing
# from testcase.page.api.login.login_branch.login_post_step1 import LoginToGetAccessToken


def read_dev_cfg():
    devices = []
    new_devices = []
    env = None
    with open(os.getcwd().split("utils")[0] + "\config\devices_cfg.yml") as f:
        data = list(yaml.safe_load_all(f))
        for d in data:
            for d1 in d:
                devices.append(list(d1.items()))
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
    for d1 in devices:
        for info1 in d1:
            if info1[0] != "common":
                for k, v in info1[1].items():
                    for k1, v1 in v.items():
                        if v1 == None:
                            v.update({k1: globals_info.get(k1)})
    for result in devices:
        for r in result:
            if r[0] != "common":
                if r[1].get("headers").get("accesstoken") == None:
                    # get_access_token = LoginToGetAccessToken()
                    headers = r[1].get('headers')
                    if env.lower() == "test":
                        headers.update({"Host": r[1].get("account").get("loginProxy_test")})
                        headers.pop("accesstoken")
                        common = {}
                        common.update({"loginUrl": r[1].get("account").get("loginUrl_test")})
                        common.update({'uname': r[1].get("account").get("uname")})
                        common.update({'pwd': r[1].get("account").get("pwd")})
                        common.update({'loginProxy': headers.get('Host')})
                        # accesstoken = get_access_token.get_access_token(common=common, headers=headers)
                        # logger.info("accesstoken: {}".format(accesstoken))
                        # r[1].get("headers").update({"accesstoken": accesstoken})
                        r[1].get("headers").update({"Host": globals_info.get("Host")})
                    if env.lower() != "test":
                        headers.update({"Host": r[1].get("account").get("loginProxy_cus")})
                        headers.pop("accesstoken")
                        common = {}
                        common.update({"loginUrl": r[1].get("account").get("loginUrl_cus")})
                        common.update({'uname': r[1].get("account").get("uname")})
                        common.update({'pwd': r[1].get("account").get("pwd")})
                        common.update({'loginProxy': headers.get('Host')})
                        # accesstoken = get_access_token.get_access_token(common=common, headers=headers)
                        # logger.info("accesstoken: {}".format(accesstoken))
                        # r[1].get("headers").update({"accesstoken": accesstoken})
                        r[1].get("headers").update({"Host": globals_info.get("Host")})
                new_devices.append([r[1]])
    return new_devices

def open_appium(appium_url, d, h, a):
    port = str(appium_url.get("url").split("http://127.0.0.1:")[1]).split("/wd/hub")[0]
    cmd = "appium -p {} -bp {} --udid {}".format(port, int(port) + 2, d.get("udid"))
    print("CMD:", cmd)
    os.system(cmd)
    sleep(30)

def open_many_appium(new_devices):
    pool_open_appium = multiprocessing.Pool(processes=2)
    for device in new_devices:
        print("Devices:",device)
        pool_open_appium.apply_async(open_appium, (device[0].get('appium_url'), device[0].get('desired_caps'), device[0].get("headers"), device[0].get('account')))
    pool_open_appium.close()
    pool_open_appium.join()


if __name__ == '__main__':
    new_devices = read_dev_cfg()
    open_many_appium(new_devices)
