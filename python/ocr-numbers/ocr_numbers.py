def number(num_grid):
    """Takes a list of strings representing a 7-segment number, and
    converts it to an integer string. Valid characters are underscores,
    pipes, and spaces."""

    if len(num_grid)%4 != 0:
        raise ValueError('Missing or extraneous line')

    if (any(len(elem) != len(num_grid[0]) for elem in num_grid)
            or any(len(elem)%3 != 0 for elem in num_grid)):
        raise ValueError('Malformed digits')

    grid_list = []

    for i in range(0,len(num_grid[0]),3):
        grid_list.append([line[i:i+3] for line in num_grid])

    num_string = ''

    for num in grid_list:
        num_string += num_map.get(tuple(num),'?')
    return num_string


def grid(num_string):
    """Takes an integer string, and converts it to a list of strings
    representing a 7-segment number, using underscores, pipes and
    spaces."""

    if not all(char.isdigit() for char in num_string):
        raise ValueError('Number string contains non-digit character')
    num_grid = [grid_map[char] for char in num_string]
    return [''.join(line) for line in zip(*num_grid)]

grid_map = {'0': [' _ ',
                  '| |',
                  '|_|',
                  '   '],
            '1': ['   ',
                  '  |',
                  '  |',
                  '   '],
            '2': [' _ ',
                  ' _|',
                  '|_ ',
                  '   '],
            '3': [' _ ',
                  ' _|',
                  ' _|',
                  '   '],
            '4': ['   ',
                  '|_|',
                  '  |',
                  '   '],
            '5': [' _ ',
                  '|_ ',
                  ' _|',
                  '   '],
            '6': [' _ ',
                  '|_ ',
                  '|_|',
                  '   '],
            '7': [' _ ',
                  '  |',
                  '  |',
                  '   '],
            '8': [' _ ',
                  '|_|',
                  '|_|',
                  '   '],
            '9': [' _ ',
                  '|_|',
                  ' _|',
                  '   ']}
num_map = {tuple(v): k for k, v in grid_map.items()}
