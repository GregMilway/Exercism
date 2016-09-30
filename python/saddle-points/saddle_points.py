# find saddle points in a matrix.
# a saddle point occurs when a given element is greater than or equal to all elements in its' row,
# and less than or equal to all elements in its' column.

def saddle_points(matrix):
    points = set()
    if matrix == []:
        return points
    if any([len(row) != len(matrix[0]) for row in matrix]):
        raise ValueError('Matrix must be square')
    m_cols = map(list, zip(*matrix))
    rows = len(matrix)
    cols = len(matrix[0])
    for i in range(rows):
        for j in range(cols):
            cand = matrix[i][j]
            if cand == max(matrix[i]) and cand == min(m_cols[j]):
                points.add((i,j))
    return points

