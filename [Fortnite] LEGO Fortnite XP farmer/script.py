from keyboard import is_pressed
from pyautogui import keyDown, keyUp, mouseDown, mouseUp
from random import choice
from os import system
from time import sleep, time



# 「;」を押してスクリプトを停止します。Fortniteの「esc」メニューが表示されると、スクリプトが停止したことがわかります。
# Hold ';' to stop the script. You will kknow the script has stopped when the 'esc' menu in Fornite opens up.

# スクリプトを実行する前に、適切な量の食品をインベントリに追加し、食品スロットに切り替える必要があります。スクリプトは30分ごとに食品を消費します。
# It is also required that you add the required amount of suitable food to the inventory and switch to the food slot before running the script. The script will consume the food every 30 minutes.

# duration = (時間 * 60 * 60) + 分 * 60) + 秒
# 3:40:00が1日で最大のXPを得るための最適な時間です。
# duration = (hour(s) * 60 * 60) + (minute(s) * 60) + second(s)
# 3:40:00 is the optimal time to gain the maximum XP in a day.
duration = (3 * 60 * 60) + (40 * 60) + 0
start_time = time()

sleep(5)
eat = [0, 0]

while True:
    
    current_time = time()
    if current_time - start_time < duration:
        system('cls')
        print("著者: 列星氷刃\nスクリプト: [Fortnite] LEGO Fortnite XP farmer\n\n\n")
        print(f"時間がかかりました: {int(((current_time - start_time) // 60) // 60)}時間 {int(((current_time - start_time) // 60) % 60)}分 {int((current_time - start_time) % 60)}秒")
        print(f"消費する時間: {int(((duration - (current_time - start_time)) // 60) // 60)}時間 {int(((duration - (current_time - start_time)) // 60) % 60)}分 {int((duration - (current_time - start_time)) % 60)}秒")
        print(f"最後に食事を摂取してからの時間: {(eat[0] // 60) % 60}分 (または {eat[0]}秒) | {eat[1]}\n\n")
        print(f"Time consumed: {int(((current_time - start_time) // 60) // 60)}h {int(((current_time - start_time) // 60) % 60)}m {int((current_time - start_time) % 60)}s")
        print(f"Time yet to consume: {int(((duration - (current_time - start_time)) // 60) // 60)}h {int(((duration - (current_time - start_time)) // 60) % 60)}m {int((duration - (current_time - start_time)) % 60)}s")
        print(f"Time since last consumption of food: {(eat[0] // 60) % 60}m (or {eat[0]}s) | {eat[1]}")
        
        if (eat[0] // 60) % 60 > 30:
            mouseDown()
            sleep(0.5)
            mouseUp()
            mouseDown()
            sleep(0.5)
            mouseUp()
            eat[0] = 0
            eat[1] += 1
            sleep(6)
        
        if is_pressed(';'):
            key_to_press = 'esc'
            break
        
        else:
            key_to_press = choice(['w', 'a', 's', 'd'])
            keyDown(key_to_press)
            # sleep(0.2)
            sleep(3)
            keyUp(key_to_press)
            eat[0] += 3

keyDown(key_to_press)
sleep(0.2)
keyUp(key_to_press)
system('cls')
print("著者: 列星氷刃\nスクリプト: [Fortnite] LEGO Fortnite XP farmer\n\n\n")
print(f"時間がかかりました: {int(((current_time - start_time) // 60) // 60)}時間 {int(((current_time - start_time) // 60) % 60)}分 {int((current_time - start_time) % 60)}秒")
print(f"消費する時間: {int(((duration - (current_time - start_time)) // 60) // 60)}時間 {int(((duration - (current_time - start_time)) // 60) % 60)}分 {int((duration - (current_time - start_time)) % 60)}秒")
print(f"最後に食事を摂取してからの時間: {(eat[0] // 60) % 60}分 (または {eat[0]}秒) | {eat[1]}\n\n")
print(f"Time consumed: {int(((current_time - start_time) // 60) // 60)}h {int(((current_time - start_time) // 60) % 60)}m {int((current_time - start_time) % 60)}s")
print(f"Time yet to consume: {int(((duration - (current_time - start_time)) // 60) // 60)}h {int(((duration - (current_time - start_time)) // 60) % 60)}m {int((duration - (current_time - start_time)) % 60)}s")
print(f"Time since last consumption of food: {(eat[0] // 60) % 60}m (or {eat[0]}s) | {eat[1]}")