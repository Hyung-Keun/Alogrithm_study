def generate(numRows):

    pascal = [[1], [1, 1]]
    if numRows <= 2:
        if numRows == 0:
            return pascal
        elif numRows == 1 or numRows < 0:
            return pascal[:1]
    # print(pascal)
    for _ in range(3, numRows + 1):
        li = [1]

        for n in range(1, len(pascal[-1]) + 1):
            li.append(sum(pascal[-1][n - 1:n + 1]))
        pascal.append(li)
    return pascal

numRows = 5
print(generate(numRows))





