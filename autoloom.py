import pyautogui
import time

from windows_toasts import Toast, WindowsToaster

# 720 for 12 minutes

how_many_min = 12
loop_interval = how_many_min * 60
total_iteration = 0

toaster = WindowsToaster('Auto Loom')
newToast = Toast()
# newToast.text_fields = ['"Auto Loom is starting.\nTimer is set to {how_many}"'].format(how_many_min)
newToast.text_fields = [f'Auto Loom is starting.\nTimer is set to {how_many_min} minutes.\nCODEDBAI']
toaster.show_toast(newToast)

while True:
    # Delay 
    time.sleep(2)

    # Simulate holding down the keys Ctrl + Shift + 1
    print("-loom simulation starting-")
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('shift')
    pyautogui.press('1')

    # Delay 
    time.sleep(2)

    # Release keys
    pyautogui.keyUp('ctrl')
    pyautogui.keyUp('shift')

    total_iteration = total_iteration + 1
    print("Screenshot done. Total iteration: " + str(total_iteration))

    # Countdown timer
    for remaining in range(int(loop_interval), 0, -1):
        # Show the 10 seconds toast
        if remaining == 10:
            toaster = WindowsToaster('Auto Loom')
            newToast = Toast()
            newToast.text_fields = ['10 seconds left. Please don\'t touch your keyboard.']
            newToast.on_activated = lambda _: print('Toast clicked!')
            toaster.show_toast(newToast)

        minutes, seconds = divmod(remaining, 60)
        print(f"Time left before next loom simulation: {minutes:02d}:{seconds:02d}", end='\r')
        time.sleep(1)

    # Show the "Time's up" toast before taking a screenshot
    toaster = WindowsToaster('Auto Loom')
    newToast = Toast()
    newToast.text_fields = ['Time\'s up. Screenshotting now. Please don\'t touch your keyboard.']
    newToast.on_activated = lambda _: print('Toast clicked!')
    toaster.show_toast(newToast)
