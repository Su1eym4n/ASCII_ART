import time
import os
import pickle
from ascii_art import ImageToAscii
#asciify a video
obj = ImageToAscii("/Users/suleiman/Desktop/BigProjects/ASCII_ART/video/shrek.mov", 5)
obj.video_ascii()

def read():
	pickle_off = open ("output.txt", "rb")
	emp = pickle.load(pickle_off)
	for el in emp:
		print(el)
		time.sleep(0.02)
		os.system('clear')
read()

os.system('clear')
#asciify an image
obj = ImageToAscii("/Users/suleiman/Desktop/BigProjects/ASCII_ART/img/tony.jpeg", 4)
obj.image_ascii()
