import sys

empty = '.'

def find_location(size, point):
    return add_tuples(generate_spiral(size, find=point), (1, 1))[::-1]

def find_point(size, x, y):
    return generate_spiral(size)[(y-1,x-1)]

def print_spiral(spiral, size):
    for x in range(size):
        for y in range(size):
            print '%2s' % spiral[(x,y)], 
        print ""

def add_tuples(a, b):
    return tuple(map(sum, zip(a, b)))

def generate_spiral(size, find=None):
    # spiral grid
    spiral = dict(((i,j), empty) for i in range(size) for j in range(size))
    
    # start at center of spiral
    curr = (size/2-1, size/2)

    # start in right direction, right, up, left, down
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    d = 0 

    # add point by point
    for p in range(1, size**2+1):
        new_d = (d + 1) % len(directions)

        # if spiral can turn at given direction, turn
        turn = add_tuples(curr, directions[new_d])

        if turn in spiral and spiral[turn] == empty:
            spiral[turn] = p 
            # update direction
            d = new_d
            curr = turn

        # else, just go ahead and maintain direction
        else:
            ahead = add_tuples(curr,directions[d])
            spiral[ahead] = p
            curr = ahead

        # if p is find: 
        #     return curr
            # return  curr

    
    # print_spiral(spiral, size)
    return spiral

# num_args = len(sys.argv) - 1
# size = sys.argv[1]

# if num_args == 2:
#   print generate_spiral(size)
#   find_location(sys.argv[2])
# elif num_args == 3:
#   find_point(sys.argv[2], sys.argv[3])