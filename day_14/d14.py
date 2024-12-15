with open('input.txt') as f:
    robots = []
    for line in f.read().splitlines():        
        pos = line.split(' v=')
        pos_curr = pos[0].split('=')[1].split(',')
        pos_mov = pos[1].split(',')
        movs = list(map(int, pos_curr + pos_mov))
        robots.append(movs)

SECONDS = 100
R = 103
C = 101

class Robot:
    def __init__(self, sx, sy, mx, my):
        self.sx = sx
        self.sy = sy
        self.mx = mx
        self.my = my
    
    def move(self, R, C):
        # move 
        self.sx += self.mx
        self.sy += self.my           
        # go out of bounds on the right
        if self.sx >= C:
            self.sx = self.sx % C
        # go out of bounds on the left
        if self.sx < 0:
            self.sx = C + self.sx
        # go out of bounds on the bottom
        if self.sy >= R:
            self.sy = self.sy % R
        # go out of bounds on the top
        if self.sy < 0:
            self.sy = R + self.sy

    def get_current_position(self):
        return (self.sx, self.sy)
    
robots_current = []
robots_next = []
for sx, sy, mx, my in robots:
    robots_current.append(Robot(sx, sy, mx, my))


for _ in range(SECONDS):
    for robot in robots_current:
        robot.move(R, C)
        robots_next.append(robot)
    robots_current = robots_next
    robots_next = []

lu, ru, ld, rd = 0, 0, 0, 0
for robot in robots_current:
    x_pos, y_pos = robot.get_current_position()
    if x_pos < C // 2 and y_pos < R // 2:
        lu += 1
    if x_pos > C // 2 and y_pos < R // 2:
        ru += 1
    if x_pos < C // 2 and y_pos > R // 2:
        ld += 1
    if x_pos > C // 2 and y_pos > R // 2:
        rd += 1
    
print(lu * ru * ld * rd)

# part2
# SECONDS = 0
# # while True:
# #     SECONDS += 1
# #     for robot in robots_current:
# #         robot.move(R, C)
# #         robots_next.append(robot)
# #     if len([robot.get_current_position() for robot in robots_next]) == len(set([robot.get_current_position() for robot in robots_next])):
# #         print(SECONDS)
# #         break
# #     robots_current = robots_next
# #     robots_next = []