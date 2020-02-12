from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from pynput.keyboard import Key, Controller
import sys
import time

#selenium
driver = webdriver.Chrome()
url = 'https://beanbeanbean.com/times-tables.html'
driver.get(url)
driver.maximize_window()
action = ActionChains(driver)

def shut_down():
    sys.exit()

def find_answer(question):
    question = question.split()
    question.pop()
    question[1] = '*'
    answer = eval(''.join(question))
    return answer

def submit_answer():
    key_b = Controller()
    # get the text of the question section of the id: QUestion Wrapper
    que = driver.find_element_by_css_selector('div#divQuestionWrapper').text
    # will call the find_answer function and get the answer which will be in string form
    ans = find_answer(que)

    # answer box
    # ans_box = driver.find_element_by_css_selector('p#pAnswerNumber')
    # ans_box.click()
    for i in str(ans):
        key_b.press(i)
        key_b.release(i)
    key_b.press(Key.enter)
    key_b.release(Key.enter)

def change_digit(txt):
    s = ''
    for i in txt:
        if i.isnumeric():
            s += i
    return int(float(s))


if __name__ == '__main__':
    key_b = Controller()
    submit_answer()
    while True:
        curr = driver.find_element_by_css_selector('div.divStat').text
        goal = driver.find_element_by_css_selector('span#spanGoal').text
        curr_bean = change_digit(curr)
        goal_bean = change_digit(goal)
        # submit_answer()
        # print(goal_bean,curr_bean,type(curr_bean), type(goal_bean))

        if curr_bean < 333:
            if curr_bean < goal_bean-2:
                submit_answer()
            else:
                key_b.press(Key.enter)
                key_b.release(Key.enter)
        else:
            time.sleep(1)
            key_b.press(Key.ctrl)
            key_b.press('w')
            key_b.release(Key.ctrl)
            key_b.release('w')
            time.sleep(1)
            sys.exit()