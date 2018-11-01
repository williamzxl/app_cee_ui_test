import requests
import json
# from utils.config import get_headers
from utils.config import get_http
from utils.log import logger


class GetAllClozeTestAnswers(object):
    def __init__(self):
        self.pr = get_http()
        # self.url = self.headers.get('Host')
        self.pas = None

    def get_all_cloze_test_answer(self, headers, groupID, taskID):
        host = headers.get("Host")
        url = "{}://{}/sysReading/{}/clozeTest".format(self.pr, host, groupID)
        querystring = {"taskID": "{}".format(taskID)}
        logger.info("完型训练 tID {} gID {} url is:{}".format(taskID, groupID, url))
        response = requests.request("GET", url, headers=headers, params=querystring)
        answer = response.text
        json_data = json.loads(answer)
        result = json_data.pop("data").pop('questGuide')
        logger.info("完型训练 tID {} gID {} result is:{}".format(taskID, groupID, result))
        all_answers = []
        for r in result:
            for step in (r.get('steps')):
                if step.get('subQuestGuide'):
                    for a in (step.get('subQuestGuide')):
                        all_answers.append([a.get("questWordSpeech"), a.get("questAnswer")])
        logger.info("完型训练 tID {} gID {} all answers is:{}".format(taskID, groupID, all_answers))
        return all_answers

    def cloze_test_right_answer(self, answers, ques_num=None):
        curr_answer = answers[int(ques_num) - 1]
        CN_answer = curr_answer[0]
        EN_answer = curr_answer[1]
        logger.info("完型训练 Right CN answer:{}, EN_answer:{}".format(CN_answer, EN_answer))
        return CN_answer, EN_answer

    def cloze_test_wrong_answer(self, answers, sen_num=None, ques_num=None):
        choice_EN = answers[sen_num - 1][ques_num - 1]
        logger.info("完型训练 Wrong CN answer:{}".format(choice_EN.upper()))
        return choice_EN.upper()


if __name__ == '__main__':
    test = GetAllClozeTestAnswers()
    right = test.get_all_cloze_test_answer(2511, 24761)
    print(right)
    print(len(right))
    r_CN, r_EN = test.cloze_test_right_answer(right, 1)
    print(r_CN, r_EN)