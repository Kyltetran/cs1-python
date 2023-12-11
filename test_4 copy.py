def check_six_eight_poem(poem):
    def find_rhyme(word):
        for i in range(len(word)):
            if word[i] in 'aeiouy':
                return word[i:]

    def check_rhyme(word1, word2):
        return find_rhyme(word1) == find_rhyme(word2)

    sentences = poem.split('\n')

    # Check for odd number of sentences
    if len(sentences) % 2 != 0:
        return 0

    # Check the rhyme rule
    for i in range(0, len(sentences), 2):
        six_word_sentence = sentences[i].split()
        eight_word_sentence = sentences[i + 1].split()

        # Check if the sixth word of the six-word sentence rhymes with the sixth word of the eight-word sentence
        if not check_rhyme(six_word_sentence[5], eight_word_sentence[5]):
            return i + 2

        # Check if the eighth word of the eight-word sentence rhymes with the sixth word of the next six-word sentence
        if i + 2 < len(sentences):
            next_six_word_sentence = sentences[i + 2].split()
            if not check_rhyme(eight_word_sentence[7], next_six_word_sentence[5]):
                return i + 3
    # Correct six-eight poem format
    return -1

# Question 2 is from here


def _find_tail(game_state, head):
    game = game_state.copy()
    for i in range(len(game_state)):
        game[i] = game_state[i].copy()
    game[head[0]][head[1]] = ""
    # print([head, game])

    if head[0] + 1 < len(game) and game[head[0] + 1][head[1]] == "x":
        return _find_tail(game, [head[0] + 1, head[1]])
    elif head[0] >= 1 and game[head[0] - 1][head[1]] == "x":
        return _find_tail(game, [head[0] - 1, head[1]])
    elif head[1] + 1 < len(game[0]) and game[head[0]][head[1] + 1] == "x":
        return _find_tail(game, [head[0], head[1] + 1])
    elif head[1] >= 1 and game[head[0]][head[1] - 1] == "x":
        return _find_tail(game, [head[0], head[1] - 1])
    else:
        return head


def find_tail(game_state, head, current_direction):
    game = game_state.copy()
    for i in range(len(game_state)):
        game[i] = game_state[i].copy()
    game[head[0]][head[1]] = ""
    if current_direction == "up":
        return _find_tail(game, [head[0] + 1, head[1]])
    elif current_direction == "down":
        return _find_tail(game, [head[0] - 1, head[1]])
    elif current_direction == "left":
        return _find_tail(game, [head[0], head[1] + 1])
    else:
        return _find_tail(game, [head[0], head[1] - 1])


def move(game_state, head_position, current_direction, user_key):
    def is_valid_move(pos):
        return 0 <= pos[0] < len(game_state) and 0 <= pos[1] < len(game_state[0])

    def is_collision(pos):
        return game_state[pos[0]][pos[1]] == "x"

    def update_position(pos, direction, user_key):
        if (direction == "up" and user_key != "left" and user_key != "right") \
                or (user_key == "up" and direction != "down"):
            return "up", [pos[0] - 1, pos[1]]
        elif (direction == "down" and user_key != "left" and user_key != "right") \
                or (user_key == "down" and direction != "up"):
            return "down", [pos[0] + 1, pos[1]]
        elif (direction == "left" and user_key != "up" and user_key != "down") \
                or (user_key == "left" and direction != "right"):
            return "left", [pos[0], pos[1] - 1]
        elif (direction == "right" and user_key != "up" and user_key != "down") \
                or (user_key == "right" and direction != "left"):
            return "right", [pos[0], pos[1] + 1]

    new_direction, new_head = update_position(
        head_position, current_direction, user_key)

    if not is_valid_move(new_head) or is_collision(new_head):
        return [game_state, head_position, new_direction, "killed"]
    else:
        tail_pos = find_tail(game_state, head_position, current_direction)
        # print(tail_pos)
        game_state[new_head[0]][new_head[1]] = "x"
        game_state[tail_pos[0]][tail_pos[1]] = ""
        return [game_state, new_head, new_direction, "alive"]


# Test cases
game_state1 = [["", "", "", "", ""], ["", "x", "x", "x", ""], [
    "", "x", "", "x", ""], ["", "x", "x", "x", ""], ["", "", "", "", ""]]
head_position1 = [1, 2]
current_direction1 = "right"
user_key1 = "left"
# print(move(game_state1, head_position1, current_direction1, user_key1))
#
game_state1 = [["", "", "", "", ""], ["", "x", "x", "x", ""], [
    "", "x", "", "x", ""], ["", "x", "x", "x", ""], ["", "", "", "", ""]]
head_position1 = [3, 3]
current_direction1 = "right"
user_key1 = "right"
# print(move(game_state1, head_position1, current_direction1, user_key1))
