#!/bin/python
#Copyright 2014 Joshua Barrett
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.

import json, sys, tkMessageBox
from Tkinter import *
from ttk import *

class Question:
	def __init__(self, master, dictlist):
		self.dictlist = dictlist
		self.master = master
		self.window = Toplevel(self.master)
		self.window.protocol('WM_DELETE_WINDOW', self.delete)
		self.frame = Frame(self.window)
		Label(self.frame, text=dictlist[0]["question"]).pack()
		self.entry = Entry(self.frame, width=50)
		self.entry.pack() #so that the above statment returns entry.
		self.btn=Button(self.frame, text="Submit", command=self.submit)
		Button(self.frame, text="Cancel", command=self.cancel).pack()
		self.btn.pack()
		self.frame.pack()
	def submit(self):
		self.btn.config(state=DISABLED)
		dl = self.dictlist.pop(0)
		if dl["answer"].lower() == self.entry.get().strip().lower():
			tkMessageBox.showinfo("result","Correct!")
		else:
			tkMessageBox.showinfo("result","Sorry, no. The answer is %s" % dl['answer'])
		self.window.destroy()
		recurse(self.dictlist)
		return
	def cancel(self):
		tkMessageBox.showinfo("abort", "The quiz has been aborted")
		global rbtn
		rbtn.config(state=NORMAL)
		self.window.destroy()
	def delete(self):
		pass
def quiz():
	global rbtn
	rbtn.config(state=DISABLED)
	try:
		f = open('quizconf','r')
	except IOError:
		tkMessageBox.showinfo("FileError:", "Error: .quizconf file not found. Please create file. Remember to write valid JSON")
		sys.exit(0)
	x = json.load(f)
	f.close
	recurse(x)

def recurse(dictlist):
	if dictlist:
		Question(root,dictlist)
	else:
		tkMessageBox.showinfo("Congratulations!", "You have finished the geothermal energy quiz! Did you learn anything?")
		global rbtn
		rbtn.config(state=NORMAL)
		return

def about():
	tkMessageBox.showinfo("about", "This program was written by Joshua Barrett, in the Python programming language, making use of the Tkinter graphics library. Thanks to the great people on the StackExchange network for answering many of the questions I needed answered to code this thing. The code is freely available on my github, at github.com/qwertyuiop924")
root=Tk()
rframe = Frame(root, width=300, height=150)
rframe.pack_propagate(0)
rframe.pack()
root.title("Geothermal Quiz!")
rbtn = Button(rframe, text="Take The Quiz", command=quiz)
rbtn.pack()
Button(rframe, text="About This Program", command=about).pack()
root.mainloop()
