from speech_recognition import (
    Recognizer,
    Microphone,
    WaitTimeoutError,
    UnknownValueError,
    RequestError,
)


def listener():
    return Recognizer(), Microphone()


def cal_noise(r, source, sec=0.5):
    """ เรียกใช้งาน adjust_for_ambient_noise ผ่าน Object r """
    r.adjust_for_ambient_noise(source, duration=sec)


def listen_command(r, source, prompt_func=None, prompt_text=""):
    if prompt_text and prompt_func:
        prompt_func(prompt_text, speed=0.05)

    while True:
        try:
            if prompt_func:
                prompt_func("\n[กำลังฟัง...]: ", speed=0.01)
            else:
                print("\n[กำลังฟัง...]: ", end='', flush=True)

            audio = r.listen(source, timeout=5, phrase_time_limit=10)
            text = r.recognize_google(audio, language="th-TH")
            print(f"ได้ยินว่า: {text}")
            return text

        except WaitTimeoutError:
            msg = "\nไม่ได้ยินเสียง ลองพูดใหม่อีกครั้ง..."
            if prompt_func:
                prompt_func(msg, speed=0.02)
            else:
                print(msg)

        except UnknownValueError:
            msg = "\nฟังไม่ชัดเจน กรุณาพูดอีกครั้ง..."
            if prompt_func:
                prompt_func(msg, speed=0.02)
            else:
                print(msg)

        except RequestError as e:
            print(f"\nเกิดข้อผิดพลาดในการเชื่อมต่อ: {e}")
            return ""
