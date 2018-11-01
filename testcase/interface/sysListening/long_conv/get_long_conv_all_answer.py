import requests
import json
from utils.config import get_http
from utils.log import logger


class GetAllLongConvAnswers(object):
    def __init__(self):
        self.pr = get_http()
        # self.url = self.eaders.get('Host')
        self.pas = None

    def get_all_long_conv_answer(self, headers, groupID, taskID):
        host = headers.get('Host')
        url = "{}://{}/sysListening/{}/longConv".format(self.pr, host, groupID)
        querystring = {"taskID": "{}".format(taskID)}
        logger.info("长对话 tID {}, gID {} url is:{}".format(taskID,groupID, url))
        response = requests.request("GET", url, headers=headers, params=querystring)
        answer = response.text
        json_data = json.loads(answer)
        result = json_data.pop("data").pop('questGuide')
        logger.info("长对话 tID {}, gID {} Result is:{}".format(taskID,groupID, result))
        word_answers = []
        for r in result:
            for answer in r.pop('subQuestGuide'):
                word_answers.append(answer.get('questAnswer'))
        logger.info("长对话 tID {}, gID {} Answers is:{}".format(taskID,groupID, word_answers))
        return (word_answers)


    def long_conv_right_answer(self, answer, num):
        get_answer = answer[:]
        right_answer = get_answer.pop(int(num)-1)
        logger.info("长对话 right Answer is:{}".format(right_answer))
        return right_answer


    def long_conv_wrong_answer(self, answer, num):
        get_answer = answer[:]
        test = get_answer.pop(int(num)-1)
        if ord(test) + 1 <= 67:
            wrong_answer = chr(ord(test) + 1)
        else:
            wrong_answer = chr(ord(test) - 1)
        logger.info("长对话 Wrong Answer is:{}".format(wrong_answer))
        return wrong_answer
        # get_answer = answer[:]
        # test = get_answer.pop(int(num)-1)
        # wrong_answer = []
        # for test in get_answer:
        #     if ord(test) + 1 <= 67:
        #         wrong_answer.append(chr(ord(test) + 1))
        #     else:
        #         wrong_answer.append(chr(ord(test) - 1))
        # return wrong_answer


if __name__ == '__main__':
    a = GetAllLongConvAnswers()
    answer = a.get_all_long_conv_answer(1826, 23289)
    print(len(answer))
    print(a.long_conv_right_answer(answer, 1))
    print(a.long_conv_wrong_answer(answer, 1))
    print(tuple(answer))

