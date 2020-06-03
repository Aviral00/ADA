# BRUTE FORCE METHOD#

# Importing time for delay
import time
import datetime

# Defined a function with 2 matrix as a parameters.
# real_matrix is the matrix for which we want transformation.
# resultant_matrix is the matrix for which we want to check
# if that is transformable by row and column exchange of real_matrix.


def is_transformable(real_matrix, resultant_matrix):

    # First for loop which will repeat loop for len(real_matrix) to find desired results.
    for i in range(0, len(real_matrix)):

        # Second for loop which will check entire row or column.
        for j in range(0, len(real_matrix)):

            # Third for loop which will check each element of that row or column.
            for k in range(0, len(real_matrix)):

                # Will find row in resultant_matrix, where element of each row,first column from real_matrix is present.
                if real_matrix[i][0] == resultant_matrix[j][k]:

                    # Created a list which will have elements of the ith row from real_matrix.
                    b = []

                    # Repeat the loop for len(real_matrix) times.
                    for m in range(0, len(real_matrix)):

                        # Append element of ith row from real_matrix in list b.
                        b.append(real_matrix[i][m])

                    # Repeat the loop for len(real_matrix) times.
                    for n in range(0, len(real_matrix)):

                        # Check if jth row of of resultant_matrix is having all elements as in list b.
                        if resultant_matrix[j][n] in b:

                            # Sleep for 0.1 milliseconds.
                            time.sleep(0.1)
                            continue

                        # If any element is not found then function will return False.
                        else:
                            return False

                # Will find row in resultant_matrix, where element of each column,first row from real_matrix is present.
                if real_matrix[0][i] == resultant_matrix[j][k]:

                    # Created a list which will have elements of the ith column from real_matrix.
                    b = []

                    # Repeat the loop for len(real_matrix) times.
                    for m in range(0, len(real_matrix)):

                        # Append element of ith column from real_matrix in list b.
                        b.append(real_matrix[m][i])

                    # Repeat the loop for len(real_matrix) times.
                    for n in range(0, len(real_matrix)):

                        # Check if kth row of of resultant_matrix is having all elements as in list b.
                        if resultant_matrix[n][k] in b:

                            # Sleep for 0.1 milliseconds.
                            time.sleep(0.1)
                            continue

                        # If any element is not found then function will return False.
                        else:
                            return False

    # If all processes completed successfully then the function will return True.
    return True


print("Input the order of squared matrix")

# Takes order of matrix as input.
m = int(input())

# Assigns 0 for all elements of real_matrix.
real_matrix = [[0 for i in range(m)] for j in range(m)]

# Assign 0 for all elements of resultant_matrix.
resultant_matrix = [[0 for i in range(m)] for j in range(m)]

print("Input the elements of REAL MATRIX")
# Takes input for all elements of real_matrix.
for i in range(0, m):
    for j in range(0, m):

        real_matrix[i][j] = int(input())

print("Input the elements of RESULTANT MATRIX")
# Takes input for all elements of resultant_matrix.
for i in range(0, m):
    for j in range(0, m):
        resultant_matrix[i][j] = int(input())

# Computes time taken for execution.
begin_time = datetime.datetime.now()

# Calls the function, takes the arguments as real_matrix, resultant_matrix and prints result.
print(is_transformable(real_matrix, resultant_matrix))












