def score(game):
    result = 0
    frame = 0
    for roll in range(len(game)):
        if frame < 10:
            if game[roll] == '/':
                result += get_value(game[roll+1])
            elif game[roll] == 'X' or game[roll] == 'x':
                result += 10 + get_value(game[roll +2])+ get_value(game[roll+1])
            else:
                result += get_value(game[roll+1]) + get_value(game[roll+2])
            frame += 1

    return result


def get_value(char):
    if char == 'X' or char == 'x':
        return 10
    elif char == '/':
        return 10
    elif char == '-':
        return 0
    if 1 <= int(char) <= 9:
        return int(char)
    else:
        raise ValueError()
