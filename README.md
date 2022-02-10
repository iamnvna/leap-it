### Project Sixteen - 100DaysOfCode
# Leap it!
This is a simple program collects user input (a year) and prints out whether the user input is a leap year or not.

## Background
This project is part of my #100DaysOfCode learning streak. I intend to write a simple python program each day. Each project would:
* be heavily commented for learning purposes;
* include a README file similar to this one;
* include an algorithm to solve it without code;
* include a summary of what I learnt.

## Algorithm
1. Start.
2. Create a variable to hold the year from the user.
3. Evaluate the user import to be sure the user input is valid.
4. Use basic if/else if/else statements to iterate through the following:
* If the year modulo 400 returns 0 and the year modulo 100 returns 0, then the year is a leap year.
* Else if the year modulo 4 returns 0 and the year modulo 100 is not 0, then the year is a leap year.
* Else the year is not a leap year.
5. Print the appropriate output that correlates with the evaluation from step 4.
6. Stop.

*NB: A leap year is made up of 366 days exactly and so returns no remainder when divided by 0*

## What I've learnt
* This program, just like **[Project 15](https://github.com/iamnvna/guess-the-word)** improved my use of if/else if/else and 'if ... in ...' statement use.
* I deployed Error Handling code to successfully evaluate user input in this code. 