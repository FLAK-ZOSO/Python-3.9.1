#!/usr/bin/env python3
import webbrowser
import pyautogui
import time
import sys

'''
class ChromeForeground(webbrowser.Chrome):
    background = False # Open Chrome in foreground [so that the human can interact]
webbrowser.register(
    'chrome', None, ChromeForeground(
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
    )
)
driver = webbrowser.get('chrome')
'''

if __name__ == '__main__':
    # python blocca-webbrowser.py upvoters.txt 1 5
    if '--help' in sys.argv:
        print('python blocca-webbrowser.py <users-file> <login-time> <block-time>')
        exit(0)
    url: str = sys.argv[1]
    webbrowser.open("http://it.quora.com") # Open Quora in Chrome
    login_time = int(sys.argv[2])
    time.sleep(login_time) # Wait for [manual] login
    block_time = int(sys.argv[3])
    with open(url, 'r') as f:
        for line in f.readlines():
            webbrowser.open(line)
            '''
            time.sleep(0.5)
            for _ in range(29):
                pyautogui.press('tab')
            pyautogui.press('enter')
            time.sleep(0.3)
            for _ in range(3):
                pyautogui.press('tab')
            pyautogui.press('enter')
            '''
            time.sleep(block_time) # Wait for [manual] block
            pyautogui.hotkey('ctrl', 'w') # Close tab