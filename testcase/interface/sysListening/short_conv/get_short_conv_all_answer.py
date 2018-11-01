import requests
import json
from utils.config import get_http
from utils.log import logger


class GetAllShortConvAnswers(object):
    def __init__(self):
        self.pr = get_http()
        # self.url = self.headers.get('Host')
        self.pas = None

    def get_all_short_conv_answer(self, headers, groupID, taskID):
        host = headers.get('Host')
        url = "{}://{}/sysListening/{}/shortConv".format(self.pr, host, groupID)
        querystring = {"taskID": "{}".format(taskID)}
        logger.info("短对话 tID {},gID {}, url is:{}".format(taskID,groupID, url))
        response = requests.request("GET", url, headers=headers, params=querystring)
        answer = response.text
        logger.info("短对话 tID {},gID {}, response is:{}".format(taskID, groupID, answer))
        json_data = json.loads(answer)
        result = json_data.pop("data").pop('questGuide')
        word_answers = []
        for r in result:
            for answer in r.pop('subQuestGuide'):
                word_answers.append(answer.get('questAnswer'))
        logger.info("短对话 tID {},gID {}, url is:{}".format(taskID, groupID, url))
        return (word_answers)


    def right_answer_short_conv(self, answer, num):
        get_answer = answer[:]
        right_answer = get_answer.pop(int(num)-1)
        logger.info("短对话 right answer is:{}".format(right_answer))
        return right_answer


    def wrong_answer_short_conv(self, answer, num):
        get_answer = answer[:]
        test = get_answer.pop(int(num)-1)
        if ord(test) + 1 <= 68:
            wrong_answer = chr(ord(test) + 1)
        else:
            wrong_answer = chr(ord(test) - 1)
        logger.info("短对话 wrong answer is:{}".format(wrong_answer))
        return wrong_answer

    #
    # answer = get_all_short_conv_answer(list=1501, taskID=1)
    # print(right_answer_sen_fill(answer, 2))
    # print(wrong_answer_sen_fill(answer, 2))
    # print(tuple(answer))

