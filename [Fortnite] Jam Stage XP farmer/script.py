from keyboard import is_pressed
from os import system
from pyautogui import keyDown, keyUp
from random import randint
from time import sleep, time



# 「;」を押してスクリプトを停止します。Fortniteの「esc」メニューが表示されると、スクリプトが停止したことがわかります。
# Hold ';' to stop the script. You will kknow the script has stopped when the 'esc' menu in Fornite opens up.

# duration = (時間 * 60 * 60) + 分 * 60) + 秒
# 3:30:00が最大XPを得るための最適な時間であることがわかりました
# duration = (hour(s) * 60 * 60) + (minute(s) * 60) + second(s)
# 3:40:00 is the optimal time to gain the maximum XP
duration = (2 * 60 * 60) + (30 * 60) + 0
span_duration = (0 * 60 * 60) + (6 * 60) + 0
start_time = time()



def emote(total_duration, iteration_duration, consumable):
    
    system('cls')
    print("著者: 列星氷刃\nスクリプト: [Fortnite] Jam Stage XP farmer\n\n\n")
    print(f"時間がかかりました: {int(((total_duration) // 60) // 60)}時間 {int(((total_duration) // 60) % 60)}分 {int((total_duration) % 60)}秒")
    print(f"消費する時間: {int(((duration - (total_duration)) // 60) // 60)}時間 {int(((duration - (total_duration)) // 60) % 60)}分 {int((duration - (total_duration)) % 60)}秒")
    print(f"最後の切り替えからの時間: {(iteration_duration // 60) % 60}分 (または {iteration_duration}秒) | {consumable}\n\n")
    print(f"Time consumed: {int(((total_duration) // 60) // 60)}時間 {int(((total_duration) // 60) % 60)}分 {int((total_duration) % 60)}秒")
    print(f"Time yet to consume: {int(((duration - (total_duration)) // 60) // 60)}時間 {int(((duration - (total_duration)) // 60) % 60)}分 {int((duration - (total_duration)) % 60)}秒")
    print(f"Time since last switch: {(iteration_duration // 60) % 60}分 (または {iteration_duration}秒) | {consumable}")
    
    if is_pressed(';'):
        return
    
    if iteration_duration >= consumable:
        if total_duration >= duration:
            return
        iteration_duration = 0
        sleep_duration = randint(10, 20)
        iteration_duration += sleep_duration
        total_duration += sleep_duration
        keyDown('b')
        sleep(0.2)
        keyDown('space')
        sleep(0.2)
        keyUp('space')
        sleep(0.2)
        keyUp('b')
        sleep(sleep_duration)
        emote(total_duration, iteration_duration, consumable)
    else:
        if total_duration >= duration:
            return
        sleep_duration = randint(10, 20)
        iteration_duration += sleep_duration
        total_duration += sleep_duration
        keyDown('b')
        sleep(0.2)
        keyUp('b')
        sleep(sleep_duration)
        emote(total_duration, iteration_duration, consumable)



sleep(5)
emote(0, 0, span_duration)
keyDown('esc')
sleep(0.2)
keyUp('esc')