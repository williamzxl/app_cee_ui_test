import requests
import json
from utils.config import get_http
from utils.log import logger


class GetAllWordsListsAnswers(object):
    def __init__(self):
        self.pr = get_http()
        # self.url = self.headers.get('Host')
        self.pas = None

    def get_all_words_lists_answer(self, headers, servicesID):
        host = headers.get("Host")
        url = "{}://{}/userStudyCenter/{}/taskInfo".format(self.pr, host, servicesID)
        querystring = {"taskID": ""}
        logger.info("词汇列表的 sID:{}, URL:{}".format(servicesID, url))
        response = requests.request("GET", url, headers=headers, params=querystring)
        answer = response.text
        logger.info("词汇列表的返回值：{}".format(answer))
        json_data = json.loads(answer)
        result = json_data.pop("data").pop('practice')
        logger.info("词汇列表的 Result:{}".format(result))
        all_words_lists = []
        for r in result:
            all_lists = r.get('questGuide')
            for a in all_lists:
                all_words_lists.append(a.get('servicePracticeIdx'))
        logger.info("词汇列表的所有单词列表：{}".format(all_words_lists))
        return all_words_lists

    def get_all_words_groupId(self, headers, servicesID):
        host = headers.get("Host")
        url = "{}://{}/userStudyCenter/{}/taskInfo".format(self.pr, host, servicesID)
        querystring = {"taskID": ""}
        logger.info("获取词汇的Group ID  URL:{}".format(url))
        response = requests.request("GET", url, headers=headers, params=querystring)
        answer = response.text
        logger.info("获取词汇的Group ID的返回值：{}".format(answer))
        json_data = json.loads(answer)
        result = json_data.pop("data").pop('practice')
        all_words_lists_groupID = []
        for r in result:
            all_lists = r.get('questGuide')
            for a in all_lists:
                all_words_lists_groupID.append(a.get('groupID'))
        logger.info("返回所有词汇的Group ID :{}".format(all_words_lists_groupID))
        return all_words_lists_groupID


if __name__ == '__main__':
    test = GetAllWordsListsAnswers()
    # all_lists = test.get_all_words_lists_answer("P90")
    # print(all_lists)
    gId = test.get_all_words_groupId("P90")
    print(gId)