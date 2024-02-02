# Soccer Quiz
#### Video Demo:  <https://youtu.be/hhDeEPS-eU0>
#### Description:
About the project:
My name is Pedro Henrique, I'm from Brazil and this is my Final Project for the CS50 - Introduction to Programming with Python course, at Harvard. The project is a game, it's called "Soccer Quiz". This idea was a combination of my passion for both football and games.

The game works as follows: the user must choose one of three available languages, Portuguese (you must type "pt"), English (you must type "en") or Spanish (you must type "es"), only these entries are accepted. After that, the user needs to type their name correctly (no special characters or numbers are allowed, only letters and spaces) and then they are guided to the application's main menu. This has three options: start playing the quiz, view the overall game rating or exit the game.

If you choose the first option from the main menu, the game starts, and the player must answer ten multiple-choice questions about the world of football, one at a time. Every question has four answer alternatives, with three false and only one true. After each player's answer, the application displays information indicating whether the player got the question right or wrong (in case of a correct answer to the question, the information is displayed in green color, in case of an incorrect answer to the question, the information is displayed in red color) and what your score is so far. At the end of all questions, the player's final score is displayed, along with feedback on performance (in case of "Bad" performance, the information is displayed in red color, in case of "Regular" performance, the information is displayed in yellow color and in case of "Good" performance, the information is displayed in green color), and the game returns to the main menu.

If you choose the second option from the main menu, the game displays to the player a table that lists the ten best scores ever obtained by players when playing the game, along with the player's name and the date the game was played.

If you choose the third option from the main menu, the game displays a thank you message and the application closes.

More details about the game:
- Every player's starting score is zero.
- Every time the player gets a question right, his score increases by one point.
- The maximum possible points in a game is ten and the minimum is zero.
- If in a game, the player gets between 8 and 10 questions correct, his performance is evaluated as "Excellent", if the player gets between 4 and 7 questions correct, his performance is evaluated as "Regular" and if the player gets between 0 and 3 correct questions, your performance is rated as "Poor".
- The issues involve FIFA World Cups, FIFA best in the world awards, players, clubs, European leagues and European Champions Leagues.
- Each game contains ten questions for the player to answer, these are chosen randomly from at least thirty questions present in a specific file (explained below).
- Each question has four answer alternatives, and these are randomly arranged between options A, B, C and D.
- The player chooses a language as soon as he starts the application, and from then on, all information displayed on the screen will be in the specified language.

About project files:
The project contains eight files, each of which will be described below.

project.py:
This is the main file, where all the application programming was done. Contains all the functions necessary for the game to work.

questions.csv:
This is the file where all the questions consulted by the application are located. It contains the questions themselves, the answers, three wrong answer alternatives, and whether the alternatives require translation. 34 (thirty-four) questions are available.

ranking.csv:
This is the file where at the end of each game, the player's performance is written. Contains the player's name, the score obtained and the date on which the game took place.

README.md:
This is the file where the project documentation is described.

requirements.txt:
This is the file where all the libraries necessary for the correct functioning of the application itself are mentioned.

test_project.py:
This is the file where the functions that test some of the functions contained in the main "project.py" file are located.

test_questions.csv:
This is the file used by the "test_project.py" file to test the function of configuring the list of questions in the "project.py" file. Contains an example question to confirm that the function really does its job.

test_ranking.csv:
This is the file used by the "test_project.py" file to test the game ranking function of the "project.py" file. Contains an example of a score record to confirm that the function really does its job.
