# SnakeGame
Basilisk is a new take on the popular snake game. It consists of a GUI which lets users see high scorers and customise their game attributes to their liking. After that, they can play the classic snake game in a new skin, in the form of Basilisk!

## Modules used
  1. pygame - The game is built around the pygame module.
  2. pyglet - Module to play an intro video at the beginning of the game.
  3. random - To randomly spawn the food for the snake.
  4. mysql.connector - This was to update and read the high scores of players.

## How to run
  1. First, instal the pyglet, pygame and mysql.connector modules onto your computer.
  2. mysql needs to be setup in order for the program to work
     - A database named snake_game needs to be made
     - Create a table called scores with the following attributes
  	   - name   char(100)
	     - score	integer
	     - speed	char(50)
	     - size	char(50)
     - The default password used is "password", if not change the password in the main code in line 29
     - It is a requirement that the table needs to have 5 items in it in order for the program to work
     - It is recommended that the following syntax be used for setting the initial 5 items 
       - <name> , 0, "slow", "small"
       - These names need to be added manually within the mysql table
  3. After these steps, the python file can be run on the terminal. Have fun!
