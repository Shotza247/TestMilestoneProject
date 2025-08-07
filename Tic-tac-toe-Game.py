# Global variables
board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
player_symbols = ["X", "O"]
scores = {"Player 1": 0, "Player 2": 0}

def display_game():
    for i in range(0, 9, 3):
        print(f"|{board[i]}\t|{board[i+1]}\t{board[i+2]}|")

def select_position(player):
    while True:
        pos_input = input(f"{player}, enter your next position (1-9): ")
        if pos_input.isdigit():
            position = int(pos_input)
            if position in range(1, 10) and board[position - 1] not in ["X", "O"]:
                return position
            else:
                print("Position already taken or invalid. Try again.")
        else:
            print("Invalid input. Please enter a number between 1 and 9.")

def replace_position(position, symbol):
    board[position - 1] = symbol

def check_win(symbol):
    win_combos = [
        [0,1,2], [3,4,5], [6,7,8], # rows
        [0,3,6], [1,4,7], [2,5,8], # columns
        [0,4,8], [2,4,6]           # diagonals
    ]
    return any(all(board[i] == symbol for i in combo) for combo in win_combos)

def check_draw():
    return all(space in ["X", "O"] for space in board)

def play_game():
    global board
    board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    current_player = 0
    display_game()
    while True:
        player_name = f"Player {current_player + 1}"
        symbol = player_symbols[current_player]
        position = select_position(player_name)
        replace_position(position, symbol)
        display_game()
        if check_win(symbol):
            print(f"{player_name} ({symbol}) wins!")
            scores[player_name] += 1
            break
        if check_draw():
            print("It's a draw!")
            break
        current_player = 1 - current_player  # Switch player

def show_scores():
    print("\nScoreboard:")
    for player, score in scores.items():
        print(f"{player}: {score}")

def main():
    print("Welcome to Tic-Tac-Toe!")
    print(f"player 1 is '{player_symbols[0]}' and player 2 is '{player_symbols[1]}'")
    while True:
        play_game()
        show_scores()
        again = input("Do you want to play again? (yes/no): ").strip().lower()
        if again != "yes":
            print("Final scores:")
            show_scores()
            print("Thanks for playing!")
            # Reset everything for a new session
            scores["Player 1"] = 0
            scores["Player 2"] = 0
            break

if __name__ == "__main__":
    main()