import requests, re, sys, os
import urllib.parse

print('getting this shit --> ' + sys.argv[1])

video_url = urllib.parse.quote(sys.argv[1])
url = 'https://bitdownloader.com/download?video='+ video_url
try:
	r = requests.get(url) #dsa
	te = re.search('id="mainDlBtn" class="no-selection downloadBtn" .* href=".*&dl=1', r.text).group()
	noamp = te.replace('amp;', '')
	print(re.search('https://.*', noamp).group()) # копирование ссылки
except:
	print("ne poluchilos")
	sys.exit()

command = "c:\\apps\\downloadmaster\\"+ re.search(' https://.*', noamp).group() # требуется наличие в PATH ярлыка на Download Master 
os.system(command)