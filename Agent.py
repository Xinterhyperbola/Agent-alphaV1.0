import time
import re
import requests
from tool.cal import add, mutiply, power
import speech_recognition as sr
import os
from brain import thinking
import subprocess
from tool.listen import listener, cal_noise, listen_command

well = 'hi what i can help u to day? ^^'


# ----------- zoon function ----------- #
def typeing(input, speed=0.01, wait=0.15):
    text = str(input)
    for i in text:
        print(i, end='', flush=True)
        time.sleep(speed)
    time.sleep(wait)
    for _ in range(len(text)):
        print('\b \b', end='', flush=True)
        time.sleep(speed)
    return ''


def types(n, speed=0.01):
    text = str(n)
    for i in text:
        print(i, end='', flush=True)
        time.sleep(speed)
    return ''


r = sr.Recognizer()
adjust_noise = r.adjust_for_ambient_noise


def get_input(use_voice, source=None, prompt_text=" "):
    """ ฟังก์ชันรับข้อมูล: สลับระหว่างพิมพ์กับพูดตามค่า use_voice """
    if not use_voice:
        # ถ้าปิดโหมดเสียง -> ใช้การพิมพ์ปกติ
        return input(types(prompt_text, speed=0.05))
    else:
        # ถ้าเปิดโหมดเสียง -> ฟังจากไมค์
        if prompt_text:
            types(prompt_text, speed=0.05)

        while True:
            try:
                types("\n[กำลังฟัง...]:  ", speed=0.01)
                audio = r.listen(source, timeout=5, phrase_time_limit=10)
                text = r.recognize_google(audio, language="th-TH")
                print(f"ได้ยินว่า: {text}")
                return text

            except sr.WaitTimeoutError:
                types("\nไม่ได้ยินเสียง ลองพูดใหม่อีกครั้ง... ", speed=0.02)

            except sr.UnknownValueError:
                types("\nฟังไม่ชัดเจน กรุณาพูดอีกครั้ง... ", speed=0.02)

            except sr.RequestError as e:
                print(f"\nเกิดข้อผิดพลาดในการเชื่อมต่อ: {e}")
                return " "


# ----------- zoon function ----------- #
typeing(well, speed=0.02)

start = True
voice_mode = False

with sr.Microphone() as source:
    while start:
        try:
            mode_label = "[Voice] " if voice_mode else "[Text] "
            a = get_input(voice_mode, source, prompt_text=f"\n{mode_label} command:  ")

            if not a:
                continue

            if a.strip().lower() in ['open voice', 'เสียง', 'voicemode', 'พูด']:
                voice_mode = True
                types("\n[system]: กำลังเปลี่ยนโหมดให้นะครับ^^ ")
                adjust_noise(source, duration=0.5)
                time.sleep(0.125)
                types("\n[system]: เปลี่ยนโหมดเรียบร้อย ")
                continue

            elif a.strip().lower() in ['close voice', 'ปิดเสียง', 'disable voice']:
                voice_mode = False
                types("\n[ระบบ]: ปิดโหมดเสียง เปลี่ยนเป็นพิมพ์ตามปกติแล้ว!\n")
                continue

            res, numbers = thinking(a)

            if res == 'add':
                types("I think i should add number\n")

                while len(numbers) < 2:
                    prompt = (
                        "กรอกมาแค่ 1 อันเอง ช่วยใส่เพิ่มอีกอันนะครับ: "
                        if len(numbers) == 1
                        else "ขอเลขอย่างน้อย 2 ตัวนะครับ: "
                    )
                    more = get_input(voice_mode, source, prompt_text=prompt)
                    morenumber = [float(n) for n in re.findall(r'\d+(?:.\d+)?', more)]
                    numbers.extend(morenumber)

                result = add(numbers[0], numbers[1])
                types(f'ผลลัพธ์: {result}\n')

            elif res == 'multiply':
                types("I think i should multiply number\n")

                while len(numbers) < 2:
                    prompt = (
                        "กรอกมาแค่ 1 อันเอง ช่วยใส่เพิ่มอีกอันนะครับ:"
                        if len(numbers) == 1
                        else "ขอเลขอย่างน้อย 2 ตัวนะครับ:"
                    )
                    more = get_input(voice_mode, source, prompt_text=prompt)
                    morenumber = [float(n) for n in re.findall(r'\d+(?:\.\d+)?', more)]
                    numbers.extend(morenumber)

                result = mutiply(numbers[0], numbers[1])
                types(f'ผลลัพธ์: {result}\n')

            elif res == 'power':
                types("I think i should power number\n")

                while len(numbers) < 2:
                    prompt = (
                        "กรอกมาแค่ 1 อันเอง ช่วยใส่เพิ่มอีกอันนะครับ:"
                        if len(numbers) == 1
                        else "ขอเลขอย่างน้อย 2 ตัวนะครับ:"
                    )
                    more = get_input(voice_mode, source, prompt_text=prompt)
                    morenumber = [float(n) for n in re.findall(r'\d+(?:\.\d+)?', more)]
                    numbers.extend(morenumber)

                result = power(numbers[0], numbers[1])
                types(f'ผลลัพธ์: {result}\n')

            elif res == 'notepad':
                os.system('notepad')

            elif res == 'stop':
                types("กำลังปิดการทำงาน...\n")
                break

            else:
                types(f"No match! Brain returned '{res}'\n")

        except KeyboardInterrupt:
            print("\nหยุดการทำงานโดยผู้ใช้")
            break