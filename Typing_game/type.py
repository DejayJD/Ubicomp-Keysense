#!/usr/bin/env python
import gui, random, time, pygame



class TypeTextInput(gui.TextInput):

	def __init__(self):
		gui.TextInput.__init__(self, (10, 300), 100, (800, 100))
				

	def key_pressed(self, key):
		#print key
		if key == 13: # ENTER
			self.text = ""
		elif key == 8: # BACKSPACE
			self.text = self.text[:-1]
		elif key in range(256):
			self.text += chr(key)
	

class TypeGUI(gui.GUI):
	
	
	def __init__(self):
		gui.GUI.__init__(self, (800,400))
		self.words = []
		self.read_wordlist("wordlist.txt")
		self.word = random.choice(self.words)
		self.word_counter = 0
		self.character_counter = 0
		self.start_time = time.time()
		
	
		exit_button = gui.Button((700,10), (50,30), "EXIT", (0, 100, 200))
		exit_button.onclick = self.exit_button_clicked
		self.buttons.append(exit_button)
		
		reset_button = gui.Button((650,10), (50,30), "RESET", (0, 200, 100))
		reset_button.onclick = self.reset_button_clicked
		self.buttons.append(reset_button)
		
		self.word_caption = gui.Caption((10, 100), 100, (800, 100), self.word, 0, (255,255,255))
		self.captions.append(self.word_caption)
		
		self.info_caption = gui.Caption((10, 10), 20, (450, 100), "")
		self.captions.append(self.info_caption)
		
		self.input_word = TypeTextInput()
		self.input_word.active = True
		self.text_inputs.append(self.input_word)
		
	
	def exit_button_clicked(self):
		self.exit()
		
	def reset_button_clicked(self):
		self.word = random.choice(self.words)
		self.word_counter = 0
		self.character_counter = 0
		self.start_time = time.time()
		
		self.word_caption.text = self.word
		self.info_caption.text = ""
		self.input_word.text = ""
		
	def right_word_entered(self):
		self.character_counter += len(self.word)
		self.word_counter += 1
		self.input_word.text = ""
		self.word = random.choice(self.words)
		self.word_caption.text = self.word
		
	def inloop(self):
		if self.word_caption.text == self.input_word.text:
			self.right_word_entered()
		speed = 0
		charspeed = 0
		now = time.time()
		if not self.word_counter == 0:
			speed = self.word_counter / (now - self.start_time)
			speed = round(speed, 2)
			charspeed = 60. * self.character_counter / (now - self.start_time)
			charspeed = round(charspeed, 2)
		self.info_caption.text = "speed (words/s): " + str(speed) + "      speed (chars/m): " + str(charspeed)
	
	def read_wordlist(self, filename):
		f = open(filename, "r")
		lines = f.readlines()
		f.close()
		self.words = []
		for line in lines:
			self.words.append(line[:-1].lower())
	
if __name__ == "__main__":

	typegui = TypeGUI()
	typegui.start()
