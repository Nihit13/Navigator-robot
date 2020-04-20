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

def curr(y = int(True),x = int(True)):
    currentcell = map1[x][y]
    print(currentcell)
    return currentcell




def get_target_cell(row,col):
    target_cell = i
    return target_cell
def adj_cell_up(row,col):
    adj_cell_up = map1[row - 1][col]
    return adj_cell_up
def adj_cell_down (row,col):
    adj_cell_down = map1[row + 1][col]
    return adj_cell_down
def adj_cell_left(row,col):
    adj_cell_left = map1[row][col - 1]
    return adj_cell_left

def adj_cell_right(row,col):
    adj_cell_right = map1[row][col + 1]
    return adj_cell_right
def decode(curr,left,right,up,down):
    if left < curr  :
        return left
    elif right < curr:
        return left
    elif up < curr:
        return up
    elif down < curr:
        return down



def move(adj,current,move_cell):
    if adj < current:
        move_cell = adj
        current = move_cell
        print(current)
curr(1,2)
