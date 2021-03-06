# read blueprint from file
def expand_haus(blueprint):
    frame = get_frame(blueprint)
    expanded = []
    for r in range(len(frame)):
        row = frame[r]
        erow = []
        ewalls = []
        for c in range(len(row)):
            room = row[c]
            ceiling = ''
            wall = ''            
            # if has room
            if room == '*':
                # if has previous room
                if c-1 >= 0 and row[c-1] == '*':
                    ceiling += '-'
                    wall += '|'
                else:
                    ceiling += '+'
                    wall += ' '
               
                # if has floor below
                if r+1 < len(frame) and frame[r+1][c] == '*':
                    ceiling += '  '
                    wall += '   '
                else:
                    ceiling += '---'
                    wall += '   '

                # if has next room
                if c+1 < len(row) and row[c+1] == '*':
                    ceiling += '-'
                    wall += ' '
                else:
                    ceiling += '+'
                    wall += '|'
                
                erow.append(ceiling)
                ewalls.append(wall)
            # if no room, empty space
            else:
                erow.append('     ')
                ewalls.append('     ')

        expanded.append(erow)
        expanded.append(ewalls)
        expanded.append(erow)
    print_haus(expanded)
    return expanded

def print_haus(haus):
    for row in haus:
        for col in row:
            print(col, end="")
        print()

def get_frame(blueprint):
    frame = [list(c) for c in [r for r in blueprint.split('\n') if len(r) > 0]]
    return frame

def test():
    f = open('blueprint.txt')
    blueprint = f.read()
    b1 = '*'
    b2 = ' *\n**'
    assert get_frame(b1) == [['*']]
    assert get_frame(b2) == [[' ', '*'], ['*', '*']]

    print('tests pass')
