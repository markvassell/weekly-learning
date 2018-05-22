dollar_amount = 45
change_amounts = [1,2,3,7,5,12]
rows = len(change_amounts)
cols = dollar_amount + 1
matrix = [0]*cols
matrix[0] = 1

for data in change_amounts:
    temp = data
    while temp < cols:
        matrix[temp] += matrix[temp - data]
        temp += 1

print(matrix)
my_dict = {}
print(my_dict[2])



