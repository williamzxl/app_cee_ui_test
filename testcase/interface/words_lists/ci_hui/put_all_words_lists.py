import requests
import json
from utils.config import get_http
from utils.log import logger


class PutAllWordsListsDone(object):
    def __init__(self):
        self.pr = get_http()
        # self.url = self.headers.get('Host')
        # self.http = self.headers.get('http')
        self.pas = None

    def put_all_words_lists_done(self, headers, taskID, groupID):
        host = headers.get("Host")
        if taskID == None or groupID == None:
            pass
        else:
            url = "{}://{}/userVoc/{}/{}/vocStatus".format(self.pr, host, taskID, groupID)
            logger.info("Post 词汇 URL:{}".format(url))
            headers.update({'Content-Type': 'application/json; charset=utf-8','Content-Length': '0'})
            logger.info("Post 词汇 Header:{}".format(headers))
            response = requests.request("PUT", url, headers=headers)
            logger.info("Post 词汇 Response:{}".format(response))
            return response


if __name__ == '__main__':
    test = PutAllWordsListsDone()
    headers = {'Platform': 'Android', 'appkey': 'CEE_AA8F55B916AB', 'appversion': '10000004', 'AppSecret': '3DB5159C-EB1E-47FE-8584-47115EF5E443', 'App': 'cee', 'accesstoken': 'd5a1206b-d1bd-4d70-932d-dbededb9b40b', 'Host': 'appncee.langlib.com', 'Connection': 'Keep-Alive', 'Accept-Encoding': 'gzip', 'User-Agent': 'okhttp/3.11.0', 'Content-Type': 'application/json; charset=utf-8', 'Content-Length': '0'}
    r = test.put_all_words_lists_done(headers, 34874, 2607)
    print(r)