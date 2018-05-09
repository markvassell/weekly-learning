
def complete_transaction(matrix, i, j, prices):

    best_sol = 0
    tracker = 0

    while tracker < j:
        if best_sol < (prices[j] - prices[tracker] + matrix[i-1][tracker]):
            best_sol = prices[j] - prices[tracker] + matrix[i-1][tracker]
        tracker += 1

    print('\n\n')

    return best_sol



def display_matrix(matrix, rows, cols):
    print('\nNew Matrix\n')
    i, j = 0, 0
    while i < rows:
        string = ''
        while j < cols:
            string += str(matrix[i][j]) + '\t'
            j+= 1
        j = 0
        i += 1
        print(string)


def build_matrix(matrix, rows, cols, prices):
    i = 1
    j = 1
    while i < rows:
        while j < cols:
            matrix[i][j] = max(matrix[i][j-1], # not making a transaction on the current day
                               complete_transaction(matrix, i, j, prices) # completing a transaction on the current day
                               )
            j += 1
        display_matrix(matrix, rows, cols)
        j = 1
        i += 1

def main():
    prices = [2, 5, 7, 1, 4, 3, 1, 3]
    trans = 3
    rows = trans + 1
    cols = len(prices)

    matrix = [[0] * cols for i in range(rows)]

    display_matrix(matrix, rows, cols)
    build_matrix(matrix, rows, cols, prices)
if __name__ == '__main__':
    main()




