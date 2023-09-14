"""
//coded by Bai to smooth out his internship. 
"""

import pyautogui
import json
import time
from windows_toasts import Toast, WindowsToaster
import pyperclip
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException

"""
1. start Auto LoomJira (notify creator that autoloom is starting)
2. ss for first time (open ss on a new tab)
3. grab that url tab
4. store in a json file as variable :after
5. last 10 seconds before times out ss again
6. swap variables :after = :before
7. grab the url again
8. store the url in a json file as new :after


basically 

after = url 1
before = null

when step 6:
after = url 1
before = url 1*

step 7:
after = url 2*
before = url 1

"""

#JIRA INIT // wanna use selenium because i need to check wether a tab is already opened or not using driver.window_handles
jira_url = "https://autoautoauto.atlassian.net/jira/software/projects/KAN/boards/1?selectedIssue=KAN-1"


chrome_options = webdriver.ChromeOptions()
chrome_options.debugger_address = "127.0.0.1:9222"
driver = webdriver.Chrome(options=chrome_options)
window_handles = [] #tab list

#initiliaze variables
# 720 for 12 minutes
how_many_min = 0.3
time_out = 5
loop_interval = how_many_min * 60
total_iteration = 0
mouse_x=665 
mouse_y=158

comment_data = {
    "The link I am working at:": "https://automattor.com/automattor-new-clone-2/",
    "Link of the source:": "https://yezza.com/en/clinic-appointment",
    "The issue to solve:": "Learning more about CSS and SVG animations",
    "Before:": None,
    "After:": None,
    "Issues encountered:": "No issue",
    "If successful:": "-"
}

def clear_text_field():
    """Clear the text of a focused input field using pyautogui."""
    pyautogui.hotkey('ctrl', 'a')  # Select all text
    pyautogui.press('delete')      # Delete selected text



#start loom
toaster = WindowsToaster('AutoLoomJira')
newToast = Toast()
newToast.text_fields = [f'AutoLoomJira is starting.\nTimer is set to {how_many_min} minutes.\n\nCODEDBAI']
toaster.show_toast(newToast)
print("AutoLoomJira Booting...")

while True:
    
    # Countdown timer ------------------------------------
    for remaining in range(int(loop_interval), 0, -1):
        # Show the 10 seconds toast
        if remaining == time_out:
            toaster = WindowsToaster('AutoLoomJira')
            newToast = Toast()
            newToast.text_fields = [f'{time_out} seconds left. Please don\'t touch your keyboard.']
            newToast.on_activated = lambda _: print('Toast clicked!')
            toaster.show_toast(newToast)

        minutes, seconds = divmod(remaining, 60)
        print(f"Time left before next AutoLoomJira simulation: {minutes:02d}:{seconds:02d}", end='\r')
        time.sleep(1)
    # Countdown timer ------------------------------------

    # take screen shot
    toaster = WindowsToaster('AutoLoomJira')
    newToast = Toast()
    newToast.text_fields = ['Time\'s up. Screenshotting now. Please don\'t touch your keyboard.']
    toaster.show_toast(newToast)

    # Screenshot code ------------------------------------

    # Delay 
    time.sleep(2)

    # Simulate holding down the keys Ctrl + Shift + 1

    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('shift')
    pyautogui.press('1')

    # Delay 
    time.sleep(2)

    # Release keys
    pyautogui.keyUp('ctrl')
    pyautogui.keyUp('shift')

    # copy url
    time.sleep(2)
    pyautogui.hotkey('ctrl', 'l')
    time.sleep(0.5)
    pyautogui.hotkey('ctrl', 'c')
    new_loom_url = pyperclip.paste()

    # close tab
    time.sleep(2)
    pyautogui.hotkey('ctrl','w')

    #json stuff
    comment_data["Before:"] = comment_data["After:"]
    comment_data["After:"] = new_loom_url

    with open("comment_data.json", "w") as json_file:
        json.dump(comment_data, json_file, indent=4)

    #debug copied loom url 
    total_iteration = total_iteration + 1
    print("New loom screenshoot url: " + str(new_loom_url))

    # Screenshot code ------------------------------------

    toaster = WindowsToaster('AutoLoomJira')
    newToast = Toast()
    newToast.text_fields = [f"Screenshot done. Switching to JIRA"]
    toaster.show_toast(newToast)
    jira_tab_exists = True
    print(f"SS Done.")
    time.sleep(2)
    # JIRA code ------------------------------------------

    # Iterate through the window handles
    window_handles = driver.window_handles

    for handle in window_handles:
        # Switch to the tab/window with the given handle
        driver.switch_to.window(handle)
        
        # Get the URL of the currently focused tab
        current_url = driver.current_url
        jira_tab_exists = False
        
        # Compare the URLs
        if jira_url in current_url:
            
            toaster = WindowsToaster('AutoLoomJira')
            newToast = Toast()
            newToast.text_fields = [f"JIRA is already opened. Switching to the existing JIRA Tab"]
            toaster.show_toast(newToast)
            jira_tab_exists = True
            print(f"JIRA is already opened.")
            break #get out of the loop and stop at existing jira tab

    else:
        print(f"JIRA is not opened. Opening JIRA on a new tab.")
        toaster = WindowsToaster('AutoLoomJira')
        newToast = Toast()
        newToast.text_fields = [f"JIRA is not opened. Opening JIRA on new tab"]
        toaster.show_toast(newToast)
        pyautogui.hotkey('ctrl','t') #open new tab
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[-1]) #last tab in the list 
        driver.get(jira_url)
        time.sleep(2)  #delay to wait to be opened
    #LOOP END


    action = ActionChains(driver)
    try:
        comment_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//input[@data-testid="chrome-collapsed"]')))
        
    except TimeoutException:
        print("Comment box is already opened. Looking for save_button")
        save_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[@data-testid="comment-save-button"]')))
        clear_text_field()

    def save_comment_data():
        with open("comment_data.json", "r") as json_file:
            comment_data = json.load(json_file)

        formatted_comment = ""
        for field_name, field_value in comment_data.items():
            if field_value is not None:
                formatted_comment += f"{field_name} {field_value if field_value is not None else ''}\n"
        return formatted_comment


    pyautogui.click(mouse_x,mouse_y) #need to switch focus from chrome url to the jira gui
    #action.move_to_element(comment_input).click().perform()
    

    formatted_data = save_comment_data()  # Call the function to get its return value
    pyperclip.copy(formatted_data)        # Copy the returned string to the clipboard

    pyautogui.press('m') #m basically delete saved comment so no need to use def clear, save time 
    time.sleep(0.5)
    pyautogui.hotkey('ctrl','v')
    print("Comment pasted into comment box.")
    
    time.sleep(1)
    try:
        save_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[@data-testid="comment-save-button"]')))
        action.move_to_element(save_button).click().perform()
        print("COMMENT SUCCESSFULLY SAVED!")

        #new toast
        toaster = WindowsToaster('AutoLoomJira')
        newToast = Toast()
        newToast.text_fields = [f"Comment successfully saved. Keep working Bai!"]
        toaster.show_toast(newToast)
    except TimeoutException:
        print("save button problem")

    # JIRA code ------------------------------------------  


