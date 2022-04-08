def win_condition(locations):
    if locations[0] == locations[1] == locations[2]:
        return True
    if locations[3] == locations[4] == locations[5]:
        return True
    if locations[6] == locations[7] == locations[8]:
        return True
    if locations[0] == locations[3] == locations[6]:
        return True
    if locations[1] == locations[4] == locations[7]:
        return True
    if locations[2] == locations[5] == locations[8]:
        return True
    if locations[0] == locations[4] == locations[8]:
        return True
    if locations[6] == locations[4] == locations[2]:
        return True
    return False

def render_map():
    game_map = (f" {locations[0]} | {locations[1]} | {locations[2]}\n"
                f"---|---|---\n"
                f" {locations[3]} | {locations[4]} | {locations[5]}\n"
                f"---|---|---\n"
                f" {locations[6]} | {locations[7]} | {locations[8]}\n")
    return game_map

locations = list(range(1, 10))

turn = "x"

while turn != "game over":

    if turn == "x":
        print(render_map())

        try:
            locations[int(input("X's move, select the number you would like to mark"))-1] = "X"
        except ValueError:
            print("Invalid input. Please enter one of the numbers corresponding to the positions on the map")
            continue

        turn = "y"

        if win_condition(locations):
            print(render_map())
            print("X's Win!!!")
            turn = "game over"

    if turn =="y":
        print(render_map())

        try:
            locations[int(input("O's move, select the number you would like to mark"))-1] = "O"
        except ValueError:
            print("Invalid input. Please enter one of the numbers corresponding to the positions on the map")
            continue

        turn = "x"

        if win_condition(locations):
            print(render_map())
            print("O's Win!!!")
            turn ="game over"


