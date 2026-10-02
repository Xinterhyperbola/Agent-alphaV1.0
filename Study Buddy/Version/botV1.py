import json
import os
import time
import winsound


notes = [
    (261, 150), 
    (329, 150),  
    (392, 150),  
    (523, 350)  
]


def load_task():
    if os.path.exists('todo.json'):
        with open('todo.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data['tasks']
    else:
        return []
def save_task():
    data = {'tasks': tasks}
    with open('todo.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
tasks = load_task()
def add_task():
    task = input("ใส่งานมาเลย")
    if task =='':
        print('ลืมพิมอะเปล่าO^O')
    else:
        tasks.append(task)
        save_task()
def remove_task():
    task = input("งานไหนเสร็จแล้ว(ให้กดเลขงานเพื่อลบ)")
    if not task:
        print('ลืมพิมอะเปล่าO^O')
    else:
        tasks.pop(int(task)-1)
        save_task()
    print(f"งานเหลือ {tasks}")
def show_task():
    if not tasks:
        print('เก่งมากไม่มีงานเลยอยากเพิ่มไหม^^')
    else:
        for i,v in enumerate(tasks,1):
            print(f'{i}.{v}')
def countdown (sec, text):
    for x in range(sec, 0 , -1):
        min = x//60
        secon =  x%60
        print(f'เวลากำลังเดินนะสู้ๆ {min:02d}:{secon:02d}',end="\r")
        time.sleep(1)
    print(f'\n{text}')
def play_alarm():
    for freq, duration in notes:
        winsound.Beep(freq, duration)
        time.sleep(0.05)
def startpomodoro ():
    print('งั้นเรามา เริ่มการ โฟกัสกับการอ่านหนังสือกันเลย ^^')
    print('แต่ก่อนอื่นขอทราบเวลาอ่านกับพักได้ไหมหื้ม^^')
    focus = input('ใส่เวลาเลย(นาที):')
    break_ = input('ใส่เวลาเลย(นาที):')
    countdown(int(focus)*60, 'หมดเวลาแล้วอ่านแล้วไปพักได้🥳')
    play_alarm()
    countdown(int(break_)*60, 'หมดเวลาพักแล้ว📚')
    play_alarm()
print('สวัสดี ยินดีต้อนรับสู่ task todo')
print('กดเลข 1 ใส่งาน | 2 ลบงาน | 3 โชว์งาน | 4 เริ่มPomodoro | 5 ออก')
while True:
    shose = input('เลือกตัวเลือกเลย:')
    if shose == '1':
        add_task()
    elif shose == '2':
        remove_task()
    elif shose == '3':
        show_task()
    elif shose == '4':
        startpomodoro()
    elif shose == '5':
        break
    else:
        print('ไม่มีตัวเลือกที่เลือกมา')
