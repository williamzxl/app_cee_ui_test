import requests
import json
from itertools import chain
from utils.config import get_http
from utils.log import logger


class GetAllSenAnAAnswers(object):
    def __init__(self):
        self.pr = get_http()
        # self.url = self.headers.get('Host')
        self.pas = None

    def get_all_sen_analysis_answer(self, headers, groupID, taskID):
        host = headers.get('Host')
        url = "{}://{}/sysReading/{}/senAnalysis".format(self.pr, host, groupID)
        querystring = {"taskID": "{}".format(taskID)}
        logger.info("句子分析 tID {}, gID {}， url is {}".format(taskID, groupID, url))
        response = requests.request("GET", url, headers=headers, params=querystring)
        answer = response.text
        json_data = json.loads(answer)
        result = json_data.pop("data").pop('questGuide')
        logger.info("句子分析 tID {}, gID {}， result is {}".format(taskID, groupID, result))
        all_answers = []
        all_answers_choice = []
        for q in result:
            all_questAnswer = q.get('subQuestGuide')
            all_answers.append([a.get('questAnswer') for a in all_questAnswer])
            all_answers_choice.append([a.get('questChoices') for a in all_questAnswer])
        logger.info("句子分析 tID {}, gID {}， all answers is {}".format(taskID, groupID, all_answers))
        logger.info("句子分析 tID {}, gID {}， all answer choice is {}".format(taskID, groupID, all_answers_choice))
        return all_answers, all_answers_choice

    def right_answer_sen_ana(self, answers, answers_choice, sen_num=None, ques_num=None):
        try:
            choice_EN = answers[sen_num-1][ques_num - 1]
            answers_choice = list(chain(*answers_choice))
            if choice_EN:
                if choice_EN.isupper():
                    for cn in list(chain(*answers_choice)):
                        if choice_EN == cn.get('choiceTag'):
                            choice_CN = cn.get('choiceCN')
                            if choice_CN:
                                logger.info("句子分析 choice_CN ：{}, choice_EN ：{}".format(choice_CN, choice_EN))
                                return choice_CN, choice_EN
                else:
                    logger.info("句子分析 choice_EN ：{} and {}".format(choice_EN, "None"))
                    return choice_EN, None
            else:
                logger.info("句子分析 choice_CN ：{}, choice_EN ：{}".format(0, "None"))
                return 0, None
        except:
            pass

    def wrong_answer_sen_ana(self, answers, answers_choice, sen_num=None, ques_num=None):
        choice_EN = answers[sen_num - 1][ques_num - 1]
        print("Choice_EN:", choice_EN)
        answers_choice = list(chain(*answers_choice))
        if choice_EN:
            if choice_EN.isupper():
                print(list(chain(*answers_choice)))
                for cn in list(chain(*answers_choice)):
                    if choice_EN == cn.get('choiceTag'):
                        choice_CN = cn.get('choiceCN')
                        if choice_CN:
                            logger.info("句子分析 Wrong choice_CN ：{}".format(choice_CN))
                            return choice_CN
            else:
                logger.info("句子分析 Wrong choice_EN ：{} Test.".format(choice_EN))
                return choice_EN + "Test"
        else:
            return 0


if __name__ == '__main__':
    test = GetAllSenAnAAnswers()
    answers, answers_choice = test.get_all_sen_analysis_answer(2579, 32515)
    # right = test.right_answer_sen_ana(answers, answers_choice, 3, 1)
    # wrong  = wrong_answer_sen_ana(answers, answers_choice, 5, 2)
    # print(right)
    # print(wrong)
    print(answers)
    right = test.right_answer_sen_ana(answers, answers_choice, 2, 2)
    print(right)
    print(answers_choice)
