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


def do_auto_search(search_bar_x, search_bar_y):
    pyautogui.moveTo(search_bar_x, search_bar_y, duration=0.2)
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

num_of_search = 20

exit_monitor = threading.Thread(target=exit_monitor)
exit_monitor.start()

for _ in tqdm(range(num_of_search), colour='green'):
    if stop:
        break
    do_auto_search(-2200, 20)  # 搜索栏坐标

print(colored("Search done.", 'blue'))
