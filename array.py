

# Arrays

def hello():
    print('hello')
    print(join_string(['bob', 'joe']))
    game_entry = GameEntry('bob', 100)
    print(game_entry.get_name())
    print(game_entry.get_score())


def join_string(words: list):
    new_word = ''
    new_word = ' '.join(words)
    return new_word


def main():
    hello()

    # Create 2D list
    multidim_list = [[0] * 2 for j in range(3)]
    print(multidim_list)
    # Create tic-tac-toe board
    board = [[' '] * 3 for i in range(3)]
    print(board)
    # String representation of board
    rows = ['|'.join(board[i]) for i in range(3)]
    print(rows)
    display = '\n-----\n'.join(rows)
    print(display)

class GameEntry:
    """Represents the entry of a list of high scores"""

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_name(self):
        return self.name

    def get_score(self):
        return self.score

    # Return string representation
    def __str__(self):
        return f'{self.name}, {self.score}'


if __name__ == '__main__':
    main()

