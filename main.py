import re
SPACES = 3
TRANSITIONS = {
        "A": 0,
        "B": 1,
        "C": 2
    }


def get_board(positions):
    string = "   A|B|C\n"
    for j in range(len(positions)):
        string += f"{j+1}. "
        for i in range(len(positions[j])):
            if i % 2 == 1:
                string += f"|{positions[j][i]}|"
            else:
                string += positions[j][i]
        if j != len(positions) - 1:
            string += "\n   -----\n"

    return string


def real_coordinate(text):
    pattern = r'^[a-cA-C][1-3]$'
    if re.match(pattern, text):
        return True
    return False


def play(positions):
    for i in range(len(positions)):
        xs = os = 0
        for j in range(len(positions[i])):
            if positions[i][j] == "X":
                xs += 1
            elif positions[i][j] == "O":
                os += 1
        if xs == SPACES:
            print("Player X Won")
            return False
        elif os == SPACES:
            print("Player O Won")
            return False

    for col in range(len(positions[0])):
        column = [positions[row][col] for row in range(len(positions))]
        if column[0] != " " and all(cell == column[0] for cell in column):
            print(f"Player {column[0]} won!")
            return False

    if all(positions[i][i] == positions[0][0] and positions[0][0] != " " for i in range(SPACES)):
        print(f"Player {positions[0][0]} won!")
        return False

    if all(positions[i][SPACES - i - 1] == positions[0][SPACES - 1] and positions[0][SPACES - 1] != " " for i in range(SPACES)):
        print(f"Player {positions[0][SPACES - 1]} won!")
        return False

    return True


def main():
    free_spaces = SPACES**2
    tura = 0
    used = []
    positions = [[" " for _ in range(SPACES)] for _ in range(SPACES)]

    while free_spaces and play(positions):
        if tura % 2 == 0:
            player = "O"
        else:
            player = "X"
        tura += 1
        print(f"\r{get_board(positions=positions)}")
        coordinates = ""
        while not real_coordinate(coordinates) or coordinates.upper() in used:
            coordinates = input(f"Player {player}, Enter coordinates eg \"A2\"").strip()

        positions[int(list(coordinates)[1])-1][TRANSITIONS[list(coordinates)[0].upper()]] = player
        used.append(coordinates.upper())
        free_spaces -= 1

    if free_spaces == 0:
        print("DRAW")


if __name__ == "__main__":
    main()
