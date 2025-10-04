#!/usr/bin/env python3
HAS_PYGETWINDOW = True
except Exception:
HAS_PYGETWINDOW = False


mouse = MouseController()
running = False
stop_flag = False




def parse_args():
p = argparse.ArgumentParser(description="Shade Auto Clicker")
p.add_argument('--delay', type=float, default=0.005, help='base seconds between clicks')
p.add_argument('--jitter', type=float, default=0.0, help='max random jitter added to base delay')
p.add_argument('--only-when-focused', type=str, default=None, help='window title substring required to be active')
p.add_argument('--test', action='store_true', help='test mode: do not send real input')
return p.parse_args()




def is_focused(target_substr):
if not target_substr:
return True
if not HAS_PYGETWINDOW:
# if user requested focus-only but pygetwindow isn't installed, behave conservatively (return False)
return False
try:
win = gw.getActiveWindow()
if not win:
return False
return target_substr.lower() in win.title.lower()
except Exception:
return False




def auto_click_loop(delay_base, jitter, focus_substr, test_mode):
global stop_flag
while not stop_flag:
if running:
if not is_focused(focus_substr):
time.sleep(0.01)
continue
if test_mode:
print('[TEST] click at', mouse.position)
else:
mouse.click(Button.left)
# compute next delay
j = random.uniform(-jitter, jitter) if jitter and jitter > 0 else 0.0
next_delay = max(0.0, delay_base + j)
# check stop frequently
for _ in range(max(1, int(next_delay / 0.005))):
if stop_flag:
return
time.sleep(0.005)
else:
time.sleep(0.05)




def on_press(key):
global running, stop_flag
try:
if key == Key.f8:
running = not running
print('Running:', running)
elif key == Key.esc:
stop_flag = True
print('Exiting...')
return False
except Exception:
pass




if __name__ == '__main__':
args = parse_args()
print('Shade Auto Clicker — by [Vexor] Chicken')
print('Toggle with F8, quit with Esc')
print('Args:', args)


loop_thread = threading.Thread(target=auto_click_loop, args=(args.delay, args.jitter, args.only_when_focused if False else args.__dict__.get('only_when_focused'), args.test), daemon=True)
loop_thread.start()


with Listener(on_press=on_press) as listener:
listener.join()


# give threads a moment (daemon threads will exit on program exit)
time.sleep(0.05)
print('Program exited cleanly.')
