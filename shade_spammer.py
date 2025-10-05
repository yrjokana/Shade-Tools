#!/usr/bin/env python3
# optional window focus check
try:
import pygetwindow as gw
HAS_PYGETWINDOW = True
except Exception:
HAS_PYGETWINDOW = False


kb = KController()
running = False
stop_flag = False

#Lol, Trash Words *Giggles cutely*
DEFAULT_WORDS = [
"pog ", "ez ", "hello ", "spam ", "A ", "kekw ", "bruh ", "yeet ", "lol ",
"SUBSCRIBE ", "Avocado ", "Cheesus ", "Dan Dingle dingles my dingle ",
"Team Vexor ", "Vexor Chicken ", "[Vexor] Chicken ", "Cheese ", "Flint & Steel ",
"I.. am Steven ", "#Spam ", "Blorp ", "Zindle ", "womp ", "womp womp ", "ChatGPT gave me half of these words ",
"LowQualityCoding said Lol, Nice Words ", "That's crazy ", "Flint & Cheese ", "#SheWas18InDogYears ",
"Diciotto anni in anni canini sono da ottantotto a centodieci ", "#69 ", "#35 ", "#NotHighQualityCoding ",
"#Grr ", "#RunningOutOfWords ", "Whap ", "Snizzle ", "Cronk ", "Glorp ", "Squish ", "Blabble ", "It's Almost Christmas ", "Shade "
]




def parse_args():
p = argparse.ArgumentParser(description='Shade Spammer')
p.add_argument('--char-delay', type=float, default=0.001, help='seconds between characters')
p.add_argument('--word-delay', type=float, default=0.002, help='seconds between words')
p.add_argument('--jitter', type=float, default=0.0, help='max jitter on char delay')
p.add_argument('--only-when-focused', type=str, default=None, help='window title substring required to be active')
p.add_argument('--test', action='store_true', help='test mode: print instead of typing')
p.add_argument('--words-file', type=str, default=None, help='optional path to a newline-separated word file')
return p.parse_args()




def is_focused(target_substr):
if not target_substr:
return True
if not HAS_PYGETWINDOW:
return False
try:
win = gw.getActiveWindow()
if not win:
return False
return target_substr.lower() in win.title.lower()
except Exception:
return False




def load_words(path):
if not path:
return DEFAULT_WORDS
try:
with open(path, 'r', encoding='utf-8') as f:
lines = [ln.rstrip('\n') for ln in f if ln.strip()]
# ensure each word ends with a trailing space so result is paragraph-like
return [ln + (' ' if not ln.endswith(' ') else '') for ln in lines]
except Exception:
print('Failed to load words file; falling back to defaults')
return DEFAULT_WORDS




def spam_loop(char_delay, word_delay, jitter, focus_substr, test_mode, words):
global stop_flag
while not stop_flag:
if running:
if not is_focused(focus_substr):
time.sleep(0.01)
continue
w = random.choice(words)
for ch in w:
