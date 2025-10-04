# Shade Tools


Two small input-automation utilities for **testing, accessibility, and education**.


- **Shade Auto Clicker** — auto-clicks wherever the mouse cursor is.
- **Shade Spammer** — types randomized words in a paragraph-style stream.


**Author / handle:** `[Vexor] Chicken`


---


## IMPORTANT DISCLAIMER


These tools are provided for benign purposes only (UI testing, accessibility, automation experiments). **Do not** use them to cheat in online or multiplayer games, to bypass anti-cheat systems, or to violate any software's Terms of Service. The author and contributors are not responsible for misuse.


---


## Features


- Toggle on/off with `F8`. Quit with `Esc`.
- `--only-when-focused` option: operate only when a given window (or the active window) is focused.
- `--test` mode prints simulated actions instead of sending real input (useful for CI or verification).
- Adjustable delays and jitter for speed tuning.


---


## Requirements


- Python 3.8+
- `pip install pynput pygetwindow` (optional: `pygetwindow` required for `--only-when-focused` support on many platforms)


---


## Quick usage examples


Auto clicker (click wherever mouse is):


```bash
python autoclicker/shade_autoclicker.py --delay 0.005
