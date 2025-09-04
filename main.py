#!/usr/bin/env python3
import time
import threading

import pyautogui
from pynput import keyboard

# ----- CONFIG -----
CLICK_POS = (855, 724)            # where to click
CHECK_POS = (297, 332)            # pixel to check
TARGET_RGB = (30, 40, 55)       # target color
INTERVAL_SECONDS = 0.5            # main interval
# ------------------

pyautogui.FAILSAFE = True  # move mouse to top-left corner to stop

stop_event = threading.Event()

def on_press(key):
    """Kill-switch: press '5' to stop."""
    try:
        if getattr(key, "char", None) == "5":
            stop_event.set()
            return False  # closes the listener
    except Exception:
        pass

def get_pixel_rgb(pos):
    """Fast pixel reading at (x, y)."""
    x, y = pos
    try:
        r, g, b = pyautogui.pixel(x, y)
        return (r, g, b)
    except Exception:
        # fallback via screenshot (slower but more robust on some configurations)
        im = pyautogui.screenshot()
        return im.getpixel((x, y))

def main():
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    try:
        while not stop_event.is_set():
            # First click at defined interval
            pyautogui.click(*CLICK_POS)
            time.sleep(0.05)  # small delay to stabilize the frame

            # Pixel check
            color = get_pixel_rgb(CHECK_POS)

            if color == TARGET_RGB:
                # If the color is correct, click again immediately
                pyautogui.click(*CLICK_POS)
                # wait until next cycle
                slept = 0.0
                # fractional wait so kill-switch is responsive
                while slept < INTERVAL_SECONDS and not stop_event.is_set():
                    time.sleep(0.05)
                    slept += 0.05
            else:
                print(f"Pixel different from target: {color} != {TARGET_RGB}. Stop.")
                pyautogui.click(*CHECK_POS)
                break
    finally:
        try:
            listener.stop()
        except Exception:
            pass

if __name__ == "__main__":
    print("Starting. Press '5' to stop. (Failsafe: move mouse to top-left corner)")
    main()
    print("Terminated.")

