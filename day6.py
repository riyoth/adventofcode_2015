#!/usr/bin/python
#Answer 
#twitter
#Part 1: 
#Part 2:
#Github
#Part 1: 377891
#Part 2: 

#twitter input:
#s = ""
#github input: iwrupvqb
#Test
import re 
grid ={}
grid2 ={}
def turn_on(start,finish):
    for x in range(start[0],finish[0]+1):
        for y in range(start[1],finish[1]+1):
            grid[x,y]=True

def turn_off(start,finish):
    for x in range(start[0],finish[0]+1):
        for y in range(start[1],finish[1]+1):
            grid[x,y]=False

def toggle(start,finish):
    for x in range(start[0],finish[0]+1):
        for y in range(start[1],finish[1]+1):
            grid[x,y] = not grid[x,y]

def increase(start,finish,i):
    for x in range(start[0],finish[0]+1):
        for y in range(start[1],finish[1]+1):
            grid2[x,y]+= i
            if grid2[x,y] < 0:
                grid2[x,y]=0

def start():
    for x in range(1000):
        for y in range(1000):
            grid2[x,y]=0

def part1():
    d = {}
    turn_off((0,0),(1000,1000))
    d['turn on'] = turn_on
    d['turn off'] = turn_off
    d['toggle'] = toggle

    with open('day6.txt','r') as f:
        for x in f:
            m = re.search(r'(turn on|turn off|toggle) (\d+),(\d+) through (\d+),(\d+)',x)
            start = (int(m.group(2)),int(m.group(3)))
            finish = (int(m.group(4)),int(m.group(5)))
            action = m.group(1)
            d[action](start,finish)
    print('Part 1:',sum(grid.values()))
            

def part2():
    for x in range(1000):
        for y in range(1000):
            grid2[x,y]=0
    d = {}
    d['turn on'] = 1
    d['turn off'] = -1
    d['toggle'] = 2

    with open('day6.txt','r') as f:
        for x in f:
            m = re.search(r'(turn on|turn off|toggle) (\d+),(\d+) through (\d+),(\d+)',x)
            start = (int(m.group(2)),int(m.group(3)))
            finish = (int(m.group(4)),int(m.group(5)))
            action = m.group(1)
            increase(start,finish,d[action])

    print('Part 2:',sum(grid2.values()))


part1()
part2()
