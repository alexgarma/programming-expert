# Project description

For this project you will be asked to create a program that can schedule games that teams will play in an end of year tournament. You will only be responsible for determining the games played in the first round of the tournament.

You will first need to ask the user of your program to input the number of teams; you may assume there will always be an even number of teams (you don't need to validate this). Next you will need to ask for the names of all of the teams and store them in some way.

After this you'll need to determine the number of games that were played by each team; you may assume each team plays the same number of games. Finally, you'll need to determine the number of wins each team had during the regular season.

When asking for user input, you'll need to make sure all input is valid and ask the user to try again if they give you invalid input. You may assume user input will always be the correct type (i.e. if you ask for a number you will always get an integer). You can determine if the input is invalid by looking at the following constraints:

    There are always at least 2 teams in the tournament.
    Each team plays every other team at least once in the regular season.
    All team names contain at most 2 words and at least 2 characters.
    Each team has at minimum 0 wins and no more wins than the number of games they played.

In the first round of the tournament the teams with the most regular season wins play the teams with the least regular season wins. For example, if Team A has 5 wins, Team B has 4 wins, Team C has 3 wins and Team D has 2 wins then Team A and Team D play each other and Team B and C play each other. If teams are tied for wins and/or losses then your program can choose any appropriate team.

Your program should output the games that should be played in the format seen below. The first game outputted should contain the team with the most regular season wins, the second game should contain the team with the second most regular season wins, etc. The home team of each game should be the team with the least wins of the two, if there is a tie in wins your program can chose any appropriate team.

See below for the sample program execution. Your prompts and output should follow the same format as seen below.

## Sample Program Execution #1

``````
    Enter the number of teams in the tournament: 1
    The minimum number of teams is 2, try again.
    Enter the number of teams in the tournament: 4
    Enter the name for team #1: Python
    Enter the name for team #2: Ruby
    Enter the name for team #3: JavaScript
    Enter the name for team #4: C
    Team names must have at least 2 characters, try again.
    Enter the name for team #4: C Is Great
    Team names may have at most 2 words, try again.
    Enter the name for Team #4: C#
    Enter the number of games played by each team: 2
    Invalid number of games. Each team plays each other at least once in the regular season, try again.
    Enter the number of games played by each team: 3
    Enter the number of wins Team Python had: 2 
    Enter the number of wins Team Ruby had: 1 
    Enter the number of wins Team JavaScript had: 0 
    Enter the number of wins Team C# had: -2
    The minimum number of wins is 0, try again.
    Enter the number of wins Team C# had: 3
    Generating the games to be played in the first round of the tournament...
    Home: JavaScript VS Away: C#
    Home: Ruby VS Away: Python
``````

## Sample Program Execution #2

``````
Enter the number of teams in the tournament: 6
Enter the name for team #1: AA
Enter the name for team #2: BB
Enter the name for team #3: CC
Enter the name for team #4: DD
Enter the name for team #5: EE
Enter the name for team #6: FF
Enter the number of games played by each team: 2
Invalid number of games. Each team plays each other at least once in the regular season, try again.
Enter the number of games played by each team: 6
Enter the number of wins Team AA had: 1 
Enter the number of wins Team BB had: 4 
Enter the number of wins Team CC had: 3 
Enter the number of wins Team DD had: 4 
Enter the number of wins Team EE had: 2 
Enter the number of wins Team FF had: 7 
The maximum number of wins is 6, try again.
Enter the number of wins Team FF had: 5 
Generating the games to be played in the first round of the tournament...
Home: AA VS Away: FF
Home: EE VS Away: BB
Home: CC VS Away: DD
``````

The games generated from this example could also be the following:

``````
Home: AA VS Away: FF
Home: EE VS Away: DD
Home: CC VS Away: BB
``````