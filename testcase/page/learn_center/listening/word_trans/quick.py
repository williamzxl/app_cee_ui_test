import threading
from time import sleep, ctime
from selenium.webdriver.common.by import By
import os
item_class = (By.CLASS_NAME, "android.widget.TextView")
evaluation_id = (By.ID, 'com.langlib.cee:id/evaluation')
action_id = (By.ID, 'com.langlib.cee:id/evaluation_begin_tv')
a = "com.langlib.cee:id/fragment_word_trans_detail_answer_a"
radio_id = (By.ID, "com.langlib.cee:id/fragment_word_trans_detail_answer_a")
radio_b_id = (By.ID, "com.langlib.cee:id/fragment_word_trans_detail_answer_b")
radio_classes = (By.CLASS_NAME, "android.widget.RadioButton")
edit_id = (By.ID, "com.langlib.cee:id/write_measure_edit")
next_id = (By.ID, "com.langlib.cee:id/senavaly_quest_next_quest")
title_id = (By.ID, "com.langlib.cee:id/title_iframe_title_tv")
web_class = (By.CLASS_NAME, "android.widget.ScrollView")
step_1_id = (By.ID, "com.langlib.cee:id/measure_step_one")


def click_ele(min):
    Flag = True
    while Flag:
        print("Start Time:",ctime())
        for y in [1200, 645, 890, 950,1090,]:
            os.system('adb shell input tap 552 {}'.format(y))
        print("End Time:", ctime())
        # c = ctime().split(" ")[4].split(":")
        # if c[1] == str(min):
        #     print("Click ELE End")
        #     break


def click_next(min):
    Flag = True
    while Flag:
        # print("Start Next Time:", ctime())
        # cmd = 'adb shell input tap 552 1843'
        for y in [1200, 645, 890, 950,1090,]:
            os.system('adb shell input tap 552 {}'.format(y))
            cmd = 'adb shell input tap 746 2471'
            os.system(cmd)
    # print("End Next Time:", ctime())
    #     c = ctime().split(" ")[4].split(":")
    #     if c[1] == str(min):
    #         print("Click next End")
    #         break


def main(min):
    t0 = threading.Thread(target=click_ele, args=(min,))
    t1 = threading.Thread(target=click_next, args=(min,))

    t1.start()
    # t1.join()
    t0.start()
    # t0.join()

    # t0.join()


if __name__ == '__main__':
    # login_page = LoginPage()
    # login_page.open(noReset=True)
    # sleep(15)
    main("50")



    # for i in range(100):
    #     main(login_page)