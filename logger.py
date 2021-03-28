import webbrowser
import pyautogui
import time
import os
import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("Token Logger")

url = 'https://discord.com/login'

cmd = 'mode 50,20'    
os.system(cmd)

def cls():
    os.system("cls" if os.name == "nt" else "clear")

def login(tokens):
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)
    time.sleep(1.5)
    pyautogui.hotkey('ctrl', 'shift', 'i')
    pyautogui.click(x=1450, y=810)
    pyautogui.click()
    pyautogui.click()
    time.sleep(1)
    pyautogui.write ("""function login(token) {
setInterval(() => {
document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`
}, 50);
setTimeout(() => {
location.reload();
}, 2500);
}""")
    pyautogui.hotkey('enter')
    pyautogui.write(f'login("{tokens}")')
    pyautogui.hotkey('enter')

    cls()
    print(f";> Attempted to login to {tokens}...")
    restart = input("Type anything to restart;>")
    start()

    

def start():
    cls()
    print("""  _      ____   _____  _____ ______ _____  
 | |    / __ \ / ____|/ ____|  ____|  __ \ 
 | |   | |  | | |  __| |  __| |__  | |__) |
 | |   | |  | | | |_ | | |_ |  __| |  _  / 
 | |___| |__| | |__| | |__| | |____| | \ \ 
 |______\____/ \_____|\_____|______|_|  \_\
                                           
                                           """)
    tokens = input("\n;>Enter a Token To Log: ")
    login(tokens)

start()





