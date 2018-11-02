
#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import wget
import time
import threading
from app import *
from tkinter import *

label1 = None
label2 = None
for_download = []
path = 'programs'
start_frame = None
secondeFrame = None

programs_array = [google, yandex, sevenZip, winRar, codecPack, qBittorrent, python3, sublimetext, colorMania]


def app_download(var, firstFrame):
	global label1
	global label2

	firstFrame.destroy()
	
	start_frame = threading.Thread(target= download_programs)
	start_frame.start()
	if not os.path.exists(path):
		os.mkdir(path)	
	time.sleep(1)
	for i in range(len(programs_array)):
		if var[i].get() == 1:
			for_download.append(programs_array[i])
	for i in for_download:
		print(i.name)
		label2.config(text='Downloading: ' + i.name)
		wget.download(i.url, path)
	files = os.listdir(path)
	os.chdir(path)
	for i in files:
		label1.config(text = 'Please Wait!')
		label2.config(text='Installing: ' + i)
		os.system('"' + i + '"')
	label2.config(text = '')
	label1.config(text='Download completed!')


def download_programs():
	global label1
	global label2
	global start_frame
	global secondeFrame
	global for_download
	global programs_array

	for_download = []
	
	secondeFrame = Tk()

	secondeFrame.title('SMART-SETUP')

	secondeFrame.resizable(0, 0)

	secondeFrame.iconbitmap('docs/favicon.ico')

	label2 = Label(secondeFrame, text = 'Installing: ', bg='white', fg='#AA1D36')

	secondeFrame.config(bg = 'white')
	secondeFrame.config()

	#elements
	label1 = Label(secondeFrame, text = 'Please Wait!', bg='white', fg='black')

	#configs
	label1.config(font=('Arial', 14, 'bold'))
	label2.config(font=('Arial', 13, 'bold'))

	#grids
	label1.grid(column = 0, row = 0)
	label2.grid(column = 0, row = 1)

	#start
	secondeFrame.mainloop()