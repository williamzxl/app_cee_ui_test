import requests
import json
from utils.config import get_http
from utils.log import logger


class GetAllWordDictAnswers(object):
    def __init__(self):
        self.pr = get_http()
        self.pas = None

    def get_all_dict_answer(self, headers, groupID, taskID):
        host = headers.get('Host')
        url = "{}://{}/sysListening/{}/wordDic".format(self.pr, host, str(groupID))
        querystring = {"taskID": "{}".format(str(taskID))}
        logger.info("单词听写 gID:{}, tID：{}， 获取答案的URL:{}".format(groupID, taskID, url))
        response = requests.request("GET", url, headers=headers, params=querystring)
        answer = response.text
        logger.info("单词听写返回值：{}".format(answer))
        json_data = json.loads(answer)
        result = json_data.pop("data").pop('questGuide')
        logger.info("单词听写 Result:{}".format(result))
        word_answers = []
        for a in result:
            word_answers.append(a.pop('wordEN'))
        logger.info("单词听写所有答案 :{}".format(word_answers))
        return word_answers

    def dict_right_answer(self, answer, num):
        get_answer = answer[:]
        right_answer = get_answer.pop(int(num)-1)
        logger.info("单词听写 正确答案：{}".format(right_answer))
        return right_answer

    def dict_wrong_answer(self, answer, num):
        get_answer = answer[:]
        test = get_answer.pop(int(num)-1)
        wrong_answer = []
        for i in test:
            if chr(ord(i) + 1).isalpha():
                wrong_answer.append(chr(ord(i) + 1))
            else:
                wrong_answer.append(chr(ord(i) -1))
        wrong_answer = "".join(wrong_answer)
        logger.info("单词听写 错误答案：{}".format(wrong_answer))
        return wrong_answer


if __name__ == '__main__':
    test = GetAllWordDictAnswers()
    word_answers = test.get_all_dict_answer(1104, 16484)
    print(word_answers)
    test.dict_right_answer(word_answers, 1)
