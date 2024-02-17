""" Using CMD module to play
music in parallel."""
import os
import cmd
from pydub import AudioSegment
from pydub.playback import play
from pygame.mixer import music
import pygame
pygame.mixer.init()

class MusicPlayer(cmd.Cmd):
	def do_play(self, fp):
		try:
			print("Here1")
			music.load(fp)
			print("Here2")
			music.play()
			print("Here3")
			print("playing")
			return
		except Exception as e:
			print("Error occurred", e)
			pass
	def do_list(self, line):
		print(os.getcwd())
		print(os.listdir("jingles"))

if __name__ == "__main__":
	MusicPlayer().cmdloop()