
#!/usr/bin/python
# -*- coding: utf-8 -*-

from ezprint import *
from tkinter import *
from download import *
import wget

var = []
firstFrame = None


def mainFrame():
	global var
	global firstFrame

	firstFrame = Tk()

	firstFrame.title('SMART-SETUP')

	firstFrame.resizable(0, 0)

	firstFrame.config(bg = 'white')
	firstFrame.config()

	firstFrame.iconbitmap('docs/favicon.ico')

	for i in range(9):
		var.append(IntVar())

	#elements
	label1 = Label(firstFrame, text = 'CHOOSE PROGRAMS FOR SETUP:' , bg='white', fg='black')
	label2 = Label(firstFrame, text = google.types , bg='white', fg='black')

	checkbutton1 = Checkbutton(firstFrame, text = google.name, variable = var[0])
	checkbutton2 = Checkbutton(firstFrame, text = yandex.name, variable = var[1])

	label3 = Label(firstFrame, text = sevenZip.types , bg='white', fg='black')

	checkbutton3 = Checkbutton(firstFrame, text = sevenZip.name, variable = var[2])
	checkbutton4 = Checkbutton(firstFrame, text = winRar.name, variable = var[3])

	label4 = Label(firstFrame, text = codecPack.types , bg='white', fg='black')

	checkbutton5 = Checkbutton(firstFrame, text = codecPack.name, variable = var[4])
	checkbutton6 = Checkbutton(firstFrame, text = qBittorrent.name, variable = var[5])

	label5 = Label(firstFrame, text = python3.types , bg='white', fg='black')

	checkbutton7 = Checkbutton(firstFrame, text = python3.name, variable = var[6])
	checkbutton8 = Checkbutton(firstFrame, text = sublimetext.name, variable = var[7])
	checkbutton9 = Checkbutton(firstFrame, text = colorMania.name, variable = var[8])

	button1 = Button(firstFrame, text = 'DOWNLOAD', command = lambda: app_download(var, firstFrame))

	#configs
	label1.config(font=('Arial', 14, 'bold'))
	label2.config(font=('Arial', 12, 'bold'))

	checkbutton1.config(fg = '#AA1D36', bg = 'white')
	checkbutton2.config(fg = '#AA1D36', bg = 'white')

	label3.config(font=('Arial', 12, 'bold'))

	checkbutton3.config(fg = '#AA1D36', bg = 'white')
	checkbutton4.config(fg = '#AA1D36', bg = 'white')

	label4.config(font=('Arial', 12, 'bold'))

	checkbutton5.config(fg = '#AA1D36', bg = 'white')
	checkbutton6.config(fg = '#AA1D36', bg = 'white')

	label5.config(font=('Arial', 12, 'bold'))

	checkbutton7.config(fg = '#AA1D36', bg = 'white')
	checkbutton8.config(fg = '#AA1D36', bg = 'white')
	checkbutton9.config(fg = '#AA1D36', bg = 'white')

	button1.config(font = ('Arial', 13, 'bold'))
	#grids
	label1.grid(column = 0, row = 0)
	label2.grid(column = 0, row = 1)

	checkbutton1.grid(column = 0, row = 2)
	checkbutton2.grid(column = 0, row = 3)

	label3.grid(column = 0, row = 4)

	checkbutton3.grid(column = 0, row = 5)
	checkbutton4.grid(column = 0, row = 6)

	label4.grid(column = 0, row = 7)

	checkbutton5.grid(column = 0, row = 8)
	checkbutton6.grid(column = 0, row = 9)

	label5.grid(column = 0, row = 10)

	checkbutton7.grid(column = 0, row = 11)
	checkbutton8.grid(column = 0, row = 12)
	checkbutton9.grid(column = 0, row = 13)

	button1.grid(column = 0, row = 14)

	#start
	firstFrame.mainloop()


if __name__ == '__main__':
	mainFrame()