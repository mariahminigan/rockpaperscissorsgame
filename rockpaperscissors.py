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
			print "Tie! You should redraw."
		elif comp == "paper":
			print "The computer picked paper, and paper beats rock. You lost this round!"
			computer_win = computer_win + 1
		elif comp == "scissors":
			print "The computer picked scissors, and rock beats scissors. You won this round!"
			player_win = player_win + 1
	elif player == "paper":
		if comp == "paper":
			print "Tie! You should redraw."
		elif comp == "scissors":
			print "The computer picked scissors, and scissors beats paper. You lost this round!"
			computer_win = computer_win + 1
		elif comp == "rock":
			print "The computer picked rock, and paper beats rock. You won this round!"
			player_win = player_win + 1
	elif player == "scissors":
		if comp == "scissors":
			print "tie! you should redraw."
		elif comp == "rock":
			print "the computer picked rock, and rock beats scissors. You lost this round!"
			computer_win = computer_win + 1
		elif comp == "paper":
			print "the computer picked paper, and scissors beats paper. You won this round!"
			player_win = player_win + 1
	elif player == "ham"
		print "That definitely wasn't an option. Points for creativity!"
			player_win = player_win + 1
	else:
		print "You didn't pick rock, paper, or scissors. Bummer. Try again!"

	time.sleep(.5)

	print "Your score is {0} and the computer's score is {1}.".format(player_win, computer_win)


if computer_win == 3:
	print "You lost the game!"
elif player_win == 3:
	print "You won the game!"




