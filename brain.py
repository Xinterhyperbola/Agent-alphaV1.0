from ast import keyword
import re
from tool.cal import add, mutiply, power
import pickle

try:
    with open('brain_model.pkl', 'rb') as f:
        ai = pickle.load(f)
except FileNotFoundError:
    ai = None


def thinking(input):
    text = input.lower()
    numbers = [float(n) for n in re.findall(r'\d+(?:.\d+)?', text)]

    if any(keyword in text for keyword in ['บวก', 'รวม', '+', 'add']):
        return 'add', numbers

    elif any(keyword in text for keyword in ['คูณ', '*', 'x', 'multiply']):
        return 'multiply', numbers

    elif any(keyword in text for keyword in ['กำลัง', 'ยกกำลัง', '^', 'power', '**']):
        return 'power', numbers

    elif any(keyword in text for keyword in ['break', 'stop', 'หยุด']):
        return 'stop', ''

    elif any(keyword in text for keyword in ['เปิดโน้ต', 'โน็ต', 'note']):
        return 'notepad', ''

    else:
        return 'unknow', numbers