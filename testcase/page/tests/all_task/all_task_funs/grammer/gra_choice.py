from testcase.page.learn_center.all_class import AllPage
from testcase.page.study_center.study_center_main_page import StudyCenter
from testcase.interface.all_interface import AllInterface


class HomeWork(AllInterface, StudyCenter, AllPage):
    pass


def gra_choice(home_work, headers, k0, k1, click_result):
    gra_choice = HomeWork()
    gra_choice_answers = gra_choice.get_all_gra_choice_answer(headers, k0, k1)
    if int(click_result) == 2:
        home_work.click_finish_button()
        home_work.click_back_btn()
    else:
        curr, total = home_work.get_gra_choice_lists_nums()
        for j in range(int(curr), int(total) + 1):
            if j == int(total):
                current_right_answer = gra_choice.gra_choice_right_answer(gra_choice_answers, j)
                current_wrong_answer = gra_choice.gra_choice_wrong_answer(gra_choice_answers, j)
                home_work.gra_choice_choose_answer(current_right_answer)
                home_work.click_gra_choice_choose_sure()
                home_work.click_gra_choice_words_list_button()
                home_work.click_words_list_finish()
                home_work.click_back_btn()
            else:
                current_right_answer = gra_choice.gra_choice_right_answer(gra_choice_answers, j)
                current_wrong_answer = gra_choice.gra_choice_wrong_answer(gra_choice_answers, j)
                home_work.gra_choice_choose_answer(current_right_answer)
                home_work.click_gra_choice_choose_sure()
                home_work.click_gra_choice_next_button()