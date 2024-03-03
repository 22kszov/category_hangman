# Category Hangman

Category Hangman is a fun terminl game that runs on Heroku. It uses python to bring you an interactive game where you can choose your own category where you guess a randomly selected word from that category!

![Homescreen of the game](./assets/images/homescreen.png)

## Running The Application

To run the application the steps are as follows:

- You can load acces it on Heroku with this link [Hangman](https://category-hangman-e049c70ad3f3.herokuapp.com/)
- Upon accessing you will be prompted to either play the game or to read the instructions
- When ready to play enter the correct prompt required
- Choose your category. You can do this by entering the number associated with your choice.
- Guess a letter.
- Correct guesses will show up for you to see what position(s) they are in the word
- Incorrect guesses will draw more of Hangman and lose a life
- When Hangman is fully drawn and all lives are lost you have lost the game
- If all letters are guessed before losing you win the game
- Upon win or loss you will be prompted to play again or exit the game

## Design and Features

For the aesthetic of the game I used the colorama python library to add color to my terminal text.

To help envision the flow of the game before creating it I used LucidChart to create a flowchart

![Flowchart](./assets/images/flowchart.png)

### Error Reading

The game makes sure the data you input at prompts will always be in a valid and the correct format and will display an error message and ask for the input again if otherwise. I achieved this with while loops, try statements, and if and for statements, giving the input guidelines to meet. eg. Input while guessing letter for hangman has to be a sting that is only one letter long. It also has to be a letter that hasnt already been guessed.
