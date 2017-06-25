#!/usr/bin/python
#Answer 
#twitter
#Part 1: 
#Part 2:
#Github
#Part 1: 255
#Part 2: 55

#twitter input:
#s = ""
#github input: iwrupvqb
#Test
#l=('ugknbfddgicrmopn','aaa','jchzalrnumimnmhp','haegwjzuvuyypxyu','dvszwmarrgswjxmb')
#l= ('qjhvhtzxzqqjkmpb','xxyxx','uurcxstgmygtbstg','ieodomkazucvgmuy')
import re 
def part1():
    l = open('day7_input.txt')
    wire ={}
    gate = {
            'NOT' : '~',
            'OR' : '|',
            'AND' : '&',
            'RSHIFT' : '>>',
            'LSHIFT' : '<<'
            }
    for x in l:
        m = re.search(r'(.*\s){1,3}\-\> (\w{1,2})',x)
        try:
            wire[m.group(len(m.groups()))] = eval(' '.join([y for y in m.groups()[:len(m.groups())-1]]))
        except (AttributeError, NameError):
            print(x)
        try:
            print(wire['a'])
            break
        except KeyError:
            print('')
    print(wire)
    print('Part 1 answer:')

def part2():
    print('Part 2 answer:')
part1()
part2()
