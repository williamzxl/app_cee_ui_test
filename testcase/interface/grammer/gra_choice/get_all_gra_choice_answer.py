import requests
import json
from utils.log import logger
from utils.config import get_http


class GetAllGraChoiceAnswers(object):
    def __init__(self, headers):
        self.pr = get_http()
        self.headers = headers
        self.url = self.headers.get('Host')


    def get_all_gra_choice_answer(self, groupID, taskID):
        url = "{}://{}/sysGrammar/{}/mulChoice".format(self.pr, self.url, groupID)
        querystring = {"groupID": "{}".format(groupID), "taskID": "{}".format(taskID)}
        logger.info("语法单选 URL is：{}".format(url))
        response = requests.request("GET", url, headers=self.headers, params=querystring)
        answer = response.text
        json_data = json.loads(answer)
        result = json_data.pop("data").pop('questGuide')
        logger.info("语法单选的全部 result".format(result))
        word_answers = []
        for a in result:
            word_answers.append(a.pop('questAnswer'))
        logger.info("语法单选 tID {} gID {} answers:{}".format(taskID, groupID, word_answers))
        return word_answers


    def gra_choice_right_answer(self, answer, num):
        get_answer = answer[:]
        right_answer = get_answer.pop(int(num)-1)
        logger.info("语法单选的正确答案：{}".format(right_answer))
        return right_answer


    def gra_choice_wrong_answer(self, answer, num):
        get_answer = answer[:]
        test = get_answer.pop(int(num)-1)
        wrong_answer = []
        if (ord(test) + 1) <= 68:
            wrong_answer.append(chr(ord(test) + 1))
        else:
            wrong_answer.append(chr(ord(test) -1))
        logger.info("语法单选的错误答案：".format("".join(wrong_answer)))
        return "".join(wrong_answer)


if __name__ == '__main__':
    test = GetAllGraChoiceAnswers()
    answers = test.get_all_gra_choice_answer(1866, 32454)
    print(answers)
    r = test.gra_choice_right_answer(answers, 1)
    print(r)