if __name__ == "__main__":
    total_weights = 10
    cols = total_weights + 1
    weights = [1,2,4,2,5]
    values = [5,3,5,3,2]
    rows = len(values)

    matrix = [[0]*cols for i in range(rows)]
    i = 0
    j = 0
    while i < rows:
        while j < cols:
            if j == 0:
                matrix[i][j] = 0

            elif i == 0:
                matrix[i][j] = values[i]
                
            else:
                if weights[i] <= j:
                    matrix[i][j] = max(values[i] + matrix[i-1][j-weights[i]], matrix[i-1][j])
                else:
                    matrix[i][j] = matrix[i-1][j]

            j += 1

        i += 1
        j = 0

    print(matrix[i-1][j-1])

    for row in matrix:
        string = ''
        for col in row:
            string += str(col) + '\t'
        print(string)
		
				 
