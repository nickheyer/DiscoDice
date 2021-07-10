# DiscoDice
A simple dice rolling bot!

To roll some dice, type "!r", then the amound of dice, then "d", followed by the amount of sides on each dice. 

For example:
"!r 20d20" 
would return something like:
"Nicholas's roll: [18, 17, 17, 16, 13, 12, 11, 10, 10, 10, 10, 9, 8, 8, 8, 7, 4, 3, 3, 1] Result: 195"

If no quantity of dice is provided, it defaults to one.

For example:
"!r d20"
would return something like:
"Nicholas's roll: [14] Result: 14"

To change the dice-command prefix from "!r" to something else, type "!set keyword" followed by whatever you'd like to replace it with. 

For example:
"!set keyword I <3 DiscoDice"
would allow you to call the dice like this:
"I <3 DiscoDice 100d40"
which would return something like:
"Nicholas's roll: [40, 40, 40, 38, 38, 38, 38, 38, 37, 36, 36, 35, 35, 34, 34, 33, 32, 31, 30, 30, 29, 29, 29, 29, 28, 27, 27, 27, 27, 27, 26, 26, 26, 25, 25, 25, 25, 24, 24, 24, 21, 21, 20, 20, 20, 20, 19, 19, 19, 19, 19, 19, 18, 17, 17, 16, 16, 15, 15, 14, 13, 13, 13, 12, 12, 11, 11, 10, 10, 10, 10, 9, 9, 9, 8, 8, 8, 8, 8, 8, 8, 7, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 3, 3, 3, 3, 2, 1, 1] Result: 1887"

To install and run the bot, you need to create a new application via (https://discord.com/developers/applications). Once you have a TOKEN provided to you by discord, you can replace "INSERT DISCORD API TOKEN HERE" (check the beginning of DiscoDice.py) with your token.

Have any questions, contact me on discord! ~ NastyNick#4212
