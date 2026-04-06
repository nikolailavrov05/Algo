def k_min(matrix, k):
    n = len(matrix)
    left = matrix[0][0]
    right = matrix[n - 1][n - 1]
    while left <= right:
        mid = (left + right) // 2
        counter = 0
        row = n - 1
        collomn = 0
        while row >= 0 or collomn < n:
            if matrix[row][collomn] <= mid:
                counter += row
                collomn += 1
            else:
                row -= 1
        if counter < k:
            left = mid + 1
        else:
            right = mid - 1
    return right


matrix = [[1, 5, 9, 11], [2, 6, 10, 12],
          [3, 7, 13, 14], [4, 8, 15, 16]]

print(k_min(matrix, 7))
