import os
import webbrowser

chrome_path = "C:\Program Files\Google\Chrome\Application\chrome.exe"


# https://stackoverflow.com/questions/63451737/open-all-html-files-from-a-folder-with-browser-in-python-enviroment
def open_files_in_browser(folder_name: str, extension: str) -> None:
    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
    browser = webbrowser.get('chrome')
    print(f'Opening all {extension} files in {folder_name}...')
    for filename in os.listdir(folder_name):
        if filename.endswith(f".{extension}"):
            browser.open_new_tab(os.path.join(folder_name, filename))


open_files_in_browser(r'C:\Users\vegans\Pictures\Screenshots', 'png')