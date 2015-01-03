import pygame, sys, random
from pygame.locals import *

def main(screen, player, screen_width, screen_height, player_rect):

	font = pygame.font.Font(None, 50) # using the standard pygame.font font

	score = 0
	level = 1

	donut = pygame.image.load('donut.png')
	donuts = []

	donut_event = pygame.USEREVENT+1
	pygame.time.set_timer(donut_event, 2000)

	new_donuts = []

	move_donuts = pygame.USEREVENT+2
	pygame.time.set_timer(move_donuts, 10)

	draw_event = pygame.USEREVENT+3
	pygame.time.set_timer(draw_event, 15)

	while True:

		for event in pygame.event.get():

			if event.type == QUIT: # simply quits the program
				pygame.quit()
				sys.exit()

			elif event.type == donut_event: # let the donuts appear

				if len(new_donuts) < 4:
					donut_x = random.randint(1,screen_width-donut.get_size()[1])
					screen.blit(donut, (donut_x,0))
					donut_position = (donut_x,0)
					donuts.append([donut_x,0])

			elif event.type == move_donuts:

				if len(donuts) > 0:
					new_donuts = []
					for i in donuts:
						i[1] = i[1] + 1
						if i[0] >= player_rect[0] and i[0] <= player_rect[0] + player.get_size()[0] and i[1] >= screen_height - player.get_size()[1] - donut.get_size()[1]/2: # teste ob kollidiert
							score = score + 10 # wenn ja score hoch
							i[1] = screen_height # kollidiert = 1
						elif i[1] < screen_height - donut.get_size()[1]:
								new_donuts.append([i[0], i[1]])
				donuts = new_donuts

			elif event.type == KEYDOWN: # handling keydown events

				if event.key == K_LEFT: # left key
					screen.fill(000000)
					player_rect = [player_rect[0] - 1, player_rect[1]] # set new position
					if player_rect[0] < 0: # don't you dare leaving the screen
						player_rect = [0, player_rect[1]]

				if event.key == K_RIGHT: # right key
					screen.fill(000000) # erase previous screen
					player_rect = [player_rect[0] + 1, player_rect[1]] # set new position
					if player_rect[0] > screen_width - player.get_size()[0]: # oh no you don't
						player_rect = [screen_width - player.get_size()[0], player_rect[1]]

			elif event.type == draw_event:

				screen.fill(000000)

				show_score = font.render(str(score), 1, (0xff, 0xff, 0xff)) # rendering the score
				show_level = font.render(str(level), 1, (0xff, 0xff, 0xff)) # rendering the level

				for i in new_donuts:
					screen.blit(donut, (i[0], i[1]))

				levelpos = (10, 10)
				scorepos = (screen_width - 10 - show_score.get_size()[0], 10)
				screen.blit(show_score, scorepos) # showing the score
				screen.blit(show_level, levelpos) # showing the level
				screen.blit(player, player_rect) # spawn player at player_rect

				pygame.display.update() # update the screen
