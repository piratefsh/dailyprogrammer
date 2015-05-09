import random, math, time, sys
size = 30
track_a = [' '] * size
track_b = [' '] * size
track_a[0] = 'a'
track_b[0] = 'b'

def roll():
    return int(math.floor(random.random() * 6 + 1))

def track_str(track):
    t = '|'
    for slot in track:
        t += slot + '|'
    return t + '\n'

def print_tracks(tracks):
    all_tracks = ''
    for t in tracks:
        all_tracks += track_str(t)
    sys.stdout.write("\033[F\033[F")
    print(all_tracks,  end='\r\r')

def move(track, steps, char):
    curr = track.index(char)
    track[curr] = ' '
    if (curr + steps) < len(track):
        track[curr + steps] = char 
        return True
    else:
        track[len(track) - 1] = char 
        return False

print("\n")
winner = ''
while True:
    print_tracks([track_a, track_b])
    if not move(track_a, roll(), 'a'):
        winner = 'a'
        break
    if not move(track_b, roll(), 'b'):
        winner = 'b'
        break
    time.sleep(1)

print_tracks([track_a, track_b])
print('%s wins!' % winner)
