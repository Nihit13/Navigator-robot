

i = 0
a = int(i) + 1
b = int(i) + 2
c = int(i) + 3
d = int(i) + 4
e = int(i) + 5
f = int(i) + 6
g = int(i) + 7
h = int(i) + 8

values = [a,b,c,d,e,f,g,h]

map1 = [
    [h,g,f,e,d,e,f,g],
    [g,f,e,d,c,d,e,f],
    [f,e,d,c,b,c,d,e],
    [e,d,c,b,a,b,c,d],
    [d,c,b,a,i,a,b,c],
    [e,d,c,b,a,b,c,d],
    [f,e,d,c,b,c,d,e,],
    [g,f,e,d,c,d,e,f]
]

def curr(row,col):
    currentcell = map1[row][col]
    print(currentcell)
    return currentcell




def get_target_cell(row,col):
    target_cell = map1[row][col]
    return target_cell



def decode(row ,col):
    adj_cell_up = map1[row - 1][col]
    adj_cell_down = map1[row + 1][col]
    adj_cell_left = map1[row][col - 1]
    adj_cell_right = map1[row][col + 1]
    if adj_cell_right < adj_cell_left or adj_cell_right < adj_cell_down  or adj_cell_right <adj_cell_up:
        print ("Right")
        return (adj_cell_right)
    elif adj_cell_left < adj_cell_right or adj_cell_left < adj_cell_down  or adj_cell_left <adj_cell_up:
        print("Left")
        return (adj_cell_left)
    elif adj_cell_up <adj_cell_right or adj_cell_up < adj_cell_left or adj_cell_up < adj_cell_down:
        print("Up")
        return (adj_cell_up)
    elif adj_cell_down < adj_cell_left or adj_cell_down < adj_cell_right or adj_cell_down < adj_cell_up:
        print("Down")
        return (adj_cell_down)

def move(adj,current,move_cell):
    if adj < current:
        move_cell = adj
        current = move_cell
        print(current)












