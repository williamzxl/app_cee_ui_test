import requests
import json
from utils.log import logger
from utils.config import get_http


class GetAllGraFillAnswers(object):
    def __init__(self):
        # self.headers = headers
        # self.url = self.headers.get('Host')
        self.pr = get_http()
        self.pas = None

    def get_all_gra_fill_answer(self, headers, groupID, taskID):
        host = headers.get('Host')
        url = "{}://{}/sysGrammar/{}/graFill".format(self.pr, host, groupID)
        querystring = {"taskID": "{}".format(taskID)}
        logger.info("语法填空 tID {} gID {} url:{}".format(taskID, groupID, url))
        response = requests.request("GET", url, headers=headers, params=querystring)
        answer = response.text
        json_data = json.loads(answer)
        result = json_data.pop("data").get('questGuide')
        logger.info("语法填空 tID {} gID {} result:{}".format(taskID, groupID, result))
        word_answers = []
        for k, v in result[0].items():
            if type(v) == type([1]):
                for i in v[1].pop('subQuestGuide'):
                    word_answers.append(i.get('questAnswer'))
        logger.info("语法填空 tID {} gID {} answers:{}".format(taskID, groupID, word_answers))
        return word_answers


    def gra_fill_right_answer(self, answer):
        get_answer = answer[:]
        # right_answer = get_answer.pop(int(num)-1)
        right_answer = get_answer
        logger.info("语法填空 right answer:{}".format(right_answer))
        return right_answer

    def gra_fill_wrong_answer(self, answer):
        get_answer = answer[:]
        # test = get_answer.pop(int(num)-1)
        wrong_answer = []
        for w in get_answer:
            wrong_answer.append(w[::-1])
        logger.info("语法填空 right answer:{}".format(wrong_answer))
        return wrong_answer

    #
    # def wrong_answer_gra_choice(answer, num):
    #     get_answer = answer[:]
    #     test = get_answer.pop(int(num)-1)
    #     wrong_answer = []
    #     for w in test:
    #         if chr(ord(w.lower()) + 1).isalpha():
    #             wrong_answer.append(chr(ord(w.lower()) + 1))
    #         else:
    #             wrong_answer.append(chr(ord(w.lower()) - 1))
    #     return "".join(wrong_answer)

    #


if __name__ == '__main__':
    test = GetAllGraFillAnswers()
    answer = test.get_all_gra_fill_answer(groupID=2438, taskID=33913)
    print(test.gra_fill_right_answer(answer))
    print(test.gra_fill_wrong_answer(answer))
