pos = input()
x, y = int(pos[1]), ord(pos[0])
move_type = [(-1, -2), (1, -2), (-1, 2), (1, 2), (-2, -1), (-2, 1), (2, -1), (2, 1)]
count = 0

for move in move_type:
    if (1 <= x + move[0] <= 8 and ord('a') <= y + move[1] <= ord('h')):
        count += 1
        
print(count)
