'''
program: finalvideostoreproject.py
author: Vinny 10/14/2020

simple python gui window with a basic label
'''
from tkinter import *
from breezypythongui import EasyFrame

class vinsVideo(EasyFrame):
	'''displays a greeting in a window'''

	def __init__(self):
		'''sets up the window and the lablel'''
		EasyFrame.__init__(self, title = "Vinny's Video Store")

		# Vars and const
		newRental = 3.00
		oldRental = 2.00
		totalCost = newRental + oldRental

		# change background color
		self.configure(bg='green')

		# Add the label components
		self.addLabel(text = "How many videos are you renting?", row = 0, column = 0)

		#add the entry field components 
		self.amount = self.addFloatField(value = 0.0, row = 0, column = 1, height = 15, width = 50)

		#add the text area component
		self.outputArea = self.addTextArea(text = "", row = 4, column = 0, columnspan = 2, width = 50, height = 25)

		# add button
		self.compute = self.addButton(text = "Compute", row = 3, column = 0, columnspan = 2, command = self.compute)

		#Input phase
		newNum = int(input("How many new videos are being rented? >> "))
		oldNum = int(input("How many old videos are being rented? >> "))

		#Caclulation phase
		totalCost = (newRental * newNum) + (oldRental * oldNum)
		if newRental + oldRental == totalCost:
			result == totalCost

		#Output phase
		print("The customer renting " + str(newNum) + " new videos. And " + str(oldNum) + " old videos.")
		print("The total charge is: $" + str(totalCost))


		#event handling method
	def compute(self):
		"""computes the investment schedule based on the inputs and outputs the schedule"""


def main():
	'''instantiates and pops up the window.'''
	vinsVideo().mainloop()

#global call to main() funct
main()