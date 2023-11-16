from math import lcm

def print_matrix(matrix):
    print("")
    for i in range(len(matrix)):
        line = ""
        for z in range(len(matrix [0])):
            line += f"{matrix [i] [z]}\t"
        print(line)
    print("")

def gaussian_eliminate(matrix):
    for i in range(len(matrix)):
        for z in range(i + 1, len(matrix)):
            if matrix [z] [i] != 0:
                lcm_required = lcm(int(matrix [z] [i]), int(matrix [i] [i]))
                matrix [z] = [((lcm_required / matrix [z] [i]) * matrix [z] [index]) - ((lcm_required / matrix [i] [i]) * matrix [i] [index]) for index in range(len(matrix [i]))]
    
    return matrix



print("Consider Ax = b")

# inputting matrix A

n = int(input("Enter the size of matrix A: "))

print("Inputting matrix A...")
matrix_a = [['x' for _z in range(n)] for _i in range(n)]

for i in range(n):
    for z in range(n):
        matrix_a [i] [z] = '_'
        print_matrix(matrix_a)
        matrix_a [i] [z] = int(input(f"Enter matrix A element ({i}, {z}): "))
        print("")

print("Final matrix A:")
print_matrix(matrix_a)

# inputting matrix B

print("\nInputting matrix B...")
matrix_b = [['x'] for _i in range(n)]

for i in range(n):
    matrix_b[i] [0] = '_'
    print_matrix(matrix_b)
    matrix_b [i] [0] = int(input(f"Enter matrix B element ({i}, 0): "))
    print("")

print("Final matrix B:")
print_matrix(matrix_b)

# determining solutions

echelon_augmented_matrix = gaussian_eliminate([matrix_a [index] + matrix_b [index] for index in range(n)])

last_row_index = len(echelon_augmented_matrix) - 1
last_col_index = len(echelon_augmented_matrix [0]) - 1

if echelon_augmented_matrix [last_row_index] [last_col_index] == 0 and echelon_augmented_matrix [last_row_index] [last_col_index - 1] == 0:
    print("Infinite solutions")
elif echelon_augmented_matrix [last_row_index] [last_col_index] != 0 and echelon_augmented_matrix [last_row_index] [last_col_index - 1] == 0:
    print("No solutions")
else:
    print("Solutions exist, matrix X:")
    matrix_x = [[0] for _i in range(n)]

    for i in range(n):
        other_solutions = matrix_x [:]
        other_solutions [last_row_index - i] [0] = 0
        sum_of_other_solutions = sum([(other_solutions [index] [0] * echelon_augmented_matrix [last_row_index - i] [index])for index in range(len(other_solutions))])
        
        matrix_x [last_row_index - i] [0] = (echelon_augmented_matrix [last_row_index - i] [last_col_index] - sum_of_other_solutions) / echelon_augmented_matrix [last_row_index - i] [last_col_index - i - 1]

    print_matrix(matrix_x)