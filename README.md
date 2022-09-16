This Battleships game is a basic single-player game in Python. You have 15 turns in which you have to find 2 out of 5 ships to win.

Things within the board:
1. "-" = empty space
2. "X" = ship that you hit

![Photo of project running in terminal](/assets/images/battleships.png)

# Contents
# User Experience UX
## User Stories
- As a user you want to play the game comfortably, meaning knowing what you need to do in order to win.
- As a user when you put an incorrect value it gives the value message with accepted values.
- As a user I want to see how many turns I have left in order to win.

## Game Structure
In my battleships game I wanted to have an X when hit and a - when miss with a text if I have hit or missed.
Also, I have put out the number of turns left to the terminal and the number of ships to sink within those turns to win.

## Design Choices
The first thing you see when you play the game is the banner of battleships, which states very clearly that you are playing a battleships game, and to enter your name to make it more personal. Also there is a board in which the guesses of the player get to.

## Colour Scheme
I have used no HTML or CSS for this project, so I have made it black and white.

# Features
Currently this is a basic battleships game for 1 player.
## Existing Features
- The game keeps track of turns left and displays this to user.
- 2 hits out of 15 turns are needed to win.
- Personalised to enter a name before playing and using that name within the game.
- If the user hits or missed he gets a notification after the attack
- If user enters a non supported / false value they get a message which value is supported to enter according to their stage in the game.
## Future Features
- Make it a 2 player game (computer and player)
- Make it more user friendly and easier to use.
- Updating the colour scheme to enchance the playing.

## Technologies Used
- Github, to host the content and show the history of the game
- Gitpod, used to make the game.
- Python, used to code the game (Only Python is used)
- Heroku, used to deploy the game, as asked from the CodeInstitute contents.

## Testing
I tested this software using the PEP8 Validator
![Testing proof](/assets/images/pep8.png)

## Bugs
- There are some error messages in the syntax, however the game currently runs smoothly.
- The banner is to long in character space, but it doesn't seem to give any problems in running the game.

# Deployment
The game was made in Github, but deployed to heroku. The steps to deploy are below:

- In the Heroku repository, go to the Settings tab.
- Once in Settings, go to the built-in packages tab on the right side. Add two packages including Python and NodeJS
- Connect your github GitHub to Heroku so you can access your repository.
- You will scroll down and see two options to move automatically or move manually

[live link to github repository](https://github.com/jouryk0rt/battleships-game)

[live link to heroku](https://battleships-game-python1.herokuapp.com/)

# Credits
## Content
The layout and game idea came from [This youtube tutorial](https://www.youtube.com/watch?v=tF1WRCrd_HQ)
## Media
All the media created I made myself.
## Acknowledgements
The game was completed for the study of Fullstack Developer at Code Institute. I want to thank my mentor Rahul for his guiding throughout the project.

