from PyQt5.QtWidgets import * 
from PyQt5 import QtCore, QtGui 
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
import random 
import sys

class Window(QMainWindow): 

	def __init__(self): 
		super().__init__() 

		self.setWindowTitle("Color_Game  ")
		
		self.setGeometry(700, 200, 500, 500) 
		self.setStyleSheet("background-color: lightcyan")

		self.UiComponents() 
 
		self.show()
		self.count_value = 30

		self.score_value = 0
		self.start_Flag = False

		
		self.color_list = ['Red', 'Blue', 'Green', 'Pink', 'Black', 
				'Yellow', 'Orange', 'Purple', 'Brown'] 


    
		
	def UiComponents(self): 

		
		head = QLabel("Color Game", self) 

		head.setGeometry(100, 10, 300, 60) 

		head.setStyleSheet('color: purple')
		font = QFont('Times', 14) 
		font.setBold(True) 
		font.setItalic(True) 
		font.setUnderline(True)
		
		
		head.setFont(font) 

        
		head.setAlignment(Qt.AlignCenter) 

		
		instruction = QLabel("Instruction : Enter the Color not the text. "
							"Press Start button to start the game.     "
							"Note : Time limit for game is 30 seconds.", self) 


		instruction.setWordWrap(True) 


		instruction.setGeometry(20, 60, 460, 60) 

		
		start = QPushButton("Start / Reset", self) 

 
		start.setGeometry(200, 120, 100, 35)

		start.setStyleSheet("border:2px solid black; background : lightgrey;")

		 
		start.clicked.connect(self.start_action) 

		 
		self.score = QLabel("Score : 0", self) 

		 
		self.score.setGeometry(160, 170, 180, 50) 

		
		self.score.setAlignment(Qt.AlignCenter) 

		
		self.score.setFont(QFont('Times', 16)) 

		
		self.score.setStyleSheet("QLabel"
								"{"
								"border : 2px solid lightpink;"
								"color : black;"
								"background : lightpink;"
								"}") 

		
		self.color = QLabel("Color Name", self) 

		
		self.color.setGeometry(50, 230, 400, 120) 

		
		self.color.setAlignment(Qt.AlignCenter) 

		
		self.color.setFont(QFont('Times', 30)) 

		
		self.input_text = QLineEdit(self) 

		
		self.input_text.setGeometry(150, 340, 200, 50) 
		self.input_text.setStyleSheet("border : 2px solid blue;")

		
		self.input_text.setFont(QFont('Arial', 14)) 

		
		self.input_text.setDisabled(True) 

		
		self.input_text.returnPressed.connect(self.input_action) 

		
		self.count = QLabel("30", self) 

		
		self.count.setGeometry(225, 430, 50, 50) 

		
		self.count.setAlignment(Qt.AlignCenter) 

		
		self.count.setFont(QFont('Times', 14)) 

		
		self.count.setStyleSheet("border : 2px solid black;"
								"background : lightgreen;") 

		
		timer = QTimer(self) 

		
		timer.timeout.connect(self.show_time) 

		
		timer.start(1000) 

	def show_time(self): 

		if self.start_Flag:
			self.count.setText(str(self.count_value)) 

			# checking if count value is zero 
			if self.count_value == 0: 

				
				self.start_Flag = False

				 
				self.input_text.setDisabled(True) 


			# decrementing the count value 
			self.count_value -= 1

	def start_action(self): 

		
		self.start_Flag = True

		
		self.score.setText("Score : 0") 
		self.score_value = 0

		
		self.count_value = 30

		
		self.input_text.clear() 

		 
		self.input_text.setEnabled(True) 

		# getting random color 
		self.random_color = random.choice(self.color_list) 

		
		self.random_color.lower() 

		 
		self.color.setStyleSheet("color : " + self.random_color + ";") 

		 
		random_text = random.choice(self.color_list) 

		
		self.color.setText(random_text) 



	def input_action(self): 

		# get the line edit test 
		text = self.input_text.text() 

		 
		text.lower() 

		 
		if text == self.random_color: 
			 
			self.input_text.clear() 

			# incrementing score value 
			self.score_value += 1

			# setting score to the score label 
			self.score.setText("Score : " + str(self.score_value)) 

			 
			self.random_color = random.choice(self.color_list) 

			
			self.random_color.lower() 

			# setting random color to the label 
			self.color.setStyleSheet("color : " + self.random_color + ";") 

			random_text = random.choice(self.color_list) 

			 
			self.color.setText(random_text) 


App = QApplication(sys.argv) 

window = Window() 

sys.exit(App.exec()) 


