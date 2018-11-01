from time import sleep
from testcase.page.learn_center.all_class import AllPage
from testcase.page.study_center.study_center_main_page import StudyCenter
from testcase.interface.all_interface import AllInterface


class HomeWork(AllInterface, StudyCenter, AllPage):
    pass


def sen_fill(home_work, headers, k0, k1, click_result):
    sen_fill = HomeWork()
    all_answers = sen_fill.get_all_sen_fill_answer(headers, k0, k1)
    sleep(10)
    if int(click_result) == 2:
        home_work.click_finish_button()
        home_work.click_back_btn()
    else:
        curr, total = home_work.get_senfill_lists_nums()
        for j in range(int(curr), int(total) + 1):
            if j == int(total):
                # home_work.save_screen_shot(page_name="Word_Trans", file_name="播放截图")
                current_right_answer = sen_fill.sen_fill_right_answer(all_answers, j)
                current_wrong_answer = sen_fill.sen_fill_wrong_answer(all_answers, j)
                # try:
                #     login_page.hideKeyboard()
                # except:
                #     login_page.save_screen_shot("No KEYBoard")
                home_work.senfill_fill_answer(current_right_answer)
                # home_work.save_screen_shot("题目判定页")
                home_work.click_sen_fill_words_list_btn()
                home_work.click_words_list_finish()
                home_work.click_back_btn()
            # login_page.click_audio_button()
            else:
                # home_work.save_screen_shot(page_name="Word", file_name="播放截图")
                current_right_answer = sen_fill.sen_fill_right_answer(all_answers, j)
                current_wrong_answer = sen_fill.sen_fill_wrong_answer(all_answers, j)
                # try:
                #     home_work.hideKeyboard()
                # except:
                #     pass
                # home_work.save_screen_shot("No KEYBoard")
                home_work.senfill_fill_answer(current_right_answer)
                # home_work.save_screen_shot("题目判定页")
                home_work.click_sen_fill_next_btn()