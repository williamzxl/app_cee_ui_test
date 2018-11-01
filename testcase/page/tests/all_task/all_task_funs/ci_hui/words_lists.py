from time import sleep
from testcase.page.learn_center.all_class import AllPage
from testcase.page.study_center.study_center_main_page import StudyCenter
from testcase.interface.all_interface import AllInterface


class HomeWork(AllInterface, StudyCenter, AllPage):
    pass


def words_lists(homework, headers, taskID, serviceID):
    cihui = HomeWork()
    all_group_lists = cihui.get_all_words_groupId(headers, serviceID)
    for gID in all_group_lists:
        cihui.put_all_words_lists_done(headers, taskID, gID)

