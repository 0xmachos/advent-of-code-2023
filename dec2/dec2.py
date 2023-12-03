#!/usr/bin/env python3
# advent-of-code-2023/dec2.py

# Determine which games would have been possible if the bag had been loaded with only
# 12 red cubes, 13 green cubes, and 14 blue cubes. What is the sum of the IDs of those games?

# The power of a set of cubes is equal to the numbers of red, green, and blue cubes multiplied together.
# For each game, find the minimum set of cubes that must have been present. What is the sum of the power of these sets?

import re
input = open("dec2-input.txt", 'r')

red_limit = 12
green_limit = 13
blue_limit = 14

possible_games = []
game_powers = []

for line in input:
    possible = True
    # Start with assumption that game is possible, this allows us to set possible to False if one set in a game is not
    # possible thus marking the whole game as not possible
    game_id = re.search(r'\d+', line).group()
    # Need to use .group() here matched subgroup as a string otherwise it's a re.Match object

    game_string = line.partition(":")[-1]
    # Get the last item in the list when splitting on :, safe here as we know the input is always same format
    # ('Game 88', ':', ' 3 green, 4 blue, 11 red; 3 green, 4 blue, 3 red; 10 red, 3 green; 3 blue, 2 red, 2 green\n')
    # With [-1] we get: 10 red, 6 blue, 11 green; 1 red, 11 green; 7 blue, 6 red, 11 green

    game_string = game_string.split(";")
    # Each set in a game is delinaited by ;
    # This breaks each set into an item in a list
    # [' 7 red', ' 5 blue, 11 red, 8 green', ' 8 red, 3 green, 2 blue\n']

    color_counts_max = {'green': 0, 'blue': 0, 'red': 0}
    # Create a dictionary to track max count value of each colour in a game (line)

    for game_set in game_string:
        color_counts = {'green': 0, 'blue': 0, 'red': 0}
        # Create a dictionary to track the count of each colour in each set
        set_parts = game_set.split(",")
        # Set would be e.g 4 green, 7 blue
        # After the split on , we get a list with an item for each colour in the set
        # e.g [' 4 green', ' 7 blue']
        for part in set_parts:
            number, colour = part.strip().split(' ')
            # part would be e.g. 4 green
            # After the split on space we get two variables number and colour
            # The value before the space is assigned to number and the value after the space is assigned to colour
            # number = 4
            # colour = green
            color_counts[colour] += int(number)
            # Use colour as the dictionary key to look up the correct colour and add the number to the dictionary count
            if color_counts['red'] > red_limit or color_counts['green'] > green_limit or color_counts['blue'] > blue_limit:
                possible = False
            # If any of the colour counts exceed the limit during a given set, set possible to False
            # If a single set of a game exceeds the count then the game was not possible

            # Check if current colour count is greater than stored color_counts_max['colour'] value
            # if so, set the color_counts_max['colour'] count to current color_counts['colour']
            if color_counts['red'] > color_counts_max['red']:
                color_counts_max['red'] = color_counts['red']

            if color_counts['green'] > color_counts_max['green']:
                color_counts_max['green'] = color_counts['green']

            if color_counts['blue'] > color_counts_max['blue']:
                color_counts_max['blue'] = color_counts['blue']

    game_power = color_counts_max['red'] * color_counts_max['blue'] * color_counts_max['green']
    # Generate the power of the game (line) by multiplying them all together
    game_powers.append(game_power)
    # Add the sum of the multiplation to a list so we can sum it later

    if possible == True:
        possible_games.append(int(game_id))
    # If the game was possible add it's game_id to a list

print(sum(possible_games))
# Answer is: 2285

print(sum(game_powers))
# Answer is: 77021






