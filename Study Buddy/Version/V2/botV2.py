#add error handling ✅
#add data expansion ✅
#add gamification 
import json
import numbers
import os
import time
import winsound
from datetime import date, timedelta

notes = [
    (261, 150), 
    (329, 150),  
    (392, 150),  
    (523, 350)  
]

default_data = {
    "tasks": [],
        "user": {
            "level": 1,
            "exp": 0,
            "streak": 0,
            "last_study_date": ""
        },
        "stats": {
            "total_pomodoros": 0,
            "total_focus_minutes": 0
        }
}

def load_data():
    if not os.path.exists('todo.json'):
        return default_data.copy()      # ใช้ default_data
    
    with open('todo.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    if "user" not in data:
        data["user"] = default_data["user"].copy()
    if "stats" not in data:
        data["stats"] = default_data["stats"].copy()
    
    return data
def save_data():
    with open('todo.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
data = load_data()
tasks = data["tasks"]

def add_task():
    
    task = input("ใส่งานมาเลย").strip()
    
    if not task:
        print('ลืมพิมอะเปล่าO^O')
        return
    else:
        tasks.append(task)
        print(f'จด{task}ไว้แล้ว!!')
        save_data()

def remove_task():
    show_task()
    task = input("งานไหนเสร็จแล้ว(ให้กดเลขงานเพื่อลบ)")
    
    if not task:
        print('ลืมพิมอะเปล่าO^O')
        return
    try:
        num = int(task)
        remove = tasks.pop(num-1)
        save_data()
        print(f'ลบ{remove}เรียบร้อยครับ')
    except ValueError:
        print('ใส่แค่เลขนะครับ')
    except IndexError:
        print('ไม่มีอยู่ในตัวเลือก')
def show_task():
    if not tasks:
        print('เก่งมากไม่มีงานเลยอยากเพิ่มไหม^^')
    else:
        try:
            for i,v in enumerate(tasks,1):
                print(f'{i}.{v}')
        except ValueError:
            print('ป้อนแค่')
def countdown (sec, text):
    for x in range(sec, 0 , -1):
        h = x// 3600
        min = (x%3600)//60
        secon =  x%60
        if x >= 3600:
            print(f'เวลากำลังเดินนะสู้ๆ {h:02d}:{min:02d}:{secon:02d}',end="\r")
        else:
            print(f'เวลากำลังเดินนะสู้ๆ {min:02d}:{secon:02d}',end="\r")
        time.sleep(1)
    print(f'\n{text}')
#ตัวถามหา เลข เมื่อไม่ให้มา 
max_min = 180
mini_min = 1
def ask_check(num, default):
    while True: 
        text = input(num).strip()
        if not text: 
            return default
        try:
            number = abs(round(float(text)))
            if number > max_min:
                print('จะเรียนไรเยอะขนาดนั้น 3ชมก็เต็มกลืนแล้วลูก')
                return max_min
            elif number < mini_min:
                print('เอิ่มแค่หายใจก็หมดแล้วมั้ง...')
                return mini_min
            
            return number
        except ValueError:
            print('ช่วยใส่ตัวเลขด้วยนะครับ')
def play_alarm():
    for freq, duration in notes:
        winsound.Beep(freq, duration)
        time.sleep(0.05)
def startpomodoro ():
    today = date.today()
    print('งั้นเรามา เริ่มการ โฟกัสกับการอ่านหนังสือกันเลย ^^')
    print('แต่ก่อนอื่นขอทราบเวลาอ่านกับพักได้ไหมหื้ม^^')
    focus = ask_check('ใส่เวลาเลย(นาที):',25)
    break_ = ask_check('ใส่เวลาเลย(นาที):',5)
    
    countdown(int(focus)*60, 'หมดเวลาอ่านแล้วไปพักได้🥳')
    play_alarm()
    data['user']['exp'] += 50
    if  data['user']['last_study_date'] == '':
        data['user']['streak'] = 1
    elif data['user']['last_study_date'] == str(today):
        pass
    else:
        last = date.fromisoformat(data['user']['last_study_date'])
        diff = (today-last).days
        if diff == 1:
            data['user']['streak'] +=1
        else:
            data['user']['streak'] =1
    data["user"]["last_study_date"] = str(today)
    data['stats']['total_pomodoros'] += 1
    data["stats"]["total_focus_minutes"] += focus
    print(f'🔥 Streak: {data["user"]["streak"]} วัน')
    while data['user']['exp'] >= 100:
        data['user']['level'] += 1
        data['user']['exp'] -= 100
        print(f'🎉 Level Up! → Level {data["user"]["level"]}')
    print(f'| Lv.{data["user"]["level"]} | EXP {data["user"]["exp"]}/100|')
    save_data()
    countdown(int(break_)*60, 'หมดเวลาพักแล้ว📚')
    play_alarm()
def show_status():
    u = data['user']
    print(f'📚 Study Buddy | Lv.{u["level"]} | '
              f'EXP {u["exp"]}/100 | 🔥 {u["streak"]}')
print('สวัสดี ยินดีต้อนรับสู่ menu')
try:
    
    while True:
        try:
            show_status()
            print('กดเลข 1 ใส่งาน | 2 ลบงาน | 3 โชว์งาน | 4 เริ่มPomodoro | 5 ออก')
            shose = input('เลือกตัวเลือกเลย:')
            sh = int(shose)
            if sh == 1:
                add_task()
            elif sh == 2:
                remove_task()
            elif sh == 3:
                show_task()
            elif sh == 4:
                startpomodoro()
            elif sh == 5:
                break
            else:
                print('ไม่มีตัวเลือกที่เลือกมา')
        except ValueError:
            print('เขียนมาแค่เลขนะครับ')
except KeyboardInterrupt:
    print('\rโห้วกด ctrl+c เลยหรอ ผมอุตส่าห์ ทำตัวเลือกออกให้T^T')
