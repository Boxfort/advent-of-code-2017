def construct_spiral(size):
    spiral = []
    x = 0
    y = 0
    direction = 1
    length = 1
    steps = 0

    for i in range(1, size+1):
        spiral.append((x, y))

        if steps >= length:
            x = x + direction
        else:
            y = y + direction

        steps = steps + 1

        if steps == (length * 2):
            steps = 0
            length = length + 1
            direction = direction * -1

    return spiral

def get_distance(node):
    return (abs(node[0]) + abs(node[1]))

if __name__ == '__main__':
    spiral = construct_spiral(361527)
    distance = get_distance(spiral[361526])
    print distance
