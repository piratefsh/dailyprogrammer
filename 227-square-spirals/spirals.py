import math

def nearest_sqrt(n):
  counter = 0
  while True:
    counter += 1

    if counter * counter > n:
      return counter - 1

def make_spiral(size, target_num=None, target_cell=None):
  grid = [[None] * size for i in range(size)]
  directions =[(1, 0), (0, 1), (-1, 0), (0, -1)]

  # flip index
  if target_cell is not None:
    target_cell = (size - target_cell[0], size - target_cell[1])

  currd = 0
  currp = (0, 0)
  center = (math.floor(size/2), math.floor(size/2))

  counter = size*size + 1
  while counter > 1:
    counter -= 1
    x, y = currp

    if target_num is not None and counter == target_num:
      return (size - x, size - y)
    if target_cell is not None and currp == target_cell:
      return counter

    grid[y][x] = counter

    # if next does not exist or occupied, change dir
    vx, vy = directions[currd]
    nx, ny = vx + x, vy + y

    if nx < 0 or nx >= size or ny < 0 or ny >= size or grid[ny][nx] is not None:
      currd = (currd + 1) % len(directions)

    vx, vy = directions[currd]
    currp = (x + vx, y + vy)

  return grid

def pprint(grid):
  for row in grid:
    for col in row:
      print("{:0>2d} ".format(col), end=" ")
    print()

res = make_spiral(5)
assert(make_spiral(3, target_num=8) == (2, 3))
assert(make_spiral(7, target_cell=(1,1)) == 37)
assert(make_spiral(9, target_cell=(6,8)) == 47)
# assert(make_spiral(1024716039, target_num=557614022) == (512353188, 512346213))
# assert(make_spiral(234653477, target_cell=(11777272, 289722)) == 54790653381545607)
assert(nearest_sqrt(26)  == 5)
assert(nearest_sqrt(9)  == 3)
assert(nearest_sqrt(10)  == 3)
pprint(res)
print('tests pass')