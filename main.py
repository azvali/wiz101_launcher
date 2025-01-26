import subprocess
import pyautogui
import time



bat_file_path = r"launcher.bat"

#add account logins here in a key : value pair format
hashmap ={}

for username, password in hashmap.items():
    
    process = subprocess.Popen([bat_file_path], shell=True)
    print(f"launching client for {username}")
    time.sleep(4)
    
    pyautogui.typewrite(username)

    pyautogui.press("tab")

    pyautogui.typewrite(password)

    pyautogui.press("enter")  
    #time.sleep(2)

print("clients launched")