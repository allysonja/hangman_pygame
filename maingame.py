import random
import pygame
import sys
from pygame import *

pygame.init()
fps = pygame.time.Clock()

# CONSTANTS #
# DIMENSIONS #
WIDTH = 600
HEIGHT = 400

# COLORS #
WHITE = (255, 255, 255)
BLACK = (0 ,0, 0)

# GAME #
word_file = "dictionary.txt"
WORDS = open(word_file).read().splitlines()
word = random.choice(WORDS).upper()[1:-1]

window = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pygame.display.set_caption('Hangman')

# GLOBAL VARIABLES #
# GAME #
word_display = ""
for char in word:
	word_display += "_ "
guess = ""
remaining_letters = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"

def draw(canvas):
	global word, word_display, guess, remaining_letters

	# create game canvas #
	canvas.fill(WHITE)

	if guess != "":
		print(word)
		print(guess)
		index = 0
		for char in word:
			if guess == char:
				word_display = word_display[:index * 2] + char + word_display[index * 2 - 1:]
				print(word_display)
			index += 1
		letter_index = remaining_letters.find(guess)
		remaining_letters = remaining_letters[:letter_index:] + remaining_letters[letter_index + 1::]
		print(remaining_letters)
		guess = ""

def keydown(event):
	global guess, won

	if event.unicode.isalpha():
		guess = event.unicode.upper()

init()

while True:
	draw(window)

	for event in pygame.event.get():

		if event.type == KEYDOWN:
			keydown(event)
		elif event.type == QUIT:
			pygame.quit()
			sys.exit()

	pygame.display.update()
	fps.tick(60)