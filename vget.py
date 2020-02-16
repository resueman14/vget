import requests, re, sys, os
import urllib.parse
import pyperclip, pynput
from pynput.keyboard import Key, Controller

keyboard = Controller()
print('getting this shit --> ' + sys.argv[1])

video_url = urllib.parse.quote(sys.argv[1])
url = 'https://bitdownloader.com/download?video='+ video_url
try:
	r = requests.get(url) #dsa
	te = re.search('id="mainDlBtn" class="no-selection downloadBtn" .* href=".*&dl=1', r.text).group()
	noamp = te.replace('amp;', '')
	pyperclip.copy(re.search('https://.*', noamp).group()) # копирование ссылки
except:
	print("ne poluchilos")
	sys.exit()

command = "dm.lnk" # требуется наличие в PATH ярлыка на Download Master 
os.system(command)
os.system(command)
keyboard.press(Key.insert)
keyboard.release(Key.insert)
keyboard.press(Key.insert)
keyboard.release(Key.insert)
keyboard.press(Key.enter)
keyboard.release(Key.enter)
