import json
import requests
from utils.config import get_http
from utils.log import logger


class GetTaskGroupNum(object):
    def __init__(self):
        self.pr = get_http()
        # self.url = self.headers.get('Host')
        pass

    def get_service_id(self, headers):
        host = headers.get("Host")
        url = "{}://{}/userStudyCenter/serviceInfo".format(self.pr, host)
        querystring = {"serviceID":""}
        logger.info("Get service id url is:{}".format(url))
        response = requests.request("GET", url, headers=headers, params=querystring)
        result = response.text
        logger.info("Service ID result is :{}".format(result))
        json_data = json.loads(result)
        data = json_data.pop("data")
        logger.info("ServiceID is :{}".format(data.get('serviceID')))
        return (data.get('serviceID'))


    def get_task_group_id(self, headers, serviceId):
        task_group = []
        host = headers.get("Host")
        url = "{}://{}/userStudyCenter/{}/taskInfo".format(self.pr, host, serviceId)
        querystring = {"taskID": ""}
        logger.info("Get Task group ID url is:{}".format(url))
        response = requests.request("GET", url, headers=headers, params=querystring)
        json_data = json.loads(response.text)
        try:
            result0 = json_data.get("data").get('userCourse').get('mtdCourse')
        except:
            pass
        result = json_data.get("data").get('practice')
        try:
            for n in result:
                task_group.append(n)
        except:
            pass
        for i in result:
            for j in i.get("questGuide"):
                task_group.append(j)
        logger.info("GroupID is :{}".format(task_group))
        return task_group


if __name__ == '__main__':
    task_group = GetTaskGroupNum()
    serviceID = task_group.get_service_id()
    print(serviceID)
    result = task_group.get_task_group_id(serviceID)
    for i in result:
        print(i.get("groupID"), i.get("taskID"), i.get("currStatus"))


