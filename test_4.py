# Citation: ChatGPT

import re


def extract_vowels(word):
    """Extract vowels from a word."""
    return re.findall(r'[aeiou]', word.lower())


def check_six_eight_poem(poem):
    lines = poem.split('\n')

    # Check for an odd number of sentences
    if len(lines) % 2 != 0:
        return 0

    # Initialize previous vowels for comparison
    previous_vowels = None

    # Check for alternating line lengths and rhyming
    for i, line in enumerate(lines):
        words = line.split()
        if len(words) == 0:  # skip empty lines
            continue

        # Extract vowels from the relevant word (6th or 8th word)
        if i % 2 == 0:  # 6-word line
            if len(words) != 6:
                return i + 1
            relevant_word = words[5]
        else:  # 8-word line
            if len(words) != 8:
                return i + 1
            relevant_word = words[5]

        vowels = extract_vowels(relevant_word)

        # Compare vowels for rhyme rule
        if previous_vowels is not None and vowels != previous_vowels:
            return i + 1

        # Update previous vowels for next comparison
        previous_vowels = vowels

        # If it's a single pair of lines and the rhyme is correct, return -1
        if i == 1 and previous_vowels is not None:
            return -1

    # The poem is a correct six-eight poem
    return -1


def move(current_state, position, direction, key):
    rows = len(current_state)
    cols = len(current_state[0])
    row, col = position

    # Determine the new direction based on the current direction and key pressed
    if direction == "left" and key != "right":
        direction = key
    elif direction == "right" and key != "left":
        direction = key
    elif direction == "up" and key != "down":
        direction = key
    elif direction == "down" and key != "up":
        direction = key

    # Move the snake based on the direction
    if direction == "left":
        col -= 1
    elif direction == "right":
        col += 1
    elif direction == "up":
        row -= 1
    elif direction == "down":
        row += 1

    # Check if the snake has hit the wall or itself
    if row < 0 or row >= rows or col < 0 or col >= cols or current_state[row][col] == "x":
        status = "killed"
    else:
        # Update the position of the snake
        current_state[row][col] = "x"
        position = [row, col]
        status = "alive"

    return [current_state, position, direction, status]
