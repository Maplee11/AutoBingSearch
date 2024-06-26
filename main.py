import pyautogui
import time
import random
import string
from tqdm import tqdm
from termcolor import colored
import threading
import keyboard


def exit_monitor():
    global stop
    keyboard.wait('q')
    stop = 1


def show_cur_mouse_coordinate():
    pre_mouse_x, pre_mouse_y = pyautogui.position()
    while True:
        current_mouse_x, current_mouse_y = pyautogui.position()
        if current_mouse_x != pre_mouse_x or current_mouse_y != pre_mouse_y:
            pre_mouse_x = current_mouse_x
            pre_mouse_y = current_mouse_y
            print(f"\r当前鼠标坐标：({current_mouse_x}, {current_mouse_y})", end="")


def do_auto_search(_search_bar_x, _search_bar_y):
    pyautogui.moveTo(_search_bar_x, _search_bar_y)
    pyautogui.click()
    characters = string.ascii_letters + string.digits
    length = 6
    query = ''.join(random.choices(characters, k=length))
    pyautogui.typewrite(query+'\n', interval=0.1)
    pyautogui.press('enter')


# 监控鼠标指针坐标
# mouse_coordinate_monitor = threading.Thread(target=show_cur_mouse_coordinate)
# mouse_coordinate_monitor.start()

stop = 0
exit_monitor = threading.Thread(target=exit_monitor)
exit_monitor.start()

# 搜索次数
num_of_search = 30

# 搜索栏坐标
search_bar_x = -2200
search_bar_y = 20

for _ in tqdm(range(num_of_search), colour='green'):
    if stop:
        break
    do_auto_search(search_bar_x, search_bar_y)
    time.sleep(5)

print(colored("Search done.", 'blue'))
