import requests
import json
# from utils.config import get_headers

pro = "https"


class GetAllWordsListsAnswers(object):
    def __init__(self):
        # self.headers = headers
        # self.url = self.headers.get('Host')
        self.pas = None

    def get_all_words_lists_answer(self, headers, servicesID):
        host = headers.get("Host")
        url = "{}://{}/userStudyCenter/{}/taskInfo".format(pro, host, servicesID)
        querystring = {"taskID": ""}
        response = requests.request("GET", url, headers=headers, params=querystring)
        answer = response.text
        json_data = json.loads(answer)
        result = json_data.pop("data").pop('practice')
        all_words_lists = []
        for r in result:
            all_lists = r.get('questGuide')
            for a in all_lists:
                all_words_lists.append(a.get('servicePracticeIdx'))
        return all_words_lists

    def get_all_words_groupId(self, headers, servicesID):
        host = headers.get("Host")
        url = "{}://{}/userStudyCenter/{}/taskInfo".format(pro, host, servicesID)
        querystring = {"taskID": ""}
        response = requests.request("GET", url, headers=headers, params=querystring)
        answer = response.text
        json_data = json.loads(answer)
        result = json_data.pop("data").pop('practice')
        all_words_lists_groupID = []
        for r in result:
            all_lists = r.get('questGuide')
            for a in all_lists:
                all_words_lists_groupID.append(a.get('groupID'))
        return all_words_lists_groupID


if __name__ == '__main__':
    test = GetAllWordsListsAnswers()
    # all_lists = test.get_all_words_lists_answer("P90")
    # print(all_lists)
    gId = test.get_all_words_groupId("P90")
    print(gId)