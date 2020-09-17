import copy
x = [[1, 2, 3], [4, 5, 6]]
y = copy.deepcopy(x)
x[0][1] = 9

print(f'{x}')
print(f'{y}')
