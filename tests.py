import soldier

def print_matrix(field):
    for row in range(len(field)):
        for col in range(len(field[row])):
            print(field[row][col],end=" ")
        print("\n")

