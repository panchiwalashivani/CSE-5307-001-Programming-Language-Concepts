"""
Name: Shivani Panchiwala
StudentID: 1001982478
Date: 04/14/2023
OS: Windows 11
Python Version: 3.11.3
"""
import random
import math as m


def create_gap(space):
    gap_str = ''
    while space > 0:
        gap_str += ' '
        space -= 1
    return gap_str


def initialize_program():
    print(create_gap(28) + 'AMAZING PROGRAM')
    print(create_gap(15) + 'CREATIVE COMPUTING MORRISTOWN, NEW JERSEY')
    print('\n')

    # new_width, new_length = 10, 10

    # print(new_width, new_length)
    new_width, new_length = get_user_input()
    while new_width <= 1 or new_length <= 1:
        print('Meaningles Dimensions. Try Again.')
        new_width, new_length = get_user_input()
    return new_width, new_length


def get_user_input():
    user_input = input('WHAT ARE YOUR WIDTH AND LENGTH? (FOR EXAMPLE TYPE 10,10 AND PRESS ENTER)\n')
    new_width, new_length = user_input.split(',')
    new_width, new_length = int(new_width), int(new_length)
    return new_width, new_length


def initialize_arrays(horizontal_size, vertical_size):
    array_w, array_v = [], []
    array_w.append([None] * vertical_size)
    array_v.append([None] * vertical_size)
    i = 1
    while i <= horizontal_size:
        array_w.append([])
        array_v.append([])
        j = 1
        array_w[i].append(None)
        array_v[i].append(None)
        while j <= vertical_size:
            array_w[i].append(0)
            array_v[i].append(0)
            j += 1
        i += 1

    return array_w, array_v


def print_first_line(x_pos, horizontal_size):
    line_str = ''
    i = 1
    while i <= horizontal_size:
        if i == x_pos:
            line_str += '.  '
        else:
            line_str += '.--'
        i += 1
    # line_str += '.\n'
    line_str += '.'
    print(line_str)


def search_unexplored_cell(row_pos, horizontal_size, column_pos, vertical_size):
    if row_pos < horizontal_size:
        row_pos += 1
    elif column_pos < vertical_size:
        row_pos = 1
        column_pos += 1
    else:
        row_pos, column_pos = 1, 1

    return row_pos, column_pos


def explore_maze(
    x,
    w,
    v,
    h,
    v2,
    ):

    (q, z) = (0, 0)
    c = 1
    w[x][1] = c
    c += 1
    (r, s) = (x, 1)
    entry = 0

    while True:
        if entry == 2:
            (r, s) = search_unexplored_cell(r, h, s, v2)
            while w[r][s] == 0:
                (r, s) = search_unexplored_cell(r, h, s, v2)

        if entry == 0 and r - 1 > 0 and w[r - 1][s] == 0:

            if s - 1 > 0 and w[r][s - 1] == 0:
                if r < h and w[r + 1][s] == 0:
                    x = m.floor(random.random() * 3 + 1)
                elif s < v2:
                    if w[r][s + 1] == 0:
                        x = m.floor(random.random() * 3 + 1)
                        if x == 3:
                            x = 4
                    else:
                        x = m.floor(random.random() * 2 + 1)
                elif z == 1:
                    x = m.floor(random.random() * 2 + 1)
                else:
                    q = 1
                    x = m.floor(random.random() * 3 + 1)
                    if x == 3:
                        x = 4
            elif r < h and w[r + 1][s] == 0:
                if s < v2:
                    if w[r][s + 1] == 0:
                        x = m.floor(random.random() * 3 + 1)
                    else:
                        x = m.floor(random.random() * 2 + 1)
                    if x >= 2:
                        x += 1
                elif z == 1:
                    x = m.floor(random.random() * 2 + 1)
                    if x >= 2:
                        x += 1
                else:
                    q = 1
                    x = m.floor(random.random() * 3 + 1)
                    if x >= 2:
                        x += 1
            elif s < v2:
                if w[r][s + 1] == 0:
                    x = m.floor(random.random() * 2 + 1)
                    if x == 2:
                        x = 4
                else:
                    x = 1
            elif z == 1:
                x = 1
            else:
                q = 1
                x = m.floor(random.random() * 2 + 1)
                if x == 2:
                    x = 4
        elif s - 1 > 0 and w[r][s - 1] == 0:
            if r < h and w[r + 1][s] == 0:
                if s < v2:
                    if w[r][s + 1] == 0:
                        x = m.floor(random.random() * 3 + 2)
                    else:
                        x = m.floor(random.random() * 2 + 2)
                elif z == 1:
                    x = m.floor(random.random() * 2 + 2)
                else:
                    q = 1
                    x = m.floor(random.random() * 3 + 2)
            elif s < v2:
                if w[r][s + 1] == 0:
                    x = m.floor(random.random() * 2 + 2)
                    if x == 3:
                        x = 4
                else:
                    x = 2
            elif z == 1:
                x = 2
            else:
                q = 1
                x = m.floor(random.random() * 2 + 2)
                if x == 3:
                    x = 4
        elif r < h and w[r + 1][s] == 0:

            if s < v2:
                if w[r][s + 1] == 0:
                    x = m.floor(random.random() * 2 + 3)
                else:
                    x = 3
            elif z == 1:
                x = 3
            else:
                q = 1
                x = m.floor(random.random() * 2 + 3)
        elif s < v2:
            if w[r][s + 1] == 0:
                x = 4
            else:
                entry = 2
                continue
        elif z == 1:
            entry = 2  # Blocked
            continue
        else:
            q = 1
            x = 4

        if x == 1:
            w[r - 1][s] = c
            c += 1
            v[r - 1][s] = 2
            r -= 1
            if c == h * v2 + 1:
                break
            q = 0
            entry = 0
        elif x == 2:
            w[r][s - 1] = c
            c += 1
            v[r][s - 1] = 1
            s -= 1
            if c == h * v2 + 1:
                break
            q = 0
            entry = 0
        elif x == 3:
            w[r + 1][s] = c
            c += 1
            if v[r][s] == 0:
                v[r][s] = 2
            else:
                v[r][s] = 3
            r += 1
            if c == h * v2 + 1:
                break
            entry = 1
        elif x == 4:
            if q != 1:
                w[r][s + 1] = c
                c += 1
                if v[r][s] == 0:
                    v[r][s] = 1
                else:
                    v[r][s] = 3
                s += 1
                if c == h * v2 + 1:
                    break
                entry = 0
            else:
                z = 1
                if v[r][s] == 0:
                    v[r][s] = 1
                    q = 0
                    r = 1
                    s = 1
                    while w[r][s] == 0:
                        if r < h:
                            r += 1
                        elif s < v2:
                            r = 1
                            s += 1
                        else:
                            r = 1
                            s = 1
                    entry = 0
                else:
                    v[r][s] = 3
                    q = 0
                    entry = 2

    return v



def print_maze(v, h, v2):
    j = 1
    while j <= v2:
        st = 'I'
        i = 1
        while i <= h:
            if v[i][j] < 2:
                st += '  I'
            else:
                st += '   '
            i += 1

        print(st)

        st = ''
        i = 1
        while i <= h:
            if v[i][j] == 0 or v[i][j] == 2:
                st += ':--'
            else:
                st += ':  '
            i += 1
        print(st + '.')
        j += 1


def main():
    h, v2 = initialize_program()
    w, v = initialize_arrays(h, v2)

    x = m.floor(random.random() * h + 1)
    print_first_line(x, h)

    v = explore_maze(x, w, v, h, v2)

    print_maze(v, h, v2)


if __name__ == '__main__':
    main()





