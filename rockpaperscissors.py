from random import choice
import time

player_win = 0
computer_win = 0

while player_win <= 2 and computer_win <= 2:

	player = raw_input("Rock, paper, or scissors? Your choice here: ")

	player = player.lower()

	print "You picked {0}! \nNow let's see how that went for you.".format(player)

	time.sleep(1)

	comp = choice(("rock", "paper","scissors"))

	print "The computer picked {0}.".format(comp)

	time.sleep(1)

	if player == "rock":
		if comp == "rock":
			print "tie! you should redraw."
		elif comp == "paper":
			print "the computer picked paper, and paper beats rock. you lose!"
			computer_win = computer_win + 1
		elif comp == "scissors":
			print "the computer picked scissors, and rock beats scissors. you win!"
			player_win = player_win + 1
	elif player == "paper":
		if comp == "paper":
			print "tie! you should redraw."
		elif comp == "scissors":
			print "the computer picked scissors, and scissors beats paper. you lose!"
			computer_win = computer_win + 1
		elif comp == "rock":
			print "the computer picked rock, and paper beats rock. you win!"
			player_win = player_win + 1
	elif player == "scissors":
		if comp == "scissors":
			print "tie! you should redraw."
		elif comp == "rock":
			print "the computer picked rock, and rock beats scissors. you lose!"
			computer_win = computer_win + 1
		elif comp == "paper":
			print "the computer picked paper, and scissors beats paper. you win!"
			player_win = player_win + 1
	else:
		print "you didn't pick rock, paper, or scissors. bummer. try again!"

	time.sleep(.5)

	print "Your score is {0} and the computer's score is {1}.".format(player_win, computer_win)


if computer_win == 3:
	print "You lose!"
elif player_win == 3:
	print "You win!"




