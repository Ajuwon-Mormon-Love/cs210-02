# cse210-03 Jumper

__The Game of Jumper__

_There are old skydivers and bold skydivers,_  
_but there are no old, bold skydivers._  
  
_- Jeff Wuorio -_ 

---
## Overview

Jumper is a game in which the player seeks to solve a puzzle by guessing the letters of a secret word one letter at a time.

---
## Getting Started

Make sure you have Python 3.8.0 or newer installed and running on your machine. Open a terminal and browse to the project's root folder. Start the program by running the following command.
```
python3 jumper 
```
or 
```
py jumper
```
You can also run the program from an IDE like Visual Studio Code. Start your IDE and open the project folder. Select the main module inside the dice folder and click the "run" button.

If a plain text file called `lexicon.txt` is present in the `data` folder, this will be used as a master word list. Each word must be on its own line. 

---
## Project Structure

The project files and folders are organized as follows:
```
root                         (project root folder)
+-- jumper                   (source code for game)
  +-- game                   (specific classes)
    +-- dictionary.py        (word disctionary class)
    +-- director.py          (director class)
    +-- skydiver.py          (skydiver class)
    +-- player.py            (player class)
    +-- terminal_service.py  (terminal service class)
  +-- data                   (game data folder)
    +-- lexicon.txt          (optional - a word list in plain text format, 1 word each line)
  +-- __main__.py            (program entry point)
+-- README.md                (general info)
```
---
## Required Technologies

* Python >= 3.8.0

---
## Authors

* Spencer Bell (bel21032@byui.edu) _Terminal Service class_ 
* Dallas Eaton (deaton879@byui.edu) _Jumper display class_
* Julian Hernandez (hernandezjuliang44@gmail.com) _Player class_
* Mike Lewis (wyoming.c64@gmail.com) _Dictionary class_
* Jaden McCarrey (jadenmccarrey@gmail.com) _Director class_

---
## Rules

Jumper is played according to the following rules.

- The puzzle is a secret word randomly chosen from a list.
- The player guesses a letter in the puzzle.
- If the guess is correct, the letter is revealed.
- If the guess is incorrect, a line is cut on the player's parachute.
- If the puzzle is solved the game is over.
- If the player has no more parachute the game is over.

---
## Requirements

The program must also meet the following requirements.

- [x] The program must include a README file.
- [x] The program must include class and method comments.
- [x] The program must have at least four classes.
- [x] The program must remain true to game play described in the overview.

---
## Have Some Fun

Have some fun by enhancing the game any way you like. A few ideas are as follows.

- [x] Enhanced input validation.
- [x] Enhanced game play and game over messages.
- [ ] Enhanced game display, e.g. parachute
