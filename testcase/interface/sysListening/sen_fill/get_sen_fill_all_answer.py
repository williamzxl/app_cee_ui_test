import requests
import json
from utils.config import get_http
from utils.log import logger


class GetAllSenFillAnswers(object):
    def __init__(self):
        self.pr = get_http()
        # self.url = self.headers.get('Host')
        self.pas = None

    def get_all_sen_fill_answer(self, headers, groupID, taskID):
        host = headers.get('Host')
        url = "{}://{}/sysListening/{}/senFill".format(self.pr, host, groupID)
        querystring = {"taskID": "{}".format(taskID)}
        logger.log("句子填充 tID {}, gID {}, url is:{}".format(taskID, groupID, url))
        response = requests.request("GET", url, headers=headers, params=querystring)
        answer = response.text
        logger.log("句子填充 tID {}, gID {}, response is:{}".format(taskID, groupID, answer))
        json_data = json.loads(answer)
        result = json_data.pop("data").pop('questGuide')
        logger.log("句子填充 tID {}, gID {}, result is:{}".format(taskID, groupID, result))
        word_answers = []
        for a in result:
            word_answers.append(a.pop('questAnswer'))
        logger.log("句子填充 tID {}, gID {}, all answers is:{}".format(taskID, groupID, word_answers))
        return (word_answers)

    def sen_fill_right_answer(self, answer, num):
        get_answer = answer[:]
        right_answer = get_answer.pop(int(num)-1)
        logger.log("句子填充 right answer is:{}".format(right_answer))
        return right_answer

    def sen_fill_wrong_answer(self, answer, num):
        get_answer = answer[:]
        test = get_answer.pop(int(num)-1)
        wrong_answer = []
        for i in test:
            wrong_answer.append(i[::-1])
        # wrong_answer = "".join(wrong_answer)
        logger.log("句子填充 wrong answer is:{}".format(wrong_answer))
        return wrong_answer

    #
    # answer = get_all_sen_fill_answer(list=1431, taskID=1)
    # print(right_answer_sen_fill(answer, 1))
    # print(wrong_answer_sen_fill(answer, 1))
    # print(tuple(answer))
    #
