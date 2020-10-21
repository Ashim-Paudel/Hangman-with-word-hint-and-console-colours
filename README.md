# Hangman-with-word-hint-and-console-colours

A simple non-graphical game, HANGMAN, developed using python. This is another version for the first repository.

This game, HANGMAN is developed on the idea to improve vocabs for school level children and to learn by playing.

The main idea of this game is to guess certain word based on the number of blank spaces(or underscores) to be filled up and some hints too. You can guess either whole word at once or letter-by-letter too. If your guess(the word as a whole) is correct/matches the word to be guessed, you win. Else, if you guessed wrong word only first letter of your entry will be accepted as input and checked for matching of the letter, if matched you can continue but if it mis-matched, for each wrong attempts: a hanging man will start to create. So, in total you will have 7 attempts to guess the word(including rope, head, hand-hand, stomach and two legs for the hanging man). Moreover, accessing hint for the word will also reduce your attempt by 1.

While entering letters, what if you inputted the same letter twice? Will it reduce my chances?----Well no! For each of your entries, the letter will be stored as lists. The correctly guessed and incorrectly guessed words being in separate lists. And, for other inputs your input will be compared whether that letter is already in those list or not, if they are already persent, then it displays that you've already correctly/incorrectly guessed that particular letter.

In this concept the program functions.

I will be very happy if anyone find this code and assist them while learning python and creating a simple HANGMAN game.
