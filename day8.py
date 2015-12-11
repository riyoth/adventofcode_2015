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

def part1():
    total =0
    with open('day8.txt','r') as f:
        for x in f:
            total += len(x)-len(eval(x))-1
    print('Part 1:',total)

def part2():
    total =0
    with open('day8.txt','r') as f:
        for x in f:
            m = len(re.findall(r'\\x',x))
            m2 = len(re.findall(r'\"',x))
            total +=(len(x)-len(eval(x)))*2-5*m+len(x)-1 
            print((len(x)-len(eval(x)))+3*m+2*m2)
            #print((len(x)-1-len(eval(x)))*2)

    print('Part 2:',total)


part1()
part2()
