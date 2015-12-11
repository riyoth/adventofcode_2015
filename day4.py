#!/usr/bin/python
#Answer 
#twitter
#Part 1: 282749
#Part 2: 9962624
#Github
#Part 1: 346386
#Part 2: 9958218

#twitter input:
s = "yzbqklnj"
#github input: iwrupvqb
#s = "iwrupvqb"
import hashlib

def part1():
    for x in range(9999999999):
        y = hashlib.md5(bytearray(''.join((s,str(x))),'utf-8')).hexdigest()
        if y[:5] == '00000':
            print('Part 1 answer:',x,'hash:',y )
            break

def part2():
    for x in range(9999999999):
        y = hashlib.md5(bytearray(''.join((s,str(x))),'utf-8')).hexdigest()
        if y[:6] == '000000':
            print('Part 2 answer:',x,'hash:',y )
            break

part1()
part2()
