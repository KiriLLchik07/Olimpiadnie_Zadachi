
def process_movement(axis, coordinate, direction, current_pos_x, current_pos_y, current_pos_z, grid_size_n):
    if axis == "X":
        if current_pos_x == coordinate:
            if direction > 0:
                temp = current_pos_z
                current_pos_z = grid_size_n + 1 - current_pos_y
                current_pos_y = temp
            else:
                temp = current_pos_y
                current_pos_y = grid_size_n + 1 - current_pos_z
                current_pos_z = temp
    elif axis == "Y":
        if current_pos_y == coordinate:
            if direction > 0:
                temp = current_pos_z
                current_pos_z = grid_size_n + 1 - current_pos_x
                current_pos_x = temp
            else:
                temp = current_pos_x
                current_pos_x = grid_size_n + 1 - current_pos_z
                current_pos_z = temp
    elif axis == "Z":
        if current_pos_z == coordinate:
            if direction > 0:
                temp = current_pos_y
                current_pos_y = grid_size_n + 1 - current_pos_x
                current_pos_x = temp
            else:
                temp = current_pos_x
                current_pos_x = grid_size_n + 1 - current_pos_y
                current_pos_y = temp
    return current_pos_x, current_pos_y, current_pos_z

def main():
    for file_number in [f"{i:02}" for i in range(1, 21)]:
        with open(f"input_s1_{file_number}.txt") as input_file:
            expected_output = open(f"output_s1_{file_number}.txt").readline().strip()
            grid_size_n, grid_size_m = map(int, input_file.readline().split())
            current_pos_x, current_pos_y, current_pos_z = map(int, input_file.readline().split())

            for _ in range(grid_size_m):
                axis, coordinate, direction = input_file.readline().split()
                coordinate, direction = int(coordinate), int(direction)
                current_pos_x, current_pos_y, current_pos_z = process_movement(axis, coordinate, direction, current_pos_x, current_pos_y, current_pos_z, grid_size_n)

            print(f"Current position: {current_pos_x} {current_pos_y} {current_pos_z}")
            if f"{current_pos_x} {current_pos_y} {current_pos_z}" == expected_output:
                print("Result: True")
            else:
                print("Result: False")

if __name__ == "__main__":
    main()

